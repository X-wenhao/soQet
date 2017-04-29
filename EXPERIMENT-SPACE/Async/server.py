import socket
import select




class ChatServer:

    def __init__(self, port):
        self.port = port

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(('', port))
        self.server_socket.listen(5)

        self.socket_pool = [self.server_socket]
        print("ChatServer on %s" % self.port)



    def run(self):
        while True:
            (read_list, write_list, err_list) = select.select(self.socket_pool, [], [])

            for sock in read_list:
                if sock == self.server_socket:
                    self.accept_new_connection()
                else:
                    data_str = sock.recv(8192).decode('utf-8')
                    if data_str == '':
                        host, port = sock.getpeername()
                        data_str = "Client left %s:%s" % (host, port)
                        self.broadcast_string(data_str, sock)
                        sock.close()
                        self.socket_pool.remove(sock)
                    else:
                        host, port = sock.getpeername()
                        data_str = "[%s:%s] > %s" (host, port, data_str)
                        self.broadcast_string(data_str, sock)


    def accept_new_connection(self):
        newconn, (rmthost, rmtport) = self.server_socket.accept()
        self.socket_pool.append(newconn)
        newconn.send("Welcome!".encode('utf-8'))
        self.broadcast_string(("%s:%s joined!" % rmthost, rmtport), newconn)



    def broadcast_string(self, data_str, omit_sock):
        for each_sock in self.socket_pool:
            if each_sock != self.server_socket and each_sock != omit_sock:
                each_sock.send(data_str.encode('utf-8'))



server = ChatServer(2333)
server.run()
