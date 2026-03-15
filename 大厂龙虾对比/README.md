# 大厂龙虾（Claw）生态对比研究报告

> 研究日期：2026-03-15  
> 研究对象：AutoClaw、KimiQClaw、MaxClaw、QClaw（并以 OpenClaw 作为基准组）

---

## 1. 研究方法与口径

- 公开可验证来源：GitHub 仓库与搜索结果页、官方仓库 README、公开文档。
- 对比维度：
  - 公开可见度（是否有官方/主仓）
  - 社区热度（代表仓库 stars）
  - 技术定位（运行时、渠道、部署偏好）
  - 生态成熟度（文档、版本、贡献者规模）
  - 适合场景（个人、本地私有化、企业导向）
- 说明：`KimiQClaw/MaxClaw/QClaw` 中部分命名存在“社区自发命名/二创分支”现象，不等同于官方产品线。

---

## 2. 快速结论（TL;DR）

1. **OpenClaw 仍是“主干生态”**：公开仓库体量、文档完整度、发行节奏、贡献者规模明显领先。  
2. **AutoClaw 更像“轻量部署分支”**：社区项目较多，但头部仓库集中在少数作者。  
3. **KimiQClaw 公开命名弱**：在 GitHub 上几乎无同名主仓，当前不具备独立生态判断基础。  
4. **MaxClaw/QClaw 呈现“热点分叉”特征**：存在高热度子项目（尤其 QClaw 周边），但碎片化较明显。  
5. 若你做开源分享，建议采用：**“OpenClaw 主线 + 分叉生态观察”** 的研究框架，而不是把分叉名当成稳定产品线。

---

## 3. 横向对比矩阵（研究版）

| 对象 | 公开可见度 | 代表仓库（示例） | 社区热度信号 | 生态成熟度判断 | 主要风险 |
| --- | --- | --- | --- | --- | --- |
| OpenClaw（基准） | 高 | openclaw/openclaw | 313k stars、59.7k forks（抓取日） | 高（文档/发布/贡献者规模完整） | 版本迭代快，需持续跟进 |
| AutoClaw | 中 | tsingliuwin/autoclaw | 43 个相关仓，头部约 76 stars | 中（有可用项目，但头部集中） | 项目同名较多，质量参差 |
| KimiQClaw | 低 | 暂未检索到同名仓 | 0 个相关仓（GitHub 搜索） | 低（证据不足） | 容易被“概念名”误导 |
| MaxClaw | 中 | Lichas/maxclaw | 17 个相关仓，头部约 144 stars | 中（有主仓苗头，仍在扩散期） | 存在大量低活跃同名仓 |
| QClaw | 中高 | photon-hq/qclaw-wechat-client 等 | 37 个相关仓，头部 723/464 stars | 中（周边工具活跃，主线不统一） | 渠道相关合规/稳定性风险 |

---

## 4. 分对象观察

### 4.1 AutoClaw

- 关键词特征：轻量、Docker 内运行、自动化部署。
- 生态现象：同名仓较多，存在“脚手架/部署脚本/包装层”并存。
- 建议：优先关注头部仓与最近 30 天活跃度，避免直接采纳低活跃 fork。

### 4.2 KimiQClaw

- 公开检索结果：GitHub 同名仓库结果为 0。
- 判断：更可能是社区讨论中的“组合命名”或未公开项目，而非稳定公开生态。
- 建议：在文档中标注“待验证对象”，不作为主对比结论来源。

### 4.3 MaxClaw

- 代表项目显示其强调：本地优先、低内存、Go 实现等方向。
- 生态现象：有头部仓，但其余同名项目分散。
- 建议：可作为“性能/资源占用”方向的备选观察对象。

### 4.4 QClaw

- 现象：围绕 WeChat 接入、客户端、绕过限制等项目热度高。
- 判断：生态热点集中在“渠道接入层”而非统一核心 runtime。
- 建议：在企业场景要重点评估合规与接口稳定性。

---

## 5. 对你项目的可执行建议

### A. 研究目录结构（已可直接落地）

建议长期维持以下结构：

- `大厂龙虾对比/README.md`（总报告）
- `大厂龙虾对比/数据快照-YYYY-MM-DD.md`（每月快照）
- `大厂龙虾对比/评估模板.md`（统一打分标准）

### B. 评估维度（建议 10 分制）

- 开源透明度（仓库/License/Issue/PR）
- 社区活跃度（stars 增长、最近提交）
- 生产可用性（文档、部署、回滚）
- 渠道能力（Telegram/Slack/WebChat/WeChat 等）
- 安全与合规（权限、审计、数据边界）
- 成本可控性（模型与运维成本）

### C. 你仓库推荐叙事

- 主线：OpenClaw 安装与实战（稳定核心）
- 支线：AutoClaw/MaxClaw/QClaw 作为“生态分叉观察”
- 待验证：KimiQClaw（证据不足，持续跟踪）

---

## 6. 数据来源（可复查）

- OpenClaw 主仓：
  - [openclaw/openclaw](https://github.com/openclaw/openclaw)
- GitHub 搜索（仓库维度）：
  - AutoClaw：[search](https://github.com/search?q=autoclaw&type=repositories)
  - KimiQClaw：[search](https://github.com/search?q=KimiQClaw&type=repositories)
  - MaxClaw：[search](https://github.com/search?q=MaxClaw&type=repositories)
  - QClaw：[search](https://github.com/search?q=QClaw&type=repositories)

---

## 7. 结语

这份报告定位为“**开源生态研究快照**”。后续建议每月更新一次，并把变化点（新增主仓、star 变化、是否出现官方化趋势）追加到快照文件，形成连续观察序列。
