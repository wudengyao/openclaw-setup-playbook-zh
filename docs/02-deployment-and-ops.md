# 02｜部署与运维（含 Docker）

## 1. 何时使用 Docker

适合：
- 你希望网关与宿主机环境隔离
- 你要部署到 VPS / 云主机
- 你希望快速复制环境

不适合：
- 只想本机最快体验（CLI 原生方式更轻）

> 参考：Docker 官方文档
> https://docs.openclaw.ai/install/docker

---

## 2. Docker 前置要求

- Docker Desktop / Docker Engine
- Docker Compose v2
- 至少 2 GB RAM（构建阶段更稳）

---

## 3. Docker 快速部署（官方推荐）

在 OpenClaw 仓库根目录执行：

```bash
./docker-setup.sh
```

该脚本会自动：
- 构建或拉取镜像
- 运行 onboarding
- 启动 gateway
- 生成并写入 dashboard token

完成后访问：
- `http://127.0.0.1:18789/`

---

## 4. 使用预构建镜像（跳过本地 build）

```bash
export OPENCLAW_IMAGE="ghcr.io/openclaw/openclaw:latest"
./docker-setup.sh
```

建议镜像来源使用官方 GHCR：`ghcr.io/openclaw/openclaw`。

---

## 5. 常用运维命令

### 查看健康状态

```bash
curl -fsS http://127.0.0.1:18789/healthz
curl -fsS http://127.0.0.1:18789/readyz
```

### 获取 dashboard 链接

```bash
docker compose run --rm openclaw-cli dashboard --no-open
```

### 设备配对/审批

```bash
docker compose run --rm openclaw-cli devices list
docker compose run --rm openclaw-cli devices approve <requestId>
```

---

## 6. Docker 生产建议

1. **持久化配置与工作区**
   - 确保 `~/.openclaw`、`~/.openclaw/workspace` 已映射并备份

2. **网关绑定策略**
   - 容器环境优先 `gateway.bind=lan`
   - 本地开发可 `loopback`

3. **日志与容量管理**
   - 定期清理会话、媒体、cron 运行日志
   - 监控 `sessions.json` 和 transcript 体积

4. **安全最小化**
   - 不要默认开放公网
   - 使用 token/password 鉴权
   - 外网暴露前先做防火墙白名单

---

## 7. WSL2 部署要点（Windows）

推荐链路：
1. `wsl --install` 安装 Ubuntu
2. 启用 systemd
3. 在 WSL 内完成 OpenClaw 安装与 daemon

关键优势：
- 与 Linux 生态一致，兼容更好
- 系统服务管理更稳定

---

## 8. 排障清单

### 症状：容器频繁 unhealthy
- 先看 `/healthz` 是否通
- 检查内存是否不足
- 检查 token/认证是否错误导致业务“可活但不可用”

### 症状：CLI 能跑，WebChat 不通
- 检查 `gateway.port` / `gateway.bind`
- 检查认证模式（token/password）
- 若是远程模式，检查隧道与代理

### 症状：权限报错 EACCES
- 校正卷目录 UID/GID（容器内通常为 uid 1000）

---

## 9. 推荐部署拓扑（实战）

### 拓扑 A：本机单机（个人）
- 本机安装 + daemon
- Dashboard + Telegram
- 适合个人提效

### 拓扑 B：家用小主机/NAS
- Docker Compose 部署
- Telegram + WebChat
- 定时备份 `~/.openclaw`

### 拓扑 C：远程 VPS（进阶）
- Gateway 跑在 Linux VPS
- 本地通过安全隧道接入
- 严格鉴权 + 白名单 + 日志审计
