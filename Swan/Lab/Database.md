# Clickhouse
> ClickHouse is an open-source column-oriented OLAP (Online analytical processing) database for real-time analytical workloads.

[Cloudflare logs management](https://blog.cloudflare.com/log-analytics-using-clickhouse/?glxid=679e7a89-33a1-41fb-a525-5d7a3e84137a&experiments=mktg-website-nav-cta-button1%3A1)
> We decided to keep default LZ4 compression for all columns. We used special encodings like Double-Delta for the DateTime columns, Gorilla for Float columns and LowCardinality for fixed-size String columns.
![[pipeline.png]]
## 日志存储模式
### Strict Table Schema

1. 需指定列名和数据类型
2. 包括其它字段的日志行将被删除

> 已知全部字段时采用 💐

### Dynamical Json 

1. 插入 Json Object
2. Clickhouse 动态添加适当类型的新列

> This schema should only be used if you have good control over the log schema and the number of total fields is less than 1,000.

### 
# PostgreSQL 
>  the world’s most [popular OSS OLTP (Online transaction processing) database](https://db-engines.com/en/ranking)


# VsCode Extension
+ [SQLTools](https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools)
+ [SQLTools Clickhouse Driver](https://marketplace.visualstudio.com/items?itemName=ultram4rine.sqltools-clickhouse-driver)
+ [SQLTools PostgreSQL/Cockroach Driver](https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools-driver-pg)

# Gorm
