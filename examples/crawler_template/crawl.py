#!/usr/bin/env python3
"""爬虫骨架 —— 仅演示结构；真实站点需按合规与反爬策略定制。"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.request import Request, urlopen


def fetch(url: str, timeout: int = 20) -> str:
    req = Request(url, headers={"User-Agent": "ai-coding-services-sample/0.1"})
    with urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def parse_demo(html: str) -> list[dict[str, str]]:
    """占位解析：正式项目会换成 BeautifulSoup / lxml / 接口 JSON。"""
    title = "unknown"
    if "<title>" in html.lower():
        start = html.lower().find("<title>") + 7
        end = html.lower().find("</title>", start)
        if end > start:
            title = html[start:end].strip()
    return [{"field": "title", "value": title}]


def save(rows: list[dict[str, str]], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.suffix.lower() == ".json":
        output.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    else:
        with output.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["field", "value"])
            writer.writeheader()
            writer.writerows(rows)
    print(f"saved {len(rows)} rows -> {output}")


def main() -> None:
    parser = argparse.ArgumentParser(description="示例爬虫骨架（请仅用于合规公开页面）")
    parser.add_argument("--url", required=True, help="目标 URL")
    parser.add_argument("-o", "--output", type=Path, default=Path("out.csv"))
    args = parser.parse_args()
    html = fetch(args.url)
    rows = parse_demo(html)
    save(rows, args.output)


if __name__ == "__main__":
    main()
