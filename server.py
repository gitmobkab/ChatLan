import socket

# HOST = socket.gethostbyname(socket.gethostname())
HOST = "127.0.0.1" # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
DEFAULT_BYTE_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    client, addr = server.accept()
    with client:
        print(f"Connected by {addr}")
        while True:
            data = client.recv(DEFAULT_BYTE_SIZE)
            if not data:
                break
            
            client.sendall(data+b" As joined the chat")