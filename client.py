import socket
from threading import Thread

sock = socket.socket()
sock.connect(('127.0.0.1', 10235))
def recv():
    while True:
        data = sock.recv(1024).decode()
        if not data: break
        print("Received:"+data)
def send():
    while True:
        sock.send(input().encode())

Thread(target=recv).start()
Thread(target=send).start()
