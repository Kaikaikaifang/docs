# Clickhouse
> ClickHouse is an open-source column-oriented OLAP (Online analytical processing) database for real-time analytical workloads.

## [Cloudflare logs management](https://blog.cloudflare.com/log-analytics-using-clickhouse/?glxid=679e7a89-33a1-41fb-a525-5d7a3e84137a&experiments=mktg-website-nav-cta-button1%3A1)

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

## ABR

> [Cloudflare's ABR Analytics](https://blog.cloudflare.com/explaining-cloudflares-abr-analytics/)

1. ⚠ 数据写入时进行采样，将数据写入具有不同采样间隔的多个表中，分别存储不同采样率的数据
2. 查询时选择最佳的采样率

## Resources

1. [vector](https://github.com/vectordotdev/vector)
2. [demo](https://github.com/cloudflare/cloudflare-blog/tree/master/2022-08-log-analytics)

## Swanlab

对于 Swanlab 而言，需要存储的数据有两大类：
+ 实验数据
+ 日志信息

### 实验数据

[Table Engine: MergeTree](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/aggregatingmergetree)

Require
1. 实验唯一 id
2. 参数名称
3. 参数类型

Example
```json
{
  "create_time": "2024-03-10T09:53:40.227712",
  "update_time": "2024-03-10T09:53:40.227712",
  "data": [
    { "index": 0, "data": 0.8470532701230307, "create_time": "2024-03-10T09:53:40.294442" },
    { "index": 1, "data": 0.45640646589227024, "create_time": "2024-03-10T09:53:40.853691" },
	{ "index": 47, "data": 0.1813315122682567, "create_time": "2024-03-10T09:54:04.612036" }
  ]
}
```

Experiments Float Data Table

| ID - 主键 | Data |
| ------- | ---- |
| 实验唯一 id |      |

### 日志信息

[Table Engine: Log](https://clickhouse.com/docs/en/engines/table-engines/log-family/log)

Requirement
1. 实验名称

Example
```bash
SwanLab INFO [2024-03-10 17:53:40,148] Run `swanlab watch` to view SwanLab Experiment Dashboard

SwanLab DEBUG [2024-03-10 17:53:40,149] Check experiment and status...

SwanLab DEBUG [2024-03-10 17:53:40,165] Namespace t created, id: 1

SwanLab DEBUG [2024-03-10 17:53:40,226] Add data, tag: t/accuracy, step: 0, data: 0.4230025085716426

SwanLab DEBUG [2024-03-10 17:53:40,242] Namespace default created, id: 3
```
# PostgreSQL 
>  the world’s most [popular OSS OLTP (Online transaction processing) database](https://db-engines.com/en/ranking)


# VsCode Extension
+ [SQLTools](https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools)
+ [SQLTools Clickhouse Driver](https://marketplace.visualstudio.com/items?itemName=ultram4rine.sqltools-clickhouse-driver)
+ [SQLTools PostgreSQL/Cockroach Driver](https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools-driver-pg)

# Gorm
