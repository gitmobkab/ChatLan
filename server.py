import socket
from rich.console import Console
import threading
from utils import *

#GUIDELINES: DATA SHOULD ALWAYS BE FORMATTED BEFORE BEEING SENT
#UNTIL A FLEXIBLE WAY TO CREATE AND MANAGE CHAT MESSAGE ROLES IS IMPLEMENTED WE WILL DO HARDCODING (GASP)


clients : list[Client] = []


console = Console()

def boot_msg():
    console.rule("Chat Lan")
    console.print("[green]Server successfully started[/green]")
    console.print(f"Server Address: [blue]{HOST}:{PORT}")
    

def connection_log(client: Client):
    console.print(f"[green]New Connection:[/green] {client}")
    console.print(f"Connections: {threading.active_count()-1}")
    console.print(clients)
    
def disconnection_log(client: Client):
    console.print(f"[red]DISCONNECTION FROM:[/red] ({client})")
    console.print(f"Connections: {threading.active_count()-2}")
    # en attendant que la classe Client_list soit créer on assume ces expressions

def broadcast(broadcast_msg:str):
    if not clients:
        return
    for client in clients:
        send_data(client.socket,broadcast_msg)

def client_register(client: Client):
    clients.append(client)


def client_unregister(client_to_delete: Client):
    try:
        clients.remove(client_to_delete)
        client_to_delete.socket.close()
    except ValueError:
        print("client not found")
        console.print(clients)
        console.print(client_to_delete)
        

def handle_client(client: Client):
    broadcast(format_for_send(client.name,"joined the chat","new_connection"))
    while True:
        try:
            msg = get_data(client.socket)
            if msg:
                console.print(msg)
                broadcast(msg)
            else:
                console.print(f"DISCONNECTION: {client}",style="dark_red")
                break
        except socket.error as failure:
            console.print(f"FORCED {client} DISCONNECTION because of Exception: {failure}",style="red")
            break
        
    client_unregister(client)
    disconnection_log(client)
    disconnection_msg = format_for_send(client.name,"left the chat","disconnection")
    broadcast(disconnection_msg)
        
    

HOST = socket.gethostbyname(socket.gethostname())
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

if __name__=="__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    boot_msg()
    while True:
        client, addr = server.accept()
        client_name = get_data(client)
        new_client = Client(client_name, client, addr)
        client_register(new_client)
        threading.Thread(target=handle_client,args=(new_client,)).start()
        connection_log(new_client)
        
        