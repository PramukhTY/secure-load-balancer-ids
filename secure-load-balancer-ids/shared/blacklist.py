import os

# Absolute path to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BLACKLIST_FILE = os.path.join(BASE_DIR, "logs", "blacklist.txt")

def block_ip(ip):
    os.makedirs(os.path.dirname(BLACKLIST_FILE), exist_ok=True)
    with open(BLACKLIST_FILE, "a", encoding="utf-8") as f:
        f.write(ip + "\n")

def is_blocked(ip):
    if not os.path.exists(BLACKLIST_FILE):
        return False
    with open(BLACKLIST_FILE, "r", encoding="utf-8") as f:
        return ip in f.read().splitlines()
