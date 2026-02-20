import socket

for _ in range(20):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(("127.0.0.1", 8000))
            s.sendall(b"FLOOD")
    except:
        pass
