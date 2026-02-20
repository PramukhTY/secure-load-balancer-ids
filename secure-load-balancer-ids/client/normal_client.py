import socket

LB_HOST = '127.0.0.1'
LB_PORT = 8000

import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 8000))
    s.sendall(b"Normal Request")
    print(s.recv(1024).decode())
