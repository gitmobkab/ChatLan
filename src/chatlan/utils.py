from rich import print as rprint
from typing import Literal
from re import fullmatch
from sys import exit
from random import choice

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
    INVALID_IP_MSG :str = """
    IP part of ADDRESS is not a valid ip
        Make sure that the IP contains four numbers separated by dots (.)
        Make sure that each number of IP contains at least 1 digits and don't exceed 3 digits
    Example: 192.168.1.9:8888
    """
    if fullmatch("^([0-9]{1,3}\\.){3}[0-9]{1,3}$",ip) is None:
            echo(INVALID_IP_MSG,"error")
            raise exit(1)
        
    invalid_ip_test = "^127\\.([0-9]{1,3}\\.){2}[0-9]{1,3}$"
    if fullmatch(invalid_ip_test,ip) is not None or ip == "0.0.0.0":
        echo(f"Looks Like Your Os returned an invalid address, Chatlan got {ip}","error")
        echo(f"Make sure you're connected to a WLAN or LAN, wifi (recommended)","info")
        echo(f"If the issue persist, see [blue link=https://github.com/gitmobkab/ChatLan/tree/rewrite#troubleshooting] ChatLan#Troubleshooting or open an issue on the repo","info")
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

def parse_chatlan_msg(message: str) -> tuple[str, str, str]:
    """
    parse message in the format **color:title:content**
    
    raise ValueError if the format is incorrect, this function never split any ":" inside of content
    
    :param message: the message to parse
    :type message: str
    :return: a tuple of three strings in the order **title, content, color**
    :rtype: tuple[str, str, str]
    """
    color, title, content = message.split(":",2) # just to raise ValueError if the string doesn't respect the format
    return (title, content, color)

def hex_color_genrator() -> str:
    """
    Return a random string representing a css hexadecimal color code string
    
    i.e: 
    
        - hex_color_generator() -> "#F45BA5"
        - hex_color_generator() -> "#5AFC09"
    
    :return: a string representing a css hexadecimal color code string 
    :rtype: str
    """
    HEX_CHARS = "ABCDEF0123456789"
    hex_color = "#"
    for i in range(6):
        hex_color += choice(HEX_CHARS)
    return hex_color

if __name__ == "__main__":
    for i in range(8):
        print(hex_color_genrator())