# File: ndsir.py (Client receiving signals)
import socket

HOST = 'IP_OF_BADERIA'  # Same as server IP
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = s.recv(1024)
        if not data:
            break
        print(f"Received from server: {data.decode()}")
