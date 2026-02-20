import time
import os
import json

# Absolute path to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "system.log")

os.makedirs(LOG_DIR, exist_ok=True)

def log_event(event_type, message):
    entry = {
        "time": time.strftime("%H:%M:%S"),
        "type": event_type,
        "message": message
    }
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
