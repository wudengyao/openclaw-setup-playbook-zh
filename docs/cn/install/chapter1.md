# 第1章：安装与初始化

## 1. 前置要求

- 推荐 Node 24（兼容 Node 22 LTS，需 22.16+）
- 确保可用命令：`node`、`npm`（或 `pnpm`）

## 2. 推荐安装

=== "macOS / Linux"

    ```bash
    curl -fsSL https://openclaw.ai/install.sh | bash
    ```

=== "Windows（推荐 WSL2）"

    1. `wsl --install`
    2. 进入 Ubuntu
    3. 按 Linux 流程安装 OpenClaw

## 3. 初始化向导

```bash
openclaw onboard --install-daemon
```

向导将完成模型授权、工作区初始化、Gateway 配置、可选渠道接入和健康检查。

## 4. 验证

```bash
openclaw gateway status
openclaw dashboard
```

## 5. Telegram 接入（最简）

1. BotFather 创建 bot 获取 token
2. 配置 `channels.telegram.botToken`
3. 执行配对审批：

```bash
openclaw pairing list telegram
openclaw pairing approve telegram <CODE>
```

## 6. 参考

- Getting Started: <https://docs.openclaw.ai/start/getting-started>
- Onboarding Wizard: <https://docs.openclaw.ai/start/wizard>
- Telegram: <https://docs.openclaw.ai/channels/telegram>
