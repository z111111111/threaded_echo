import socket

sock = socket.socket()
try:
    sock.connect(('192.168.1.71', 1488))
    print('Connecting to server')
except:
    print('Connection failed')
a = input()
while a != 'exit':
    sock.send(a.encode())
    print('Message sent to server')
    data = sock.recv(1024)
    if data:
        print('Message recieved from server')
    print(data.decode())
    a = input()
    if a == 'exit':
        sock.close()
        print('Closing connection')

