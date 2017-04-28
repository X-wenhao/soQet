from socketserver import BaseRequestHandler, ThreadingTCPServer


from test import collectAndParse




socket_pool = []    # socket池，用于储存广播目标地址


class EchoHandler(BaseRequestHandler):
    def handle(self):

        print('Got connection from', self.client_address)

        global socket_pool
        socket_pool.append(self.client_address)
        print(socket_pool)

        try:
            while True:
                data = collectAndParse(self.request)
                msg = data['name'] + ': ' + data['content']
                # for addr in socket_pool:
                #     self.request.sendto(msg.encode('utf-8'), addr)
                self.request.send(msg.encode('utf-8'))
        except ConnectionAbortedError:
            for i in range(len(socket_pool)):
                if socket_pool[i] == self.client_address:
                    socket_pool.pop(i)
                    break
            print(socket_pool)



if __name__ == '__main__':
    serv = ThreadingTCPServer(('', 20000), EchoHandler)
    serv.serve_forever()
