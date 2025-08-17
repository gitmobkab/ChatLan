import socket

SERVER_HOST = "127.0.0.1"  # The server's hostname or IP address
SERVER_PORT = 65432  # The port used by the server
NICKNAME = "Mob (@admin)"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((SERVER_HOST, SERVER_PORT))
    msg = bytes(NICKNAME,encoding="utf-8")
    client.sendall(msg)
    data = client.recv(1024)

print(data)