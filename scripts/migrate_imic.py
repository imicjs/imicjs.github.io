#!/usr/bin/env python3
"""Convert the IMIC metadata archive into Hugoplate posts with real thumbnails."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlparse

import yaml
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / ".source-cache/imic-raw/imic.nuist.edu.cn"
POSTS = ROOT / "content/english/blog"
IMAGES = ROOT / "assets/images/content"

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
    candidate = RAW / path
    return candidate if candidate.is_file() else None


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


def section_for(page: dict) -> str:
    if page["category_slug"] == "seminars":
        return "academic-exchange"
    if page["section_slug"] == "opportunities":
        return "opportunities"
    return page["section_slug"]


def main():
    pages = [json.loads(line) for line in (ROOT / "metadata/content.jsonl").read_text().splitlines()]
    recovered = recover_listing_images()

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


if __name__ == "__main__":
    main()
