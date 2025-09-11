import socket
import argparse
import random
from rich.text import Text
from rich.rule import Rule
from rich.console import Console
from rich.layout import Layout
from utils import *

console= Console()

#PARSING
command_parser = argparse.ArgumentParser(
    prog="Client",
    description="A command to connect to a server on socket",
)

command_parser.add_argument(
    "address",
    help="Specify the server address in the 'IP:PORT' format"
)

command_parser.add_argument(
    "-n","--name",
    required=False,
    default= "User" + str(random.randint(1,455)),
    help="The Desired username for the upcoming session"
)

args = command_parser.parse_args()

if not ":" in args.address:
    console.print("[red]Error: The address must follow the 'IP:PORT' format[/red]")
    raise SystemExit(1)


ADDRESS: str = args.address
NAME: str = args.name
HOST_IP,HOST_PORT = ADDRESS.split(":")
HOST_PORT = int(HOST_PORT)
chat = []
CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def client_login(username,client_socket: socket.socket):
    username = bytes(username,encoding="utf-8")
    client_socket.sendall(username)

def format_for_print(data: str):
    if data.endswith("@new_connection"):
       return Rule(data.removesuffix(" @new_connection"),style="green")
    
    elif data.endswith("@client"):
        words = data.removesuffix(" @client").split()
        username = Text(words[0],style="blue")
        return f"[{username}]: "+ " ".join(words[1:])
    
    elif data.endswith("@disconnection"):
        return Rule(data.removesuffix(" @disconnection"),style="red")
        
        
        
        
if __name__ == "__main__":
    CLIENT.connect((HOST_IP, HOST_PORT))
    client_login(NAME,CLIENT)
    data = format_for_print(get_data(CLIENT))
    console.print(data)
    while True:
        try:
            user_prompt = console.input("[blue]Type out something:")
            msg = format_for_send(NAME,user_prompt)
            send_data(CLIENT,msg)
            try:
                data = get_data(CLIENT)
                chat.append(format_for_print(data))
                console.print(chat)
            except socket.error:
                console.rule("DISCONNECTED FROM SERVER",style="dark_red")
        except KeyboardInterrupt:
            console.print("Exiting program",style="red")
            CLIENT.close()
            break
        