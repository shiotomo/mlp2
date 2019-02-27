import socket

HOST = "127.0.0.1"
PORT = 50007
LISTEN = 1

print('== socket server ==')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(LISTEN)

    while True:
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print('data:' + format(data)),
                print('addr:' + format(addr))
                conn.sendall(b'Received: ' + data)
