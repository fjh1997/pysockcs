import socket
from threading import Thread

sock = socket.socket()
sock.bind(('127.0.0.1', 10235))
sock.listen(1)
conn, addr = sock.accept()
print('connected:', addr)

def recv():
    while True:
        data = conn.recv(1024).decode()
        if not data: break
        print("Received:"+data)
def send():
    while True:
        conn.send(input().encode())

Thread(target=recv).start()
Thread(target=send).start()

