import socket
import sys
import os
import time
from collections import defaultdict

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from shared.blacklist import is_blocked, block_ip
from shared.logger import log_event

LB_HOST = "127.0.0.1"
LB_PORT = 8000

SERVERS = [
    ("127.0.0.1", 9001),
    ("127.0.0.1", 9002),
    ("127.0.0.1", 9003),
]

# ---------- Flood Detection Config ----------
FLOOD_LIMIT = 10        # max requests
TIME_WINDOW = 3         # seconds
request_tracker = defaultdict(list)

current = 0

def get_next_server():
    global current
    server = SERVERS[current]
    current = (current + 1) % len(SERVERS)
    return server

lb = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lb.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
lb.bind((LB_HOST, LB_PORT))
lb.listen()

log_event("LB", "Load Balancer started")
print("[LB] Running")

while True:
    conn, addr = lb.accept()
    ip = addr[0]
    now = time.time()

    # ---------- Check Blacklist ----------
    if is_blocked(ip):
        log_event("LB", f"Blocked connection from {ip}")
        conn.close()
        continue

    # ---------- Flood Detection ----------
    request_tracker[ip].append(now)
    request_tracker[ip] = [
        t for t in request_tracker[ip] if now - t <= TIME_WINDOW
    ]

    if len(request_tracker[ip]) > FLOOD_LIMIT:
        log_event("IDS", f"Flood detected from {ip} at Load Balancer")
        block_ip(ip)
        log_event("IDS", f"IP {ip} added to blacklist")
        conn.close()
        continue

    # ---------- Normal Request Handling ----------
    try:
        message = conn.recv(1024).decode()
        server = get_next_server()

        log_event("LB", f"Forwarded request from {ip} to server {server}")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(server)
            s.sendall(message.encode())
            response = s.recv(1024)

        conn.sendall(response)

    except Exception as e:
        log_event("LB", f"Error handling request from {ip}: {e}")

    finally:
        conn.close()
