# File: animesh.py (Client sending signals)
import socket

HOST = input('IP_OF_BADERIA :')  # Replace with server's IP (e.g., Indore server)
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello from Animesh!")
    data = s.recv(1024)
print(f"Server replied: {data.decode()}")
