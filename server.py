import socket
from rich.console import Console
import threading
from utils import *

#GUIDELINES: DATA SHOULD ALWAYS BE FORMATTED BEFORE BEEING SENT

clients = []

console = Console()
def boot_msg():
    console.rule("Chat Lan")
    console.print("[green]Server successfully started[/green]")
    console.print(f"Server Address: [blue]{HOST}:{PORT}")
    

def connection_log(client_socket: socket.socket, client_nickname: str, client_addr):
    console.print(f"[green]New Connection:[/green] {client_nickname} {client_addr}")
    console.print(f"Connections: {threading.active_count()}")
    connection_msg = format_for_send(client_nickname, "joined the chat" , role="login")
    send_data(client_socket,connection_msg)
    
def broadcast(broadcast_msg:str):
    for client in clients:
        send_data(client.socket,broadcast_msg)

def client_register(client_username,client_socket,client_addr):
    clients.append(Client(client_username,client_socket,client_addr))
    return Client(client_username,client_socket,client_addr)


def client_unregister(client_socket_to_delete: socket.socket):
    for client in clients:
        try:
            if client == client_socket_to_delete:
                clients.remove(client)
                client_socket_to_delete.close()
        except ValueError:
            print("client not found")
            console.print(clients)
            console.print(client_socket_to_delete)
        

def handle_client(client: Client):
    while True:
        try:
            msg = get_data(client.socket)
            if msg:
                console.print(msg)
                broadcast(msg)
            else:
                console.print(f"DISCONNECTION: {client}",style="dark_red")
                client_unregister(client.socket)
                break
        except socket.error as failure:
            console.print(f"A connection Error has occurred: {failure}",style="red")
            client_unregister(client.socket)
            break
        
    

HOST = socket.gethostbyname(socket.gethostname())
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
boot_msg()
while True:
    client, addr = server.accept()
    client_name = get_data(client)
    connection_log(client, client_name, addr)
    client_obj = client_register(client_name, client, addr)
    threading.Thread(target=handle_client,args=(client_obj,)).start()
      