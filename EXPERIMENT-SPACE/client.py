import socket, json
from datetime import datetime

from test import *




client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 2333



client.connect((host, port))


while True:
    push_msg = Message(name='????', content=str(input('> ')))
    if push_msg['content'] == '.exit':
        break
    client.send(push_msg.encode('utf-8'))           # 直接传送序列化后的json
    # print(collectString(client))
    print(client.recv(1024).decode('utf-8'))

client.send(Message(content='.exit').encode('utf-8'))
client.close()
