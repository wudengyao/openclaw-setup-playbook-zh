# 01｜安装与快速上手

## 1. 前置条件

- 推荐 Node 24（官方兼容 Node 22 LTS，需 22.16+）
- 建议先确认：
  - `node --version`
  - `npm --version` 或 `pnpm --version`

> 参考：Getting Started（官方）
> https://docs.openclaw.ai/start/getting-started

---

## 2. 推荐安装方式（CLI）

### macOS / Linux

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

### Windows（推荐 WSL2）

- 官方建议优先走 WSL2（Ubuntu）
- 先安装 WSL2：`wsl --install`
- 在 WSL 内执行 Linux 安装流

> 参考：Windows（WSL2）
> https://docs.openclaw.ai/platforms/windows

---

## 3. 一键初始化（最推荐）

```bash
openclaw onboard --install-daemon
```

该向导会完成：
1. 模型与鉴权配置
2. 工作区初始化（默认 `~/.openclaw/workspace`）
3. Gateway 端口/绑定/认证设置
4. 渠道接入（Telegram、WhatsApp、Discord 等）
5. 守护进程安装（macOS launchd / Linux systemd user）
6. 健康检查
7. 推荐 skills 安装

> 参考：Onboarding Wizard
> https://docs.openclaw.ai/start/wizard

---

## 4. 验证安装是否成功

```bash
openclaw gateway status
openclaw dashboard
```

- 若仪表盘打开成功，说明 Gateway 已可用
- 默认可直接在浏览器控制台体验（无需先接入 IM 渠道）

---

## 5. 第一次发消息（CLI）

```bash
openclaw agent --message "你好，给我一个今天的工作计划"
```

或使用 Web 控制台直接发送。

---

## 6. Telegram 快速接入（示例）

1. 在 Telegram 用 `@BotFather` 创建机器人，拿到 token
2. 配置：

```json
{
  "channels": {
    "telegram": {
      "enabled": true,
      "botToken": "123:abc",
      "dmPolicy": "pairing",
      "groups": {
        "*": { "requireMention": true }
      }
    }
  }
}
```

3. 启动并配对：

```bash
openclaw gateway
openclaw pairing list telegram
openclaw pairing approve telegram <CODE>
```

> 参考：Telegram 官方文档
> https://docs.openclaw.ai/channels/telegram

---

## 7. 从源码安装（进阶开发者）

```bash
git clone https://github.com/openclaw/openclaw.git
cd openclaw
pnpm install
pnpm ui:build
pnpm build
pnpm openclaw onboard --install-daemon
```

适用于你要二次开发、打补丁或跟踪主干分支。

---

## 8. 常见问题（快速诊断）

### Q1：向导报健康检查失败
- 执行 `openclaw doctor`
- 检查本机端口占用（默认 18789）

### Q2：控制台显示未授权 / pairing required
- 重新获取 dashboard token
- 检查 `gateway.auth.mode` 与 token 是否匹配

### Q3：Windows 下不稳定
- 优先迁移到 WSL2 + systemd 路径
- 避免直接在原生 Windows 跑复杂链路

---

## 9. 下一步

继续阅读：
- [02-部署与运维（含 Docker）](02-deployment-and-ops.md)
- [04-安全与最佳实践](04-security-best-practices.md)
