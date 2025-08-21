import socket
from rich.console import Console
from utils import *

console = Console()
def boot_msg():
    console.rule("Chat Lan")
    console.print("[green]Server successfully started[/green]")
    console.print(f"Server Address: [blue]{HOST}:{PORT}")
    

def connection_log(client_socket: socket.socket, client_nickname, client_addr):
    console.print("[green]New Connection:")
    client_nickname= client_nickname.decode("utf-8")
    console.print(f"[blue]{client_nickname} {client_addr}")
    connection_msg = f"{client_nickname} As joined the chat"
    echo(client_socket,connection_msg)

HOST = socket.gethostbyname(socket.gethostname())
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
boot_msg()
while True:
    client, addr = server.accept()
    with client:
        try:
            client_name = get_pure_data(client)
            connection_log(client,client_name,addr)
        except OSError as error:
            console.print(f"Client log unsuccessfull Exception: {error}")