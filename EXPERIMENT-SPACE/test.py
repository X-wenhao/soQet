from datetime import datetime
import socket
import json



def collectString(sock):
    buffer = []
    while True:
        # TODO: 注释中用data=sock.recv(1024)的方法会进入死循环
        # TODO: 因此目前聊天室里一句话不能说太长了
        buffer = [sock.recv(1024), ]
        break
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
                 mime='text',
                 content='',
                 time_stamp=datetime.now().timestamp()):
        dict.__init__(self,
                      mime=mime,
                      content=content,
                      time_stamp=time_stamp)

    def __str__(self):
        rst = dict['mime']
        rst += ' @ ' + str(dict['time_stamp'])
        rst += ': ' + dict['content']
        return rst


    def encode(self, codec):
        return (json.dumps(self)).encode(codec)
