# File: baderia.py (Server in Indore)
import socket

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 65432       # Port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server running on {HOST}:{PORT}...")
    
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            data = conn.recv(1024)
            if not data:
                break
            # Broadcast to all clients (e.g., ndsir)
            print(f"Received from animesh: {data.decode()}")
            # Forward to ndsir (you'd need a list of connected clients)
            # conn.sendall(b"Signal forwarded to ndsir!")
