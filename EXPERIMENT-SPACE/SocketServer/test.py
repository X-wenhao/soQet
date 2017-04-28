from datetime import datetime
import socket
import json
import time



def collectString(sock):
    buffer = []
    while True:
        # TODO: 注释中采用阻塞法，接收端无法判断接收是否结束，会卡住
        # TODO: 因此目前聊天室里一句话不能说太长了
        buffer = [sock.recv(8192), ]
        break
        # sock.setblocking(0)
        # data = sock.recv(1024)
        # if data:
        #     buffer.append(data)
        # else:
        #     break
    data = b''.join(buffer)
    data = data.decode('utf-8')     # utf-8 string
    return data


def collectAndParse(sock):
    data = collectString(sock)
    return json.loads(data)      # dict





class Message(dict):
    '''
    消息类

    ARGS:
        dict['mime']:       消息类型        # 暂时只支持text文本类型
        dict['content']:    消息内容
        dict['time_stamp']: 时间戳

    FUNCS:
        继承dict类，该怎么用怎么用
        ps 支持json.dumps()方法，将通过json在client和server之间传送数据
    '''
    def __init__(self,
                 name='',
                 mime='text',
                 content='',
                 time_stamp=datetime.now().timestamp()):
        dict.__init__(self,
                      name=name,
                      mime=mime,
                      content=content,
                      time_stamp=time_stamp)

    def __str__(self):
        return (
            self['mime'] + ' @ ' + str(self['time_stamp']) + ' : ' +
            self['name'] + ' : ' + self['content']
        )


    def encode(self, codec):
        return (json.dumps(self)).encode(codec)
