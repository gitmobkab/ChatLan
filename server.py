import socket
from rich.console import Console
import threading
from utils import *

clients = []

console = Console()
def boot_msg():
    console.rule("Chat Lan")
    console.print("[green]Server successfully started[/green]")
    console.print(f"Server Address: [blue]{HOST}:{PORT}")
    

def connection_log(client_socket: socket.socket, client_nickname: str, client_addr):
    console.print("[green]New Connection:")
    console.print(f"[blue]{client_nickname} {client_addr}")
    console.print(f"Connection: {threading.active_count()}")
    connection_msg = f"{client_nickname} has joined the chat"
    echo_str(client_socket,connection_msg)
    
def broadcast(broadcast_msg:str):
    for client in clients:
        echo_str(client.socket,broadcast_msg)

def client_register(client_username,client_socket,client_addr):
    clients.append(Client(client_username,client_socket,client_addr))


def client_unregister(client_socket_to_delete):
    for client in clients:
        try:
            if client.socket.fileno() == client_socket_to_delete.fileno():
                clients.remove(client)
        except ValueError:
            print("client not found")
            console.print(clients)
            console.print(client_socket_to_delete)
        

def handle_client(client_socket: socket.socket):
    while True:
        try:
            msg = get_data(client_socket)
            if msg:
                console.print(msg)
                broadcast(msg)
            else:
                console.print(f"DISCONNECTION: {client_socket}",style="dark_red")
                client_unregister(client_socket)
                client_socket.close()
                break
        except ConnectionError as failure:
            console.print(f"A connection Error has occurred: {failure}",style="red")
        
    

HOST = socket.gethostbyname(socket.gethostname())
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
boot_msg()
while True:
    client, addr = server.accept()
    client_name = get_data(client)
    connection_log(client,client_name,addr)
    client_register(client_name,client,addr)
    threading.Thread(target=handle_client,args=(client,)).start()
      