# Pysockcs-simple

In netcat I can send data while receive data at the same time.

![](pysock.png)

And for python programming if you use recv() and send() in only one thread,you cannot send data until recv() is finished cause recv() block the thread.

```python
import socket
sock = socket.socket()
sock.bind(('127.0.0.1', 10235))
sock.listen(1)

conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = conn.recv(1024)
    print(data)
    if not data:
        break
    conn.send(bytes.fromhex(input()))

conn.close()

```



Now I make a simplest python socket implemention to behave like netcat with send and recv socket data at the same time (Just to make send and recv in seperate thread)

![](pysock2.png)

