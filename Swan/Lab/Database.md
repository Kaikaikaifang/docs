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

### Same Data Type in One Array

1. 相同类型字段存储在相同数组
2. Clickhouse 通过数组函数查询
3. ***the materialized column feature***
	> 能够从数组中取出元素作为列

> We recommend adopting this schema since it provides safeguards against applications logging too many fields.

## 分区
> Since our logging pipeline generates TBs of data daily, we created the table partitioned with `toStartOfHour(dateTime).`

## 主键

1. once a table is created the primary key can not be updated
2. 各行的主键并不唯一，不同行间的主键可以相同

## Data skipping indexes

1. 目的是提高数据查询速度
	> ClickHouse query performance is directly proportional to whether it can use the primary key when evaluating the WHERE clause.
2. uses bloom filters and skip reading significant chunks of data that are guaranteed to have no match


# PostgreSQL 
>  the world’s most [popular OSS OLTP (Online transaction processing) database](https://db-engines.com/en/ranking)


# VsCode Extension
+ [SQLTools](https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools)
+ [SQLTools Clickhouse Driver](https://marketplace.visualstudio.com/items?itemName=ultram4rine.sqltools-clickhouse-driver)
+ [SQLTools PostgreSQL/Cockroach Driver](https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools-driver-pg)

# Gorm
