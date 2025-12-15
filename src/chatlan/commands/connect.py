import typer
import socket

DEFAULT_USERNAME = socket.gethostname()

connect_app = typer.Typer()

@connect_app.command()
def connect( 
         address :str = typer.Argument(None,
                                        help="The Address of the target server, must be in IP:PORT"),
         
          username :str = typer.Option(DEFAULT_USERNAME,
                                       "-u","--username",
                                       help="The username to use for the chat session")
        
        ):
    pass