# 第4章：安全与最佳实践

## 1. 五条底线

1. 默认不公网暴露 Gateway
2. 强制认证（token/password）
3. 渠道访问最小权限（allowlist / pairing）
4. 高风险动作人工审批
5. 定期升级 + 回归测试

## 2. Telegram 安全建议

- `dmPolicy`：个人环境建议 `allowlist`
- 群组建议 `requireMention: true`
- token 不入库，使用环境变量或 secret

## 3. Sandbox 建议

- `mode: non-main` 保护非主会话
- 网络默认 `none`
- 使用工具白名单，不做全放开

## 4. 上线前检查表

- [ ] Gateway 认证已开启
- [ ] 渠道访问控制已配置
- [ ] 人工确认环节已开启
- [ ] 备份与恢复已演练
- [ ] 健康检查与告警已验证

## 5. 参考

- Security: <https://docs.openclaw.ai/gateway/security>
- Config: <https://docs.openclaw.ai/gateway/configuration>
- Troubleshooting: <https://docs.openclaw.ai/channels/troubleshooting>
