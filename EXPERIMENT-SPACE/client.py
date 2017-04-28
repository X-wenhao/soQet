import socket



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 2333



client.connect((host, port))


while True:
    push_msg = str(input('i_stream > '))
    if push_msg == '.exit':
        break
    client.send(push_msg.encode('utf-8'))
    print(client.recv(1024).decode('utf-8'))

client.send('.exit'.encode('utf-8'))
client.close()
