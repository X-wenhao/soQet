# socket

## Intro
最简单的版本，连聊天都不行  
只能把送过来的话原封不动的还回去  

#### 但是  
可以考虑把每个人read和write的socket分开，从而可以实现任意人数的通话  
（虽然比较浪费socket，但是反正我们有没有那么大的客户群体:joy::joy:

------------------------------------------------------------------

## The Message Class
算是这个文件夹里唯一的亮点吧，本体在 `./test.py` 中：  
（暂时先把API写在这里，转正了再说）
```python
class Message(dict):
    '''
    消息类 - 一个储存消息内容以及有关该消息其他内容的容器

    SUPER:
        dict类

    ARGS:
        self['name']:       发消息的人的昵称（可以作为识别id）
        self['mime']:       消息的类型：text 文字；其他再说
        self['content']:    消息内容：text utf-8
        self['time_stamp']: （float数）消息的时间戳，有总比没有好
    '''

    def __init__(self,
                 name = '',
                 mime = 'text',
                 content = '',
                 time_stamp = $当前时间):
        '''
        实例化/初始化方法

        name和content没有默认值，需要指定
        '''
        pass


    def __str__(self):
        '''
        DEBUG的时候可以直接
            >>> print(message)

        FORMAT:
            text @ 12324.2132 : smdsbz : Lorem ipsum dolor sit amet...
        '''
        pass


    def encode(self, codec):
        '''
        编码方法：
            由于python3 socket要求send()和recv()的数据格式都是byte，
            但是这里要传到前台的数据是JSON语法的字符串，所以必须要编码  
            （也就实际调用的时候省点字数求个好看吧）

        USAGE:
            client_socket.send(
                message.encode('utf-8')
            )
        '''
        pass
```

------------------


### `collectString()`方法
网上说在接收数据的时候，可以用循环的方式把byte先放到buffer里面装好，（函数体中被注释的部分），全部接受完了后再解码  
（当然可以设置timeout用非阻塞式，但我觉得一条消息也大不到哪里去。。。。）

#### 但是
由于这里的`recv()`是阻塞式的，在接收完数据后，并不会有一个标志说这一条数据已经没了，  
所以再会回到循环中，等待`recv()`中传来数据（即发生阻塞）  
