import socket
import time

ports = [8000, 9001, 9002, 9003, 22, 80, 443, 3306, 8080]

for p in ports:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect(("127.0.0.1", p))
    except:
        pass
    time.sleep(0.2)
