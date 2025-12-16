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
    
