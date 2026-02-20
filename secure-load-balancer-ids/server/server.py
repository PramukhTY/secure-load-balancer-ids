import socket
import sys

HOST = "127.0.0.1"
PORT = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen()

print(f"[SERVER {PORT}] Running")

while True:
    conn, addr = s.accept()
    data = conn.recv(1024).decode()
    conn.sendall(f"Response from Server {PORT}".encode())
    conn.close()
