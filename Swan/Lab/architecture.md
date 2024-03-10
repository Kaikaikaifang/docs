对于架构的分析从两个入口函数展开
1. cli: swanlab watch
2. sdk: swanlab.init
# watch
1. import swanlog
	> 导入日志记录模块
2. import app
	> 导入实例化应用服务
	+ init_env 
		> 初始化环境变量
	+ log.register
		> 初始化日志记录模块
3. uvicorn.run(app, ...)
	> 
	
	
	
