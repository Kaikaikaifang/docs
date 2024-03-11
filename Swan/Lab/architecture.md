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
1. 创建 logdir: swanlog 用于
2. init_env
3. connect(autocreate=True)
	> 连接数据库