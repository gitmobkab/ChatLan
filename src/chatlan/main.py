from typer import Typer
from .commands import init,connect

chat_command = Typer(no_args_is_help=True)
chat_command.add_typer(init)
chat_command.add_typer(connect)