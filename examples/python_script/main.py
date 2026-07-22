#!/usr/bin/env python3
"""批处理脚本骨架 —— 演示交付形态，正式需求按 brief 定制。"""

from __future__ import annotations

import argparse
from pathlib import Path


def run(input_path: Path, output_path: Path) -> None:
    lines = input_path.read_text(encoding="utf-8").splitlines()
    cleaned = [line.strip() for line in lines if line.strip()]
    output_path.write_text("\n".join(cleaned) + ("\n" if cleaned else ""), encoding="utf-8")
    print(f"done: {len(cleaned)} lines -> {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="示例：清洗文本文件空行")
    parser.add_argument("-i", "--input", type=Path, required=True, help="输入文件")
    parser.add_argument("-o", "--output", type=Path, required=True, help="输出文件")
    args = parser.parse_args()
    run(args.input, args.output)


if __name__ == "__main__":
    main()
