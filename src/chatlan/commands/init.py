import typer
import socket
from ..server_utils import ServerApp
from ..utils import check_ip

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
    """
    Initialize a chatlan server at the host ip address (most users don't need to use any of the options)
    """
    check_ip(IP_ADDRESS)
    
    server_app = ServerApp(
                           server_ip=IP_ADDRESS,
                           server_port=port)
    server_app.run()