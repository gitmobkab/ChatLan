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

def unformat_msg(message: str | bytes) -> str:
    """
    Should be called after `reader.readline()`
    
    take a bytes object and return a string without the last char
    
    basically this is supposed to remove the `\\n` char after `reader.readline()`
    
    but keep in mind that this only remove the last char
    
    i.e:
        - unformat_msg(b"Mobsy\\n") -> "Mobsy"
        - unformat_msg(b"Mobsy") -> "Mobs"
    """
    if type(message) is bytes:
        unformatted_msg = message.decode()
        return unformatted_msg[:-1]
    elif type(message) is str:
        return message[:-1]
    
    return ""