import socket, threading, time



def chatting(sock, addr):
    print("Accepted client: %s:%s" % addr)
    while True:
        data = sock.recv(1024)
        time.sleep(1)

        if data.decode('utf-8') == '.exit':
            break
        else:
            sock.send(("client: %s" % data.decode('utf-8')).encode('utf-8'))

    sock.close()
    print("session closed")




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
