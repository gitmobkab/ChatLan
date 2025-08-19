import socket
import argparse
import random
from rich.console import Console

console= Console()

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
    console.print("[red]Error: The address must be respect the 'IP:PORT' format[/red]")
    raise BaseException

ADDRESS: str = args.address
NAME: str = args.name

HOST_IP,HOST_PORT = ADDRESS.split(":")
HOST_PORT = int(HOST_PORT)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST_IP, HOST_PORT))
    msg = bytes(NAME,encoding="utf-8")
    client.sendall(msg)
    data = client.recv(1024)

print(data)