# soQet
Prototype of primitive chat-room, concerning socket programming.

---

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
	- 表单提交（**非空检查**）
- [ ] **Toast Msg - 弹出式消息提醒**<br>
	- 可以参考[MaterializeCSS](http://materializecss.com/dialogs.html)和[Toastr](http://codeseven.github.io/toastr/)


### Chat Module
#### Back-End
- [ ] **在联系人列表中，在线状态的表示**
- [ ] **消息存储**
	- [ ] 离线消息
	- [ ] 历史记录最大条数控制
- [ ] **前后台对接**
    - 说到AJAX，我希望你们都能去看一下[上一个项目里面的搜索是如何以动态的方式展示的](https://github.com/smdsbz/NewsHorizon/blob/master/static/js/function.js#L20)，要不然我感觉可能做不完...

---

## Project Structure
### Directory Structure Overview
```
soQet/
|
|-- utils/
|   |-- __init__.py
|   |-- user/           // including database operations
|   |   |-- ???
|   |-- chat_utils/
|   |   |-- ???
|   |-- ???
|
|-- database/           // user_info, chat_msg & other cache
|   |-- chat_rooms/
|   |-- P2P_chats/
|   |-- user.db
|       |-- ID      TEXT    PRIMARY KEY     NOT NULL
|       |-- PASSWD  TEXT                    NOT NULL    // HASHed
|       |-- TITLES  TEXT
|
|-- static/
|   |-- img/
|   |-- js/
|   |   |-- front_end.js
|   |   |-- various_kinds_of_joints.js
|   |-- css/
|   |-- other_essential_stuffes
|
|-- templates/
|
|-- main.py
|
|-- globalvar.py
    |-- DATABASE    // database node
    |-- OTHER_GLOBAL_VARS
```

### Task Apportion
*to be filled*
*请在此处填写任务分配，将用作开发记录*


### API
（选择好自己的任务后，请 **花时间** 完善API信息）  
（可以txt写好发给我，或者有能力直接注释出PEP8文档）  
规定格式：  
（函数名统一camelCase，尽量封装完善）
```python
def functionName(user_id, user_passwd):
    '''
    这个函数是干啥的

    ARGS:
        user_id 简要阐述这个参数是啥，i.e.怎么调用
        user_passwd

    RETURN:
        若有，申明返回数据的内容及格式
    '''
    pass
```


```python
class ClassName():
    '''
    这个类是干啥的
    '''
    # 只需要写封装之后的内容

    ' ARGS '
    ...

    ' FUNCTIONS '
    # 注释格式同上
    ...
```




---


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
	```
	Python 3.6.1 ...
	......
	>>> import socket
	>>> help(socket)
	```
