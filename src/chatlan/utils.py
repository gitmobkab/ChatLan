from rich import print as rprint
from typing import Literal
from re import fullmatch
from sys import exit

def echo(message:str,mode: Literal["info","success","warning","error"]):
    prefixs = {
        "info": "[blue]::INFO::[/blue]",
        "success": "[green]::SUCCESS::[/green]",
        "warning":"[orange]::WARNING::[/orange]",
        "error":"[red]::ERROR::[/red]"
    }
    
    prefix = prefixs[mode]
    rprint(f"{prefix} [bold]{message}")
    
def check_ip(ip :str) -> None:
    first_test = "^127\\.([0-9]{1,3}\\.){2}[0-9]{1,3}$"
    if fullmatch(first_test,ip) is not None or ip == "0.0.0.0":
        echo(f"Looks Like Your Os returned an invalid address, Chatlan got {ip}","error")
        echo(f"Make sure you're connected to a WLAN or LAN, wifi (recommended)","info")
        echo(f"If the issue persist, see [blue link=https://github.com] ChatLan#Troubleshooting or open an issue on the repo","info")
        raise exit(1)
    
    
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