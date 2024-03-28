# 环境搭建

> 使用 `gvm` 进行 `go` 的版本管理

1. 安装 gvm
2. 下载目标[版本](https://go.dev/dl/)
3. 放到 ~/.gvm/archive/
4. gvm install go1.?.? -B
5. gvm use --default go1.?.?

# 依赖包

```bash
go mod init  # 初始化go.mod
go mod tidy  # 更新依赖文件
go mod download  # 下载依赖文件
go mod vendor  # 将依赖转移至本地的vendor文件
go mod edit  # 手动修改依赖文件
go mod graph  # 打印依赖图
go mod verify  # 校验依赖
```

## 初始化项目

1. `go mod download`
## 初始化空白项目
