import sys
import os
import time
from collections import defaultdict
from scapy.all import sniff, IP, TCP

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from shared.blacklist import block_ip
from shared.logger import log_event

FLOOD_THRESHOLD = 10
TIME_WINDOW = 3
PORT_SCAN_THRESHOLD = 10

packet_count = defaultdict(list)
port_access = defaultdict(set)
alerted_ips = set()

def detect(packet):
    if IP in packet and TCP in packet:
        src_ip = packet[IP].src
        dst_port = packet[TCP].dport
        now = time.time()

        if src_ip in alerted_ips:
            return

        # -------- Flood Detection --------
        packet_count[src_ip].append(now)
        packet_count[src_ip] = [
            t for t in packet_count[src_ip]
            if now - t <= TIME_WINDOW
        ]

        if len(packet_count[src_ip]) > FLOOD_THRESHOLD:
            log_event("IDS", f"Flood detected from {src_ip}")
            block_ip(src_ip)
            log_event("IDS", f"IP {src_ip} added to blacklist")
            alerted_ips.add(src_ip)
            return

        # -------- Port Scan Detection --------
        port_access[src_ip].add(dst_port)
        if len(port_access[src_ip]) > PORT_SCAN_THRESHOLD:
            log_event("IDS", f"Port scan detected from {src_ip}")
            block_ip(src_ip)
            log_event("IDS", f"IP {src_ip} added to blacklist")
            alerted_ips.add(src_ip)

def start_ids():
    log_event("IDS", "IDS started")
    print("[IDS] Intrusion Detection System running...")
    sniff(prn=detect, store=False)

if __name__ == "__main__":
    start_ids()
