# VoltAgent 全网技能实战索引（5400+）

> 来源仓库：https://github.com/VoltAgent/awesome-openclaw-skills  
> 抓取时间：2026-03-15  
> 说明：该仓库维护的是 OpenClaw 技能生态“全量目录”，可视作“全网实战场景库”（按类别组织）。

---

## 1）全量说明

- 仓库声明：收录 **5400+** 社区技能（来自官方 Skills Registry 的筛选聚合）
- 结构方式：
  - 根 `README.md`：总目录 + 类别统计 + 部分类别示例
  - `categories/*.md`：各类别下的完整条目列表（每条通常包含技能名、描述、源链接）

这意味着：
- 如果要“全量抓取实战案例”，需要以 `categories/*.md` 为主数据源。

---

## 2）类别总览（来自仓库目录统计）

> 以下计数为仓库 README 中公开的类别统计（会动态变化）：

- Git & GitHub（170）
- Coding Agents & IDEs（1222）
- Browser & Automation（335）
- Web & Frontend Development（938）
- DevOps & Cloud（409）
- Image & Video Generation（169）
- Apple Apps & Services（44）
- Search & Research（352）
- Clawdbot Tools（37）
- CLI Utilities（186）
- Marketing & Sales（105）
- Productivity & Tasks（206）
- AI & LLMs（197）
- Data & Analytics（28）
- Finance（21）
- Media & Streaming（85）
- Notes & PKM（71）
- iOS & macOS Development（29）
- Transportation（110）
- Personal Development（51）
- Health & Fitness（88）
- Communication（149）
- Speech & Transcription（45）
- Smart Home & IoT（43）
- Shopping & E-commerce（55）
- Calendar & Scheduling（65）
- PDF & Documents（111）
- Self-Hosted & Automation（33）
- Security & Passwords（54）
- Moltbook（29）
- Gaming（36）
- Agent-to-Agent Protocols（17）

---

## 3）全量入口（直接可用）

- 总入口（README）：  
  https://github.com/VoltAgent/awesome-openclaw-skills

- 类别目录（建议从这里逐类抓取）：  
  https://github.com/VoltAgent/awesome-openclaw-skills/tree/main/categories

- 典型类别页示例：
  - Git & GitHub：
    https://github.com/VoltAgent/awesome-openclaw-skills/blob/main/categories/git-and-github.md
  - Coding Agents & IDEs：
    https://github.com/VoltAgent/awesome-openclaw-skills/blob/main/categories/coding-agents-and-ides.md
  - Browser & Automation：
    https://github.com/VoltAgent/awesome-openclaw-skills/blob/main/categories/browser-and-automation.md

---

## 4）如何把“全部案例”持续同步到你的仓库（建议流程）

### A. 一次性同步

1. 抓取 `categories` 目录下全部 `.md` 文件
2. 按原文件名保存到本仓库，例如：
   - `全网实战案例/skills-categories/git-and-github.md`
   - `全网实战案例/skills-categories/browser-and-automation.md`
3. 建立索引页，自动链接全部分类文件

### B. 定期增量同步（每周/每月）

1. 比较上游 commit（`awesome-openclaw-skills`）
2. 仅更新变更的分类文件
3. 在索引页附“最后同步时间”

---

## 5）安全提醒（非常重要）

- 技能条目属于“收录与分类”，并不代表全部经过安全审计。
- 上线前必须做三件事：
  1) 审源码；2) 审权限；3) 先在沙箱环境试运行。
- 涉及外发消息、资金、删除类操作，必须加人工确认。

---

## 6）本次已完成内容

- 已将 VoltAgent 生态加入“全网实战案例”目录
- 已补齐“全量入口 + 类别统计 + 同步方法”
- 你现在可以直接把该页作为“全网实战案例总入口（技能生态）”对外分享
