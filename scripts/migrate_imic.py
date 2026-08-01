#!/usr/bin/env python3
"""Convert the IMIC metadata archive into Hugoplate posts with real thumbnails."""

from __future__ import annotations

import json
import hashlib
import re
import shutil
import subprocess
from bisect import bisect_right
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse
from urllib.request import Request, urlopen

import yaml
from bs4 import BeautifulSoup, Comment, NavigableString

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / ".source-cache/imic-raw/imic.nuist.edu.cn"
POSTS = ROOT / "content/english/blog"
IMAGES = ROOT / "assets/images/content"
ARTICLE_IMAGES = ROOT / "assets/images/articles"
EXTERNAL_CACHE = ROOT / ".source-cache/external-images"

SECTION_NAMES = {
    "news": "News",
    "people": "People",
    "research": "Research",
    "academic-exchange": "Events",
    "opportunities": "Opportunities",
    "other": "Archive",
}

FALLBACKS = {
    "news": RAW / "images/ban3.jpg",
    "people": RAW / "images/ban002.jpg",
    "research": RAW / "images/ban2.jpg",
    "academic-exchange": RAW / "images/s2-bg.jpg",
    "opportunities": RAW / "images/s4-bg.jpg",
    "other": RAW / "images/ban3.jpg",
}


def local_asset(url: str) -> Path | None:
    path = unquote(urlparse(url).path).lstrip("/")
    candidates = [RAW / path, ROOT / "assets" / path]
    return next((candidate for candidate in candidates if candidate.is_file()), None)


def normalized_text(value: str) -> str:
    """Normalize source text so image positions survive rich-text span markup."""
    return re.sub(r"\s+", "", value or "")


def resolve_source_image(src: str, html_path: Path) -> Path | None:
    """Resolve a source image locally, downloading cross-site legacy assets if needed."""
    parsed = urlparse(src)
    if parsed.scheme in {"http", "https"}:
        candidate = RAW / unquote(parsed.path).lstrip("/")
        if candidate.is_file():
            return candidate
        suffix = Path(parsed.path).suffix.lower() or ".jpg"
        cache_name = f"{hashlib.sha256(src.encode()).hexdigest()[:16]}{suffix}"
        cached = EXTERNAL_CACHE / cache_name
        if not cached.is_file():
            EXTERNAL_CACHE.mkdir(parents=True, exist_ok=True)
            try:
                request = Request(src, headers={"User-Agent": "Mozilla/5.0 IMIC archive repair"})
                with urlopen(request, timeout=30) as response:
                    cached.write_bytes(response.read())
            except Exception:
                return None
        return cached

    if src.startswith("/"):
        candidate = RAW / unquote(src).lstrip("/")
    else:
        candidate = (html_path.parent / unquote(src)).resolve()
    try:
        candidate.relative_to(RAW.resolve())
    except ValueError:
        return None
    return candidate if candidate.is_file() else None


def article_blocks(page: dict, source_id: str) -> tuple[list[dict], dict]:
    """Insert source article images and videos into the translated block sequence."""
    html_path = RAW / page["source_path"]
    soup = BeautifulSoup(html_path.read_bytes(), "html.parser")
    content = soup.select_one(".v_news_content") or soup.select_one("#vsb_content")
    text_blocks = [
        block for block in page["blocks"] if block["type"] not in {"image", "video"}
    ]
    if content is None:
        return text_blocks, {"source_id": source_id, "source_images": 0, "localized_images": 0}

    source_text = normalized_text(content.get_text("", strip=False))
    cursor = 0
    text_ends = []
    unmatched_text_blocks = 0
    for block in text_blocks:
        needle = normalized_text(block.get("text_zh", ""))
        start = source_text.find(needle, cursor) if needle else cursor
        if start < 0:
            unmatched_text_blocks += 1
            start = cursor
        cursor = start + len(needle)
        text_ends.append(cursor)

    media_events = []
    text_offset = 0
    for node in content.descendants:
        if (
            isinstance(node, NavigableString)
            and not isinstance(node, Comment)
            and getattr(node.parent, "name", None) not in {"style", "script"}
        ):
            text_offset += len(normalized_text(str(node)))
            continue
        node_name = getattr(node, "name", None)
        if node_name == "script" and node.get("name") == "_videourl":
            video_src = node.get("vurl")
            if video_src:
                media_events.append(
                    (
                        text_offset,
                        {
                            "type": "video",
                            "src": urljoin(page["source_url"], video_src),
                            "width": int(node.get("vwidth") or 16),
                            "height": int(node.get("vheight") or 9),
                            "original_src": video_src,
                        },
                    )
                )
            continue
        if node_name != "img":
            continue
        original_src = node.get("orisrc") or node.get("src") or node.get("data-src")
        if not original_src:
            continue
        source_file = resolve_source_image(original_src, html_path)
        if source_file is None:
            media_events.append(
                (
                    text_offset,
                    {
                        "type": "image",
                        "source_file": None,
                        "original_src": original_src,
                        "alt": node.get("alt", ""),
                    },
                )
            )
            continue
        media_events.append(
            (
                text_offset,
                {
                    "type": "image",
                    "source_file": source_file,
                    "original_src": original_src,
                    "alt": node.get("alt", ""),
                },
            )
        )

    target_dir = ARTICLE_IMAGES / f"source-{source_id}"
    if target_dir.exists():
        shutil.rmtree(target_dir)
    target_dir.mkdir(parents=True, exist_ok=True)

    buckets: list[list[dict]] = [[] for _ in range(len(text_blocks) + 1)]
    missing_images = []
    localized = 0
    source_videos = 0
    for position, media in media_events:
        insertion_index = bisect_right(text_ends, position)
        if media["type"] == "video":
            source_videos += 1
            buckets[insertion_index].append(media)
            continue
        source_file = media["source_file"]
        original_src = media["original_src"]
        if source_file is None:
            missing_images.append(original_src)
            continue
        localized += 1
        target = target_dir / f"{localized:02d}.webp"
        write_article_image(source_file, target)
        buckets[insertion_index].append(
            {
                "type": "image",
                "src": f"/images/articles/source-{source_id}/{target.name}",
                "alt_zh": media["alt"] or page["title_zh"],
                "original_src": original_src,
            }
        )

    repaired: list[dict] = []
    for index, text_block in enumerate(text_blocks):
        repaired.extend(buckets[index])
        repaired.append(text_block)
    repaired.extend(buckets[-1])
    return repaired, {
        "source_id": source_id,
        "source_path": page["source_path"],
        "source_images": sum(media["type"] == "image" for _, media in media_events),
        "localized_images": localized,
        "source_videos": source_videos,
        "embedded_videos": source_videos,
        "missing_images": missing_images,
        "unmatched_text_blocks": unmatched_text_blocks,
    }


def recover_listing_images() -> dict[str, Path]:
    """Recover thumbnails shown on source listing cards but absent from articles."""
    recovered: dict[str, Path] = {}
    pattern = re.compile(r"(?:\.\./)*info/(\d+)/(\d+)\.htm")
    for html in list(RAW.rglob("*.htm")) + list(RAW.rglob("*.html")):
        try:
            soup = BeautifulSoup(html.read_bytes(), "html.parser")
        except Exception:
            continue
        for anchor in soup.find_all("a", href=True):
            match = pattern.search(anchor["href"])
            if not match:
                continue
            source_path = f"info/{match.group(1)}/{match.group(2)}.htm"
            candidates = []
            for container in [anchor, *list(anchor.parents)[:4]]:
                if hasattr(container, "find_all"):
                    candidates.extend(container.find_all("img", src=True))
            for image in candidates:
                src = image.get("orisrc") or image.get("src")
                if not src or src.endswith(("default.jpg", "tit-line.png")):
                    continue
                candidate = (html.parent / unquote(src)).resolve()
                try:
                    candidate.relative_to(RAW.resolve())
                except ValueError:
                    continue
                if candidate.is_file():
                    recovered.setdefault(source_path, candidate)
                    break
            if source_path in recovered:
                continue
            for container in [anchor, *list(anchor.parents)[:4]]:
                if not hasattr(container, "find_all"):
                    continue
                styled = [container, *container.find_all(style=True)]
                for element in styled:
                    match_url = re.search(
                        r"background-image\s*:\s*url\(['\"]?([^'\")]+)",
                        element.get("style", ""),
                    )
                    if not match_url:
                        continue
                    candidate = (html.parent / unquote(match_url.group(1))).resolve()
                    try:
                        candidate.relative_to(RAW.resolve())
                    except ValueError:
                        continue
                    if candidate.is_file():
                        recovered.setdefault(source_path, candidate)
                        break
                if source_path in recovered:
                    break
    return recovered


def write_thumbnail(source: Path, target: Path):
    target.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        [
            "sips",
            "-Z",
            "1400",
            "-s",
            "format",
            "jpeg",
            "-s",
            "formatOptions",
            "78",
            str(source),
            "--out",
            str(target),
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode:
        raise RuntimeError(f"Unable to process {source}: {result.stderr}")


def write_article_image(source: Path, target: Path):
    """Create a web-ready WebP without enlarging the original source image."""
    dimensions = subprocess.run(
        ["sips", "-g", "pixelWidth", str(source)],
        capture_output=True,
        text=True,
        check=True,
    )
    match = re.search(r"pixelWidth:\s*(\d+)", dimensions.stdout)
    width = int(match.group(1)) if match else 0
    command = ["cwebp", "-quiet", "-mt", "-m", "6", "-q", "82"]
    if width > 1920:
        command.extend(["-resize", "1920", "0"])
    command.extend([str(source), "-o", str(target)])
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(f"Unable to process article image {source}: {result.stderr}")


def section_for(page: dict) -> str:
    if page["category_slug"] == "seminars":
        return "academic-exchange"
    if page["section_slug"] == "opportunities":
        return "opportunities"
    return page["section_slug"]


def main():
    pages = [json.loads(line) for line in (ROOT / "metadata/content.jsonl").read_text().splitlines()]
    recovered = recover_listing_images()

    audit = []
    for page in pages:
        source_id = re.search(r"/(\d+)\.htm$", page["source_url"]).group(1)
        page["blocks"], page_audit = article_blocks(page, source_id)
        audit.append(page_audit)

    (ROOT / "metadata/content.jsonl").write_text(
        "\n".join(json.dumps(page, ensure_ascii=False) for page in pages) + "\n"
    )
    (ROOT / "metadata/image-audit.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n"
    )

    POSTS.mkdir(parents=True, exist_ok=True)
    for old in POSTS.glob("post-*.md"):
        old.unlink()
    IMAGES.mkdir(parents=True, exist_ok=True)

    manifest = []
    for page in pages:
        source_id = re.search(r"/(\d+)\.htm$", page["source_url"]).group(1)
        section = section_for(page)
        body_image = next(
            (
                local_asset(block["src"])
                for block in page["blocks"]
                if block["type"] == "image" and local_asset(block["src"])
            ),
            None,
        )
        source_image = body_image or recovered.get(page["source_path"]) or FALLBACKS[section]
        image_origin = (
            "article"
            if body_image
            else "listing"
            if page["source_path"] in recovered
            else f"section-fallback:{section}"
        )
        thumbnail = IMAGES / f"source-{source_id}.jpg"
        write_thumbnail(source_image, thumbnail)

        section_name = SECTION_NAMES[section]
        categories = [section_name]
        if page["category_en"] and page["category_en"] != section_name:
            categories.append(page["category_en"])

        frontmatter = {
            "title": page["title_en"],
            "meta_title": page["title_en"],
            "description": page["summary_en"],
            "date": f"{page['date'] or '2000-01-01'}T00:00:00+08:00",
            "image": f"/images/content/source-{source_id}.jpg",
            "categories": categories,
            "author": "IMIC Lab",
            "tags": ["IMIC", section_name],
            "draft": False,
            "source_url": page["source_url"],
            "translation_status": page.get(
                "translation_status", "machine-translated-and-terminology-normalized"
            ),
        }

        body = []
        for block in page["blocks"]:
            if block["type"] == "image":
                body.extend([f"![{page['title_en']}]({block['src']})", ""])
            elif block["type"] == "video":
                ratio = f"{block['width']} / {block['height']}"
                body.extend(
                    [
                        (
                            '<div class="imic-article-video" '
                            f'style="--video-aspect: {ratio}">\n'
                            '  <video controls preload="metadata" playsinline '
                            f'aria-label="{page["title_en"]}">\n'
                            f'    <source src="{block["src"]}" type="video/mp4">\n'
                            "    Your browser does not support HTML5 video.\n"
                            "  </video>\n"
                            "</div>"
                        ),
                        "",
                    ]
                )
            elif block.get("text_en"):
                body.extend([block["text_en"], ""])
        body.extend(
            [
                "---",
                "",
                f"*Translated from the [original Chinese source]({page['source_url']}).*",
                "",
            ]
        )
        output = "---\n" + yaml.safe_dump(
            frontmatter, sort_keys=False, allow_unicode=True, width=1000
        ) + "---\n\n" + "\n".join(body)
        (POSTS / f"source-{source_id}.md").write_text(output)
        manifest.append(
            {
                "source_id": source_id,
                "source_url": page["source_url"],
                "thumbnail": f"assets/images/content/source-{source_id}.jpg",
                "thumbnail_origin": image_origin,
                "original_asset": str(source_image.relative_to(ROOT)),
            }
        )

    (ROOT / "metadata/thumbnail-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    )
    counts = {}
    for item in manifest:
        counts[item["thumbnail_origin"]] = counts.get(item["thumbnail_origin"], 0) + 1
    print(json.dumps({"pages": len(pages), "thumbnail_sources": counts}, indent=2))
    print(
        json.dumps(
            {
                "article_image_pages": sum(item["source_images"] > 0 for item in audit),
                "source_images": sum(item["source_images"] for item in audit),
                "localized_images": sum(item["localized_images"] for item in audit),
                "source_videos": sum(item.get("source_videos", 0) for item in audit),
                "embedded_videos": sum(item.get("embedded_videos", 0) for item in audit),
                "missing_images": sum(len(item.get("missing_images", [])) for item in audit),
                "unmatched_text_blocks": sum(item["unmatched_text_blocks"] for item in audit),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
