import socket,selectors

from textual.app import App,ComposeResult
from textual.widgets import Header,Footer,DataTable,RichLog
from textual.containers import HorizontalGroup

class ServerUi(App):
    
    AUTO_FOCUS = "RichLog"
    
    CSS = """
        DataTable{
            width: 30%;
        }
    """
    
    
    def __init__(   self,
                    server_socket: socket.socket,
                    driver_class = None,
                    css_path = None,
                    watch_css = True,
                    ansi_color = False
                 ):
        super().__init__(driver_class, css_path, watch_css, ansi_color)
        
        self.server_socket = server_socket
        self.selector: selectors.BaseSelector = selectors.DefaultSelector()    
        self.clients: ClientStack = ClientStack()
    
    def compose(self) -> ComposeResult:
        yield Header()
        with HorizontalGroup():
            yield DataTable(fixed_columns=2,fixed_rows=1)
            yield RichLog()
        yield Footer()
        
        
       
    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns("username","address")
        table.add_row("mob","127.0.0.1")    
        
        
class Client():
    def __init__(
                    self,
                    socket: socket.socket,
                    username: str,
                    address: str  
                ):
        self.socket = socket
        self.username = username
        self.address = address
        
    def __repr__(self) -> str:
        return f"{self.username}/{self.address}"
    
    def __str__(self) -> str:
        return f"{self.username}/{self.address}"
    
    def __eq__(self, value) -> bool:
        return isinstance(value,Client) and value.socket == self.socket


class ClientStack():
    def __init__(self):
        self.__clients :list[Client] = []
        
    def push(self, client: Client) -> None:
        self.__clients.append(client)
        
    def remove(self, client_to_remove: Client) -> None:
        self.__clients.remove(client_to_remove)    
        
    def length(self) -> int:
        return len(self.__clients)
    
    def __repr__(self) -> list[Client]:
        return self.__clients
    
    def __str__(self) -> list[Client]:
        return self.__clients