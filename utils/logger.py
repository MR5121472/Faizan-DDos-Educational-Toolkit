# utils/logger.py — Faizan™ Logging System

import os
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "attack_log.txt")

def ensure_log_dir():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

def log_attack(method, target_ip, target_port, duration, spoof=False):
    ensure_log_dir()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "Spoofed" if spoof else "Normal"
    
    log_entry = (
        f"[{now}] Method: {method} | Target: {target_ip}:{target_port} | "
        f"Duration: {duration}s | Mode: {status}\n"
    )

    with open(LOG_FILE, "a") as log_file:
        log_file.write(log_entry)
