# 第2章：部署与运维实战

> 本章路径与示例站点风格一致：`/cn/adopt/chapter2/`

## 1. Docker 是否适合你

适合：

- 想隔离运行环境
- 部署到 VPS/云主机
- 需要稳定复用部署流程

不适合：

- 只追求本地最快上手（原生安装更轻）

## 2. Docker 快速部署

在 OpenClaw 仓库根目录：

```bash
./docker-setup.sh
```

完成后访问：`http://127.0.0.1:18789/`

## 3. 使用官方预构建镜像

```bash
export OPENCLAW_IMAGE="ghcr.io/openclaw/openclaw:latest"
./docker-setup.sh
```

## 4. 运维必备命令

### 健康检查

```bash
curl -fsS http://127.0.0.1:18789/healthz
curl -fsS http://127.0.0.1:18789/readyz
```

### 获取控制台链接

```bash
docker compose run --rm openclaw-cli dashboard --no-open
```

### 设备审批

```bash
docker compose run --rm openclaw-cli devices list
docker compose run --rm openclaw-cli devices approve <requestId>
```

## 5. 生产建议

1. 持久化 `~/.openclaw` 与 `~/.openclaw/workspace`
2. 默认不开公网，开启 token/password 认证
3. 对高风险动作做人工确认
4. 建立日志轮转与备份恢复演练

## 6. 常见问题

### 容器 `unhealthy`

- 检查内存和端口占用
- 检查 `/healthz` 是否可达
- 校验 token 与认证模式

### WebChat 不通

- 核对 `gateway.bind`、`gateway.port`
- 核对 auth 配置
- 如为远程模式，检查隧道/Tailscale

### `EACCES` 权限错误

- 校正挂载目录 UID/GID（常见为 1000）

## 7. 官方参考

- Docker: <https://docs.openclaw.ai/install/docker>
- Windows/WSL2: <https://docs.openclaw.ai/platforms/windows>
- WebChat: <https://docs.openclaw.ai/web/webchat>
