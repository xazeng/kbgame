这是一个KBEngine服务端资产库
========

##启动服务端

使用固定参数来启动：(参数的意义:http://www.kbengine.org/cn/docs/startup_shutdown.html)
	
	Linux:
		start_server.sh

	Windows:
		start_server.bat


##关闭服务端

快速杀死服务端进程:

	Linux:
		kill_server.sh

	Windows:
		kill_server.bat


如果是正式运营环境，应该使用安全的关闭方式，这种方式能够确保数据安全的存档，安全的告诉用户下线等等。

	Linux:
		safe_kill.sh

	Windows:
		safe_kill.bat

## Q&A
========

* UID 是啥  
  用来区分服务器组

* cid 是啥  
  用来区分服务进程

* gus 是啥  
  给生成唯一id用的，详情请查看 `KBEngine.genUUID64`

* 是否可以不参与负载均衡？  
  有，详情请查看 `KBEngine.setAppFlags`

* def 文件中 Utype 是啥  
  (可选)  
  属性的自定义协议ID，如果客户端不使用kbe配套的SDK来开发，客户端需要开发跟kbe对接的协议,  
  开发者可以定义属性的ID便于识别，c++协议层使用一个uint16来描述，如果不定义ID则引擎会使用  
  自身规则所生成的协议ID, 这个ID必须所有def文件中唯一
