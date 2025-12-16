from rich import print as rprint
from typing import Literal

def echo(message:str,mode: Literal["info","success","warning","error"]):
    prefixs = {
        "info": "[blue]::INFO::[/blue]",
        "success": "[green]::SUCCESS::[/green]",
        "warning":"[orange]::WARNING::[/orange]",
        "error":"[red]::ERROR::[/red]"
    }
    
    prefix = prefixs[mode]
    rprint(f"{prefix} [bold]{message}")
    
def format_msg(message: str | bytes) -> bytes:
    """
    Take a message either in a string or a bytes
    
    always add the `\\n` character to the end of the message
    
    and return it as a bytes
    
    ie:
        - format_msg("Mob Joined the Chat") -> b"Mob Joined The Chat \\n"
        - format_msg(b"Mob Joined the Chat") -> b"Mob Joined The Chat \\n"
        - format_msg("Mob \\nJoined the Chat") -> b"Mob \\nJoined The Chat \\n"
    """
    if type(message) is str:
        formatted_msg = message + "\n"
        formatted_msg = formatted_msg.encode()
        return formatted_msg
    
    if type(message) is bytes:
        return message + b"\n"
    
    return b""