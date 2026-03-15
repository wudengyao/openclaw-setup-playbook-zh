#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import re
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
USECASES_FILE = ROOT / "全网实战案例" / "awesome-openclaw-usecases-40例.md"
SHOWCASE_FILE = ROOT / "全网实战案例" / "official-showcase-案例汇总.md"
SKILLS_INDEX_FILE = ROOT / "全网实战案例" / "awesome-openclaw-skills-全网实战索引.md"
SKILLS_DIR = ROOT / "全网实战案例" / "skills-categories"


def count_usecases() -> int:
    text = USECASES_FILE.read_text(encoding="utf-8")
    nums = [int(n) for n in re.findall(r"^\s*(\d+)\.\s", text, flags=re.M)]
    return max(nums) if nums else 0


def count_showcases() -> int:
    text = SHOWCASE_FILE.read_text(encoding="utf-8")
    # 只统计官方案例条目，按「- xxx」计数
    return len(re.findall(r"^\s*-\s+", text, flags=re.M))


def count_skill_categories() -> int:
    return len(list(SKILLS_DIR.glob("*.md")))


def get_skills_ecosystem_size() -> str:
    text = SKILLS_INDEX_FILE.read_text(encoding="utf-8")
    m = re.search(r"(\d[\d,]*\+)", text)
    return m.group(1).replace(",", "") if m else "5400+"


def badge(label: str, message: str, color: str) -> str:
    l = quote(label, safe="")
    m = quote(message, safe="")
    return f"https://img.shields.io/badge/{l}-{m}-{color}?style=for-the-badge"


def replace_between(text: str, start_pat: str, end_pat: str, new_block: str) -> str:
    pattern = re.compile(rf"({start_pat}\n)([\s\S]*?)(\n{end_pat})")
    return pattern.sub(rf"\1{new_block}\3", text, count=1)


def main() -> None:
    today = dt.date.today().isoformat()
    last_sync_for_badge = today.replace("-", "--")
    usecases = count_usecases()
    showcase = count_showcases()
    categories = count_skill_categories()
    skills_total = get_skills_ecosystem_size()

    badges = [
        f"![awesome]({badge('awesome', 'openclaw', '7b68ee')})",
        f"![community usecases]({badge('community usecases', str(usecases), '0ea5e9')})",
        f"![official showcase]({badge('official showcase', f'{showcase}+', 'f97316')})",
        f"![skills categories mirrored]({badge('skills categories mirrored', str(categories), '22c55e')})",
        f"![skills ecosystem]({badge('skills ecosystem', skills_total, '06b6d4')})",
        f"![last sync]({badge('last sync', last_sync_for_badge, '64748b')})",
    ]
    badges_block = "\n".join(badges)

    summary_block = "\n".join(
        [
            f"- 社区案例：{usecases}（来源：`全网实战案例/awesome-openclaw-usecases-40例.md`）",
            f"- 官方案例：{showcase}+（来源：`全网实战案例/official-showcase-案例汇总.md`）",
            f"- skills 分类镜像：{categories} 类（来源：`全网实战案例/skills-categories/`）",
            f"- skills 生态规模：{skills_total}（来源：`全网实战案例/awesome-openclaw-skills-全网实战索引.md`）",
        ]
    )

    text = README.read_text(encoding="utf-8")

    # 更新时间：有则替换，无则插入在目标说明前
    if re.search(r"^> 更新时间：", text, flags=re.M):
        text = re.sub(r"^> 更新时间：.*$", f"> 更新时间：{today}  ", text, flags=re.M, count=1)
    else:
        text = re.sub(r"(^> 目标：)", f"> 更新时间：{today}  \n\\1", text, flags=re.M, count=1)

    # 徽章区替换：在“目标”与“### 数据说明”之间
    text = re.sub(
        r"(?ms)(^> 目标：.*?\n)(.*?)(^### 数据说明（这些开源项目常见怎么做）)",
        lambda m: m.group(1)
        + "\n## 📊 项目数据看板（自动更新）\n\n"
        + badges_block
        + "\n\n"
        + m.group(3),
        text,
        count=1,
    )

    # 口径区替换：在“### 本仓库当前口径”与下一个二级标题之间
    text = re.sub(
        r"(?ms)(^### 本仓库当前口径\n\n)(.*?)(^##\s)",
        lambda m: m.group(1) + summary_block + "\n\n" + m.group(3),
        text,
        count=1,
    )

    README.write_text(text, encoding="utf-8")
    print("README metrics updated")
    print(f"usecases={usecases}, showcase={showcase}, categories={categories}, skills={skills_total}, date={today}")


if __name__ == "__main__":
    main()
