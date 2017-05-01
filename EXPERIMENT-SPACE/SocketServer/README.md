# SocketServer



没有 `listen()`  
一个server可以通过多线程的方式处理任意个数的socket（i.e. 任意个数的聊天室/小窗口）  
此时每个socket的地位都是同等的，需要一个比较好的管理方式
