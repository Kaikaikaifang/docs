
# pnpm
`pnpm install` GET 拉取依赖报错
```bash  WARN  GET https://registry.npmjs.org/@vitejs%2Fplugin-vue error (ETIMEDOUT). Will retry in 10 seconds. 2 retries left.
 WARN  GET https://registry.npmjs.org/autoprefixer error (ETIMEDOUT). Will retry in 10 seconds. 2 retries left.
 WARN  GET https://registry.npmjs.org/eslint error (ETIMEDOUT). Will retry in 10 seconds. 2 retries left.
```
解决方案：
```bash
sudo sysctl -w net.ipv6.conf.all.disable_ipv6=1
sudo sysctl -w net.ipv6.conf.default.disable_ipv6=1
sudo sysctl -w net.ipv6.conf.lo.disable_ipv6=1
```