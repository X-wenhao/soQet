# soQet
Prototype of primitive chat-room, concerning socket programming.



## Tasks

### Login Module
#### Back-End
- [ ] **用户登陆<br>**
	- [ ] *注册？？*
- [ ] **账号密码在数据库中的存储**
- [ ] **用户在线状态实现方法：**<br>
	- [ ] 对其他用户（是否可以开启小窗口？离线未接收的消息）
	- [ ] 对服务器（安全考虑，禁止未注册人员登陆）

#### Front-End
- [ ] **登陆（注册）页面**<br>
	- 表单提交
- [ ] **在联系人列表中，在线状态的表示**


### Chat Module
#### Back-End
- [ ] **消息存储**
	- [ ] 离线消息
	- [ ] 历史记录最大条数控制




    
    
## References & Bibliographies
- 廖雪峰教程：
	- [TPC编程](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432004374523e495f640612f4b08975398796939ec3c000)
	- [UDP编程](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432004977916a212e2168e21449981ad65cd16e71201000)
- RTFM:
	- On Windows:<br>
		`PS $CUR_DIR> python`
	- On OS X or other \*nix systems:<br>
		`→ python3`<br>
	- And then enter:
	```python
	Python 3.6.1 ...
	......
	>>> import socket
	>>> help(socket)
	```
  
  
