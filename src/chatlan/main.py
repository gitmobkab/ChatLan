from typer import Typer
from .commands import init,connect

chat_command = Typer(no_args_is_help=True,help="A command line tool to chat with friends")
chat_command.add_typer(init)
chat_command.add_typer(connect)