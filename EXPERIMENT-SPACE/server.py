import socket, threading, time
import json

from test import *



##########################################


def chatting(sock, addr):
    print("Accepted client: %s:%s" % addr)
    while True:
        data = collectAndParse(sock)
        print(data)
        if data['content'] == '.exit':
            break
        else:
            sock.send(("{}: {}".format(data['name'],
                                       data['content'])).encode('utf-8'))
    sock.close()
    print("session closed")


#################################################

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = socket.gethostname()
port = 2333


server.bind((host, port))


server.listen(3)


while True:
    client, addr = server.accept()

    client_thread = threading.Thread(target=chatting, args=(client, addr))
    client_thread.start()

    client_thread.join()
    break
