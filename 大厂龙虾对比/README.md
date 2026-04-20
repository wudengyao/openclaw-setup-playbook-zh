# 大厂龙虾（Claw）对比研究报告（GitHub + 互联网）

> 研究日期：2026-03-15  
> 研究对象：AutoClaw、KimiQClaw（含 Kimi Claw 相关命名）、MaxClaw、QClaw（OpenClaw 作为基准）

## 快照归档（自动更新）

<!-- SNAPSHOT:LIST_START -->
- [数据快照-2026-04-20](数据快照-2026-04-20.md)
- [数据快照-2026-04-13](数据快照-2026-04-13.md)
- [数据快照-2026-04-06](数据快照-2026-04-06.md)
- [数据快照-2026-03-30](数据快照-2026-03-30.md)
- [数据快照-2026-03-23](数据快照-2026-03-23.md)
- [数据快照-2026-03-16](数据快照-2026-03-16.md)
- [数据快照-2026-03-15](数据快照-2026-03-15.md)
<!-- SNAPSHOT:LIST_END -->

---

## 1. 研究方法与证据分级

### 1.1 数据来源

- GitHub：仓库搜索结果、代表仓库主页信息。
- 互联网：官网/官方资源页、行业媒体报道、社区分析文章。

### 1.2 证据分级

- A 级（高可信）：官方站点、官方文档、官方仓库。
- B 级（中可信）：主流媒体/技术媒体报道。
- C 级（参考）：第三方评测、目录站、博客站点。

> 注：同名站点较多（尤其 `autoclaw`、`kimi claw`、`qclaw`），本报告仅引用可公开访问且可复查页面，不把所有同名域名都视为官方。

---

## 2. 结论先行（TL;DR）

1. **OpenClaw 是基准主线生态**：开源体量、贡献者规模、发布节奏、文档完整性显著领先。  
2. **AutoClaw/MaxClaw/QClaw 更接近“产品化分叉”**：强调一键部署、IM 入口、云托管。  
3. **KimiQClaw 在 GitHub 同名弱，但“Kimi Claw”在互联网有明确产品叙事**：需要按命名层做区分，不可简单等同。  
4. **互联网叙事与 GitHub 证据存在差异**：很多“能力声明”来自官网/媒体，不一定对应公开可审计代码。  
5. 对开源读者最稳妥的表达方式是：**“开源主线（OpenClaw）+ 产品化生态观察（Auto/Kimi/Max/Q）”**。

---

## 3. 主页可复用对比矩阵（详细版）

| 对象 | GitHub 信号（公开代码） | 互联网信号（产品/媒体） | 产品定位 | 风险提示 |
| --- | --- | --- | --- | --- |
| OpenClaw（基准） | `openclaw/openclaw`，约 313k stars、59.7k forks（抓取日） | 官方文档体系完善，含多渠道、部署、安全、运维 | 开源主框架 + 自托管优先 | 迭代快，配置与命令易变更 |
| AutoClaw | GitHub 搜索约 43 结果；头部如 `tsingliuwin/autoclaw`（约 76 stars） | 可见官方/半官方落地页强调本地执行、IM 回流、下载体验 | 一键安装/本地执行导向 | 同名站点多，需辨别“官方域名 vs 镜像站” |
| KimiQClaw（Kimi Claw） | 直接搜 `KimiQClaw` 几乎无仓库；更多是 `Kimi + OpenClaw` 组合信息 | `kimi.com` 资源页描述 Kimi Claw：一键云部署、5,000+ 技能、40GB 存储 | 云托管 + Kimi 生态融合 | 命名不统一（KimiQClaw/Kimi Claw/kimiclaw），需防误引 |
| MaxClaw | GitHub 搜索约 17 结果；头部如 `Lichas/maxclaw`（约 144 stars） | `maxclaw.ai` 强调云托管、10 秒部署、多平台接入、低成本 | 云托管与低门槛部署 | 许多性能/成本说法来自自述，需独立验证 |
| QClaw | GitHub 搜索约 37 结果；相关高热项目集中在 WeChat 接入周边（如 723/464 stars） | `qclaw.qq.com`（腾讯）页面突出微信直连、Mac/Win 下载、Skills 生态 | 微信入口 + 本地执行 + 远程操控 | 渠道自动化涉及合规边界，企业需审计风控 |

---

## 4. 分对象深度观察

### 4.1 AutoClaw

**GitHub 侧：**

- 关键词集中在“自动部署 OpenClaw”“轻量代理”“容器化”。
- 同名仓多、质量分布离散，头部仓外大量低活跃项目。

**互联网侧：**

- 可检索到面向中文用户的一键部署/本地执行叙事页面（强调 IM 入口、执行回流、下载即用）。

**判断：**

- 更偏“产品包装与交付层”，不完全等于新的独立开源主框架。

### 4.2 KimiQClaw（Kimi Claw）

**GitHub 侧：**

- 直接关键词 `KimiQClaw` 基本无仓库沉淀。

**互联网侧：**

- `kimi.com` 资源页提供较完整产品叙事：
  - 一键云部署；
  - 5,000+ skills；
  - 40GB 云存储；
  - 与 OpenClaw 的对比表述；
  - 同时可链接本地 OpenClaw 方案。
- `docs.openclaw.ai/providers/moonshot` 证实 OpenClaw 对 Moonshot/Kimi 模型有官方 provider 支持。

**判断：**

- 建议采用“**Kimi Claw（产品）** + **OpenClaw（开源主线）”双层表述，避免单独使用 `KimiQClaw` 当作标准项目名。

### 4.3 MaxClaw

**GitHub 侧：**

- 存在同名项目群，头部仓热度中等，尚未形成单一官方开源中心。

**互联网侧：**

- `maxclaw.ai` 对外叙事明确：云托管、一键部署、多渠道接入、长记忆、成本优势。
- 第三方技术媒体（如 SitePoint）也将其归类为“平台化代理方案”，并强调待验证项（定价、SLA、合规）。

**判断：**

- 产品化信号强于开源统一性，适合在报告里归入“托管平台路线”。

### 4.4 QClaw

**GitHub 侧：**

- 高热仓多与 WeChat 接入、SDK、客户端、旁路工具相关；
- 代码生态更像“渠道集成层”而非单主仓核心 runtime。

**互联网侧：**

- `qclaw.qq.com` 显示腾讯品牌、下载链接（Mac/Win）、微信直连、Skills 生态、持续记忆等主张。
- 媒体报道多聚焦“打包 OpenClaw 做一键部署 + 接入微信/QQ”这一定位。

**判断：**

- 在中国 IM 场景具备高可见度，但企业落地前必须做权限、审计、自动化边界评估。

---

## 5. 对你项目的落地建议

### 5.1 文档策略

建议长期分两层写法：

- 层 A（可审计）：GitHub 开源证据（仓库、stars、提交活跃度）。
- 层 B（市场侧）：官网与媒体叙事（能力声明、定位、价格、场景）。

### 5.2 你仓库中的推荐目录

- [大厂龙虾对比/README.md](README.md)：主报告（本文件）
- `大厂龙虾对比/数据快照-YYYY-MM-DD.md`：月度快照
- `大厂龙虾对比/评估模板.md`：统一打分模板（透明度、合规、成本、可运维性）

### 5.3 统一评分维度（建议）

- 开源可审计性（代码可见、License、Issue 活跃）
- 产品可用性（安装门槛、运行稳定性、渠道接入）
- 企业可落地性（安全、合规、审计、数据边界）
- 总拥有成本（模型费用 + 托管/运维费用）
- 供应商锁定风险（迁移难度、兼容性）

---

## 6. 证据清单（可复查）

### 6.1 GitHub

- OpenClaw 主仓：[openclaw/openclaw](https://github.com/openclaw/openclaw)
- AutoClaw 搜索：[GitHub Search - AutoClaw](https://github.com/search?q=autoclaw&type=repositories)
- KimiQClaw 搜索：[GitHub Search - KimiQClaw](https://github.com/search?q=KimiQClaw&type=repositories)
- MaxClaw 搜索：[GitHub Search - MaxClaw](https://github.com/search?q=MaxClaw&type=repositories)
- QClaw 搜索：[GitHub Search - QClaw](https://github.com/search?q=QClaw&type=repositories)

### 6.2 官网 / 官方资源（A 级）

- AutoClaw（智谱入口页）：[autoglm.zhipuai.cn/autoclaw](https://autoglm.zhipuai.cn/autoclaw/)
- QClaw（腾讯）：[qclaw.qq.com](https://qclaw.qq.com/)
- Kimi Claw（Kimi 资源页）：[Kimi Claw Introduction](https://www.kimi.com/resources/kimi-claw-introduction)
- OpenClaw Moonshot Provider（官方文档）：[docs.openclaw.ai/providers/moonshot](https://docs.openclaw.ai/providers/moonshot)
- MaxClaw 官网：[maxclaw.ai](https://maxclaw.ai/)

### 6.3 媒体 / 第三方（B/C 级）

- TechNode（QClaw 报道）：[Tencent reportedly tests QClaw](https://technode.com/2026/03/09/tencent-reportedly-tests-qclaw-ai-agent-with-one-click-openclaw-deployment/)
- SitePoint（MaxClaw 分析）：[MaxClaw by MiniMax](https://www.sitepoint.com/maxclaw-minimax-ai-agents-update/)
- DuckDuckGo 互联网检索入口：
  - [AutoClaw](https://html.duckduckgo.com/html/?q=AutoClaw)
  - [Kimi OpenClaw](https://html.duckduckgo.com/html/?q=Kimi+OpenClaw)
  - [MaxClaw AI agent](https://html.duckduckgo.com/html/?q=MaxClaw+AI+agent)
  - [QClaw AI](https://html.duckduckgo.com/html/?q=QClaw+AI)

---

## 7. 风险与边界声明

- 本报告是“公开情报对比”，不构成安全背书或法律意见。  
- 对“成本/性能/上下文长度/可用性”类信息，若仅来自官网或媒体声明，均应在生产前自行压测验证。  
- 涉及远程控制、自动执行、IM 回流时，请优先完成：权限最小化、审计日志、人工确认闸门。

---

## 8. 结语

这份版本已经从“仅 GitHub 对比”升级为“**GitHub + 互联网双源对比**”。后续建议每月更新一次快照，重点跟踪：

- 是否出现新的官方仓库或官方 API 文档；
- 宣称能力是否在开源代码中可验证；
- 价格、合规、SLA 是否有公开更新。
