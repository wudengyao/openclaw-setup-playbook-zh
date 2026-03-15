#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMPARE_DIR = ROOT / "大厂龙虾对比"
REPORT = COMPARE_DIR / "README.md"


def extract_section(text: str, heading: str, next_heading: str | None = None) -> str:
    if next_heading:
        pattern = re.compile(rf"(?ms)^## {re.escape(heading)}\n(.*?)^## {re.escape(next_heading)}\n")
        m = pattern.search(text)
        return m.group(1).strip() if m else ""
    pattern = re.compile(rf"(?ms)^## {re.escape(heading)}\n(.*)$")
    m = pattern.search(text)
    return m.group(1).strip() if m else ""


def upsert_snapshot_index(report_text: str) -> str:
    files = sorted(COMPARE_DIR.glob("数据快照-*.md"), reverse=True)
    lines = [f"- [{f.stem}]({f.name})" for f in files[:12]]
    block = "\n".join(lines) if lines else "- 暂无快照"
    pattern = re.compile(r"(?ms)(<!-- SNAPSHOT:LIST_START -->\n)(.*?)(\n<!-- SNAPSHOT:LIST_END -->)")
    return pattern.sub(rf"\1{block}\3", report_text, count=1)


def main() -> None:
    today = dt.date.today().isoformat()
    snapshot_file = COMPARE_DIR / f"数据快照-{today}.md"

    report_text = REPORT.read_text(encoding="utf-8")

    tldr = extract_section(report_text, "2. 结论先行（TL;DR）", "3. 主页可复用对比矩阵（详细版）")
    matrix = extract_section(report_text, "3. 主页可复用对比矩阵（详细版）", "4. 分对象深度观察")
    sources = extract_section(report_text, "6. 证据清单（可复查）", "7. 风险与边界声明")

    snapshot_content = "\n".join(
        [
            f"# 大厂龙虾对比数据快照（{today}）",
            "",
            f"> 自动生成时间：{today}",
            f"> 来源主报告：[大厂龙虾对比/README.md](README.md)",
            "",
            "---",
            "",
            "## 结论先行（TL;DR）",
            "",
            tldr if tldr else "- 本次未提取到 TL;DR，请检查主报告结构。",
            "",
            "---",
            "",
            "## 对比矩阵（当期）",
            "",
            matrix if matrix else "- 本次未提取到对比矩阵，请检查主报告结构。",
            "",
            "---",
            "",
            "## 证据清单（当期）",
            "",
            sources if sources else "- 本次未提取到证据清单，请检查主报告结构。",
            "",
        ]
    )

    snapshot_file.write_text(snapshot_content, encoding="utf-8")

    updated_report = upsert_snapshot_index(report_text)
    REPORT.write_text(updated_report, encoding="utf-8")

    print(f"snapshot={snapshot_file.name}")
    print("comparison report snapshot index updated")


if __name__ == "__main__":
    main()
