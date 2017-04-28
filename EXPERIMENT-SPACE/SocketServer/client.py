from socket import socket, AF_INET, SOCK_STREAM

from test import Message, collectAndParse, collectString


user_name = str(input('Your name: '))


client = socket(AF_INET, SOCK_STREAM)


client.connect(('localhost', 20000))

while True:
    content = str(input('> '))
    data = Message(name=user_name, content=content)
    client.send(data.encode('utf-8'))
    if data['content'] == '.exit':
        break
    print(client.recv(8192).decode('utf-8'))


client.close()
