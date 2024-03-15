# 技术选型
## 公有云版
1. pypi swanlab: Python
2. fontend: Vue
3. backend: 
	1. go + [clickhouse](https://clickhouse.com/) (实验数据)
	2. js + [prisma](https://www.prisma.io/) + [postgreSQL](https://www.postgresql.org/)
	3. clickhouse & postgres integration 集成
		+ [docker-compose](https://github.com/ClickHouse/examples/blob/main/docker-compose-recipes/recipes/ch-and-postgres/docker-compose.yaml)
	ClickHouse & Postgres
	+ [migrating data between clickhouse postgres](https://clickhouse.com/blog/migrating-data-between-clickhouse-postgres)
	+ [migrating-data-between-clickhouse-postgres-part-2](https://clickhouse.com/blog/migrating-data-between-clickhouse-postgres-part-2)
	![[clickhouse&postgres.png]]
	
# 入口函数
对于架构的分析从两个入口函数展开
1. cli: swanlab watch
2. sdk: swanlab.init
# watch
> 启动应用进程
1. import swanlog
	> 导入日志记录模块
2. import app
	> 导入实例化应用服务
	+ init_env 
		> 初始化环境变量
	+ log.register
		> 初始化日志记录模块
3. uvicorn.run(app, ...)
	> 启动 uvicorn 服务器来运行 app 应用 (fastapi)
	
# init
> 初始化 swanlab 运行时实例
1. 创建 logdir: swanlog 
	用于保存：
	+ 数据库：runs.swanlab
	+ 实验数据：run_id
2. init_env
3. connect(autocreate=True)
	1. 初始化数据库实例
		> 若 runs.swanlab 不存在，创建 Sqlite database
		> 使用 [peewee](https://docs.peewee-orm.com/en/latest/) 来操作表，各方法具体细节：
		+ .connect
		> 若 runs.swanlab 不存在，创建 runs.swanlab 空文件
		+ .bind(table)
		+ .create_tables(tables)
		> peewee 的此方法通过 CREATE TABLE IF NOT EXISTS 语句实现，仅在表不存在时创建表
		+ .close
	1. 数据表的旧兼容操作（新增字段）
		> 借助 playhouse(peewee extension) 实现数据表字段的增加
4. 
	
	