import socket

HOST = '127.0.0.1'
PORT = 50007

content = input("input => ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(bytes(content.encode()))
    data = s.recv(1024)
    print(repr(data))

