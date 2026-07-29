#!/usr/bin/env python3
"""Extract the Chinese IMIC site, translate it, and emit HugoBlox content."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

import yaml
from bs4 import BeautifulSoup, NavigableString, Tag


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / ".source-cache/imic-raw/imic.nuist.edu.cn"
META = ROOT / "metadata"
CACHE_FILE = META / "translation-cache.json"
SOURCE_HOST = "https://imic.nuist.edu.cn"
SEPARATOR = "\n␞\n"

CATEGORY_SLUGS = {
    "综合新闻": "news",
    "通知公告": "announcements",
    "学术报告": "seminars",
    "研究成果": "research-highlights",
    "论文发表": "publications",
    "科研项目": "projects",
    "数据库下载": "datasets",
    "软件下载": "software",
    "研究方向": "research",
    "领导": "leadership",
    "工学教师": "engineering-faculty",
    "医学教师": "medical-faculty",
    "兼职教师": "adjunct-faculty",
    "合作者": "collaborators",
    "研究生": "graduate-students",
    "留学生": "international-students",
    "访问学生": "visiting-students",
    "毕业生": "alumni",
    "人才招聘·招生": "opportunities",
}

SECTION_SLUGS = {
    "新闻·通知": "news",
    "科学研究": "research",
    "研究队伍": "people",
    "学术交流": "academic-exchange",
    "实验室概况": "about",
    "人才招聘·招生": "opportunities",
}

TERM_FIXES = {
    "Jiangsu Provincial University Key Laboratory of Intelligent Medical Image Computing":
        "Jiangsu Key Laboratory of Intelligent Medical Image Computing",
    "Key Laboratory of Intelligent Medical Image Computing in Jiangsu Universities":
        "Jiangsu Key Laboratory of Intelligent Medical Image Computing",
    "Nanjing University of Information Science and Technology": "Nanjing University of Information Science & Technology",
    "Nanjing University of Information Engineering": "Nanjing University of Information Science & Technology",
    "IMIC Laboratory": "IMIC Lab",
}


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def canonical_url(path: Path) -> str:
    rel = path.relative_to(RAW).as_posix()
    if rel == "index.html":
        return SOURCE_HOST + "/"
    return SOURCE_HOST + "/" + rel


def source_asset_url(page: Path, src: str) -> str:
    if src.startswith(("http://", "https://")):
        return src
    rel = (page.parent / urllib.parse.unquote(src)).resolve()
    try:
        path = rel.relative_to(RAW.resolve()).as_posix()
    except ValueError:
        return urllib.parse.urljoin(canonical_url(page), src)
    return SOURCE_HOST + "/" + path


class Translator:
    def __init__(self, enabled: bool = True):
        self.enabled = enabled
        self.cache = json.loads(CACHE_FILE.read_text()) if CACHE_FILE.exists() else {}
        self.dirty = False

    def _request(self, text: str) -> str:
        params = urllib.parse.urlencode(
            {"client": "gtx", "sl": "zh-CN", "tl": "en", "dt": "t", "q": text}
        ).encode()
        req = urllib.request.Request(
            "https://translate.googleapis.com/translate_a/single",
            data=params,
            headers={"User-Agent": "Mozilla/5.0 IMIC-English-Site/1.0"},
        )
        for attempt in range(5):
            try:
                with urllib.request.urlopen(req, timeout=30) as response:
                    payload = json.load(response)
                return "".join(part[0] for part in payload[0] if part[0])
            except Exception:
                if attempt == 4:
                    raise
                time.sleep(1.5 * (attempt + 1))
        return text

    def translate(self, text: str) -> str:
        text = clean_text(text)
        if not text or not re.search(r"[\u3400-\u9fff]", text):
            return text
        key = hashlib.sha256(text.encode()).hexdigest()
        if key not in self.cache:
            self.cache[key] = self._request(text) if self.enabled else text
            self.dirty = True
        result = self.cache[key]
        for old, new in TERM_FIXES.items():
            result = result.replace(old, new)
        return result

    def translate_many(self, values: list[str]) -> list[str]:
        return [self.translate(value) for value in values]

    def bulk_translate(self, values: list[str], workers: int = 6) -> dict[str, str]:
        unique = []
        seen = set()
        for value in values:
            value = clean_text(value)
            if value and re.search(r"[\u3400-\u9fff]", value) and value not in seen:
                seen.add(value)
                unique.append(value)

        batches = []
        current = []
        current_size = 0
        for value in unique:
            addition = len(value) + 24
            if current and current_size + addition > 3200:
                batches.append(current)
                current, current_size = [], 0
            current.append(value)
            current_size += addition
        if current:
            batches.append(current)

        def translate_batch(batch):
            marked = "\n".join(
                f"⟦IMIC{i:05d}⟧\n{text}" for i, text in enumerate(batch)
            )
            translated = self._request(marked)
            chunks = re.split(r"⟦IMIC\d{5}⟧\s*", translated)[1:]
            if len(chunks) != len(batch):
                return {text: self._request(text) for text in batch}
            return {source: result.strip() for source, result in zip(batch, chunks)}

        translated_map = {}
        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = [executor.submit(translate_batch, batch) for batch in batches]
            for index, future in enumerate(as_completed(futures), 1):
                translated_map.update(future.result())
                if index % 10 == 0 or index == len(futures):
                    print(f"Translated batch {index}/{len(futures)}", flush=True)

        for source, result in translated_map.items():
            for old, new in TERM_FIXES.items():
                result = result.replace(old, new)
            key = hashlib.sha256(source.encode()).hexdigest()
            self.cache[key] = result
        self.dirty = bool(translated_map)
        return translated_map

    def save(self):
        if self.dirty:
            CACHE_FILE.write_text(
                json.dumps(self.cache, ensure_ascii=False, indent=2) + "\n"
            )


def discover_page(path: Path) -> dict | None:
    soup = BeautifulSoup(path.read_bytes(), "html.parser")
    title_node = soup.select_one(".art-tit h3, .cont-tit h3")
    body = soup.select_one("#vsb_content .v_news_content, #vsb_content")
    if not title_node or not body:
        return None

    section_node = soup.select_one(".channl-menu h2")
    active_node = soup.select_one(".channl-menu li.active a, .channl-menu li.on a")
    section_zh = clean_text(section_node.get_text(" ", strip=True)) if section_node else ""
    category_zh = clean_text(active_node.get_text(" ", strip=True)) if active_node else ""
    title_zh = clean_text(title_node.get_text(" ", strip=True))

    date = ""
    source = ""
    meta_text = [clean_text(x.get_text(" ", strip=True)) for x in soup.select(".art-tit p span")]
    for item in meta_text:
        if "发布日期" in item:
            match = re.search(r"\d{4}-\d{1,2}-\d{1,2}", item)
            if match:
                date = match.group(0)
        if "信息来源" in item:
            source = item.split("：", 1)[-1].strip()

    blocks = []
    seen_images = set()
    for node in body.descendants:
        if not isinstance(node, Tag):
            continue
        if node.name == "img":
            src = node.get("orisrc") or node.get("src")
            if not src:
                continue
            asset_url = source_asset_url(path, src)
            if asset_url in seen_images:
                continue
            width = int(re.sub(r"\D", "", str(node.get("width", "0"))) or 0)
            height = int(re.sub(r"\D", "", str(node.get("height", "0"))) or 0)
            if width <= 2 or height <= 2:
                continue
            seen_images.add(asset_url)
            blocks.append({"type": "image", "src": asset_url, "alt_zh": title_zh})
        elif node.name in {"p", "h1", "h2", "h3", "h4", "li"}:
            if node.find_parent(["p", "li", "h1", "h2", "h3", "h4"]):
                continue
            text = clean_text(node.get_text(" ", strip=True))
            if text:
                blocks.append({"type": "text", "text_zh": text})

    if not blocks:
        text = clean_text(body.get_text(" ", strip=True))
        if text:
            blocks.append({"type": "text", "text_zh": text})

    return {
        "source_url": canonical_url(path),
        "source_path": path.relative_to(RAW).as_posix(),
        "section_zh": section_zh,
        "category_zh": category_zh,
        "title_zh": title_zh,
        "date": date,
        "source": source,
        "blocks": blocks,
    }


def slug_for(page: dict) -> str:
    match = re.search(r"/info/\d+/(\d+)\.htm$", page["source_url"])
    return f"source-{match.group(1)}" if match else hashlib.sha1(page["source_url"].encode()).hexdigest()[:12]


def markdown_body(page: dict) -> str:
    lines = []
    for block in page["blocks"]:
        if block["type"] == "image":
            lines.extend([f'![{page["title_en"]}]({block["src"]})', ""])
        else:
            lines.extend([block.get("text_en", ""), ""])
    lines.extend(
        [
            "---",
            "",
            f'*This page was translated from the [original Chinese source]({page["source_url"]}).*',
            "",
        ]
    )
    return "\n".join(lines).strip() + "\n"


def emit_hugo(page: dict):
    category = page["category_slug"]
    if category in {"seminars"}:
        root = ROOT / "content/events"
        page_type = "event"
    elif category in {"research-highlights", "publications", "projects", "datasets", "software", "research"}:
        root = ROOT / "content/research"
        page_type = "research"
    elif page["section_slug"] == "people":
        root = ROOT / "content/people"
        page_type = "people"
    else:
        root = ROOT / "content/news"
        page_type = "blog"
    target = root / slug_for(page)
    target.mkdir(parents=True, exist_ok=True)
    date = page["date"] or "2000-01-01"
    front = {
        "title": page["title_en"],
        "date": f"{date}T00:00:00+08:00",
        "summary": page["summary_en"],
        "type": page_type,
        "categories": [page["category_en"]] if page["category_en"] else [],
        "tags": ["IMIC", page["section_en"]] if page["section_en"] else ["IMIC"],
        "source_url": page["source_url"],
        "source_language": "zh-CN",
        "translation_status": "machine-translated-and-terminology-normalized",
    }
    payload = "---\n" + yaml.safe_dump(front, sort_keys=False, allow_unicode=True).strip() + "\n---\n\n"
    (target / "index.md").write_text(payload + markdown_body(page))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-translate", action="store_true")
    args = parser.parse_args()
    META.mkdir(parents=True, exist_ok=True)
    translator = Translator(enabled=not args.no_translate)

    pages = []
    for path in sorted(RAW.glob("info/**/*.htm")):
        page = discover_page(path)
        if page:
            pages.append(page)

    all_strings = []
    for page in pages:
        all_strings.extend([page["section_zh"], page["category_zh"], page["title_zh"]])
        all_strings.extend(
            block["text_zh"] for block in page["blocks"] if block["type"] == "text"
        )
    if not args.no_translate:
        translator.bulk_translate(all_strings)
        translator.save()

    for index, page in enumerate(pages, 1):
        page["section_slug"] = SECTION_SLUGS.get(page["section_zh"], "other")
        page["category_slug"] = CATEGORY_SLUGS.get(
            page["category_zh"], page["section_slug"]
        )
        page["section_en"] = translator.translate(page["section_zh"])
        page["category_en"] = translator.translate(page["category_zh"])
        page["title_en"] = translator.translate(page["title_zh"])
        text_blocks = [b for b in page["blocks"] if b["type"] == "text"]
        for block in text_blocks:
            block["text_en"] = translator.translate(block["text_zh"])
        first_text = next((b.get("text_en", "") for b in text_blocks if b.get("text_en")), "")
        page["summary_en"] = first_text[:320].rsplit(" ", 1)[0] + ("…" if len(first_text) > 320 else "")
        emit_hugo(page)
        if index % 10 == 0:
            translator.save()
            print(f"Translated {index}/{len(pages)} pages", flush=True)

    translator.save()
    fetched_at = datetime.now(timezone.utc).isoformat()
    for page in pages:
        page["fetched_at"] = fetched_at
    with (META / "content.jsonl").open("w") as stream:
        for page in pages:
            stream.write(json.dumps(page, ensure_ascii=False) + "\n")
    inventory = {
        "source": SOURCE_HOST,
        "fetched_at": fetched_at,
        "page_count": len(pages),
        "sections": sorted({p["section_zh"] for p in pages}),
        "categories": sorted({p["category_zh"] for p in pages}),
        "translation_method": "Google machine translation with IMIC terminology normalization",
    }
    (META / "inventory.yaml").write_text(
        yaml.safe_dump(inventory, sort_keys=False, allow_unicode=True)
    )
    print(json.dumps(inventory, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
