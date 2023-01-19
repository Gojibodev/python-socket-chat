import socketserver
import threading

class ChatHandler(socketserver.BaseRequestHandler):
    clients = []

    def handle(self):
        self.clients.append(self.request)
        while True:
            data = self.request.recv(1024).strip()
            if not data:
                self.clients.remove(self.request)
                break
            for client in self.clients:
                client.sendall(data)

class ChatServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = "localhost", 40010

    server = ChatServer((HOST, PORT), ChatHandler)
    ip, port = server.server_address

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)

    while True:
        cmd = input()
        if cmd == 'exit':
            server.shutdown()
            break
