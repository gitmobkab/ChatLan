from typer import Typer,Option,Argument
from socket import gethostbyname,gethostname
from ..server_utils import ServerApp
from ..utils import check_ip

init_app = Typer()
DEFAULT_USERNAME = gethostname() 
DEFAULT_IP_ADDRESS = gethostbyname(DEFAULT_USERNAME)

@init_app.command()
def init( ip: str = Argument(DEFAULT_IP_ADDRESS,
                             help="The ip that the server should use (only meant for advanced configuration)"), 
         
          port: int = Option(8888,
                                   "-p","--port",
                                   min=8000,
                                   max=9000,
                                   help="The port to use for the server"), 
          
          username: str = Option(DEFAULT_USERNAME,
                                 "-u","--username",
                                 help="The username to use for this session")
        ): 
    """
    Initialize a chatlan server at the host ip address (most users don't need to use any of the options)
    """
    check_ip(DEFAULT_IP_ADDRESS)
    
    server_app = ServerApp(
                           server_ip=ip,
                           server_port=port,
                           server_username=username)
    server_app.run()