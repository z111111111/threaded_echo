import socket
import threading

class TS(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket()
        self.sock.bind((self.host, self.port))

    def listen(self):
        print(f'Start listening {self.port}')
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            print('connected:', address)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, conn, address):
        while True:
            data = conn.recv(1024).decode()
            if data:
                print(f'Message recieved from {address}')
            if not data:
                print(f'{address} disconnected')
                break
            conn.send(data.upper().encode())
            print(f'Message echoed to {address}')

if __name__ == "__main__":
    port = input("Port: ")
    port = int(port)
    TS('',port).listen()