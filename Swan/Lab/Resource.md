# Raspi
JCHY_5G 192.168.31.208
Geektech 172.16.38.217
> Notice: 172.16.39.68 位于 GeekTech 局域网下，访问以下资源时需连接 GeekTech WiFI ⚠
# Dell 开发机

JCHY 192.168.31.242

| IP       | 172.16.39.86   |     |
| -------- | -------------- | --- |
| User     | kakai          |     |
| Password | 1030jkf@kaikai |     |
> Notice: it's kakai, not kaikai! 🃏
# Clickhouse

| Server   | 172.16.39.79         |
| -------- | -------------------- |
| Port     | 8123(http) 9000(tcp) |
| Database | swanlab_dev          |
| User     | swan                 |
| Password | 1030jkf@kaikai       |
|          |                      |

```go
package main

import (
    "gorm.io/driver/clickhouse"
    "gorm.io/gorm"
)

func main() {
    click_dsn := "clickhouse://swan:1030jkf@localhost:9000/swanlab_dev?dial_timeout=10s&read_timeout=20s"
    _, err2 := gorm.Open(clickhouse.Open(click_dsn), &gorm.Config{})
    if err2 != nil {
        panic("failed to connect clickhouse")
    }
}
```
# Postgres

| Server   | 172.16.39.79   |
| -------- | -------------- |
| Port     | 5432           |
| Database | swanlab_dev    |
| User     | swan           |
| Password | 1030jkf@kaikai |
```go
package main

import (
    "gorm.io/driver/postgres"
    "gorm.io/gorm"
)

func main() {
    post_dsn := "host=localhost user=swan password=1030jkf@kaikai dbname=swanlab_dev port=5432 sslmode=disable TimeZone=Asia/Shanghai"
    _, err1 := gorm.Open(postgres.Open(post_dsn), &gorm.Config{})
    if err1 != nil {
        panic("failed to connect postgres")
    }
}
```