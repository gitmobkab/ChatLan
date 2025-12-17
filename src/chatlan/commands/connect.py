import typer
from socket import gethostname
from re import fullmatch
from ..client_utils import ClientApp
from ..utils import echo,check_ip

DEFAULT_USERNAME = gethostname()

connect_app = typer.Typer()


def parse_address(address:str) -> tuple[str,int]:
    clean_address = address.strip()
    INVALID_IP_MSG :str = """
    IP part of ADDRESS is not a valid ip
        Make sure that the IP contains four numbers separated by dots (.)
        Make sure that each number of IP contains at least 1 digits and don't exceed 3 digits
    Example: 192.168.1.9:8888
    """
    
    try:
        ip, port = clean_address.split(":")
        
        if fullmatch("^([0-9]{1,3}\\.){3}[0-9]{1,3}$",ip) is None:
            echo(INVALID_IP_MSG,"error")
            raise typer.Exit(1)
        check_ip(ip)    
    except ValueError:
        echo("The <ADDRESS> argument must be in the format IP:PORT","error")
        echo("If you don't have a ChatLan Server already Running you might prefer to use 'chat init'","info")
        echo("You check the server address in the app after you run 'chat init'","info")
        raise typer.Exit(1)
    
    try:
        converted_port = int(port)
    except ValueError:
        echo(f"Unable To convert PORT expected an integer,got {port}","error")
        raise typer.Exit(1)
    
    return ip,converted_port
        

@connect_app.command()
def connect( 
         address :str = typer.Argument(None,
                                        help="The Address of the target server, must be in IP:PORT"),
         
          username :str = typer.Option(DEFAULT_USERNAME,
                                       "-u","--username",
                                       help="The username to use for the chat session")
        
        ):
    """
    Connect to a chatlan server with the given ADDRESS which must be in the format IP:PORT i.e: '192.168.1.9:8888'
    """
    ip,port = parse_address(address=address)
    
    client_app = ClientApp(ip=ip,
                           port=port,
                           client_name=username)
    client_app.run()
    