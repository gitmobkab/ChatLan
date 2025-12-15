import typer
from ..utils import ServerUi
import socket

init_app = typer.Typer()
IP_ADDRESS = socket.gethostbyname(socket.gethostname())


@init_app.command()
def init( 
          port: int = typer.Option(8888,
                                   "-p","--port",
                                   min=8000,
                                   max=9000,
                                   help="The port to use for the server")  
        
        ): 

    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind((IP_ADDRESS,port))
    server_socket.listen()
    server_socket.setblocking(False)
    
    server_app = ServerUi(server_socket=server_socket)
    server_app.run()