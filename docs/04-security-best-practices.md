# 04｜安全与最佳实践

## 1. 基础安全原则

1. 默认不公网暴露 Gateway
2. 启用 token/password 认证
3. 渠道访问采用 allowlist 或 pairing
4. 高风险动作加人工审批
5. 定期更新 OpenClaw 与依赖

---

## 2. 渠道安全建议（以 Telegram 为例）

- `dmPolicy` 推荐：
  - 个人：`allowlist`
  - 试运行：`pairing`
- 群组建议开启 mention gating（`requireMention: true`）
- 不要把 bot token 写死在公开仓库

---

## 3. Sandbox 建议

- 对非主会话启用 sandbox（`mode: non-main`）
- 网络默认 `none`，只按需放开
- 对工具白名单控制，最小化开放范围

---

## 4. 生产运维建议

- 监控：`/healthz` + `/readyz`
- 备份：配置、会话、workspace
- 日志保留与轮转：避免磁盘打满
- 发布策略：先灰度再全量

---

## 5. 版本升级建议

- 关注官方 release notes
- 先在测试环境跑 `openclaw doctor`
- 对关键场景做回归（消息收发、任务执行、渠道连接）

---

## 6. 一份简化“上线前检查表”

- [ ] Gateway 认证已开启
- [ ] 渠道访问控制已配置
- [ ] 敏感操作有人工确认
- [ ] 备份策略已验证可恢复
- [ ] 告警通道可达
- [ ] 文档已更新到当前版本

---

## 7. 参考链接

- 安全文档：https://docs.openclaw.ai/gateway/security
- 配置参考：https://docs.openclaw.ai/gateway/configuration
- 排障文档：https://docs.openclaw.ai/channels/troubleshooting
