import socket
from rich.console import Console

console = Console()
def boot_msg():
    console.rule("Chat Lan")
    console.print("[green]Server successfully started[/green]")
    console.print(f"Server Address: [blue]{HOST}:{PORT}")
    
def echo(client_socket: socket.socket , msg: str = ""):
    encoded_msg = bytes(msg,encoding="utf-8")
    client_socket.sendall(encoded_msg)
    
def connection_log(client_socket: socket.socket, client_nickname, client_addr):
    console.print("[green]New Connection:")
    console.print(f"[blue]{client_nickname} {addr}")
    client.sendall(client_nickname+b" As joined the chat")

HOST = socket.gethostbyname(socket.gethostname())
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
DEFAULT_BYTE_SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
boot_msg()
while True:
    client, addr = server.accept()
    with client:
        client_name = client.recv(DEFAULT_BYTE_SIZE)
        connection_log(client,client_name,addr)