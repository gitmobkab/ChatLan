from textual.app import App,ComposeResult
from textual.binding import Binding
from textual.widgets import RichLog,Input,Header,Footer
import socket
from rich.rule import Rule
from client import *

    



class ClientApp(App):
    
    BINDINGS = [
        Binding("ctrl+d","toggle_dark","Toggle the app dark mode")
    ]
    
    def update_chat_log(self):
        chat_log = self.query_one(RichLog)
        while True:
            try:
                data = get_data(CLIENT)
                latest_msg = format_for_print(data)
                self.call_from_thread(chat_log.write,latest_msg,scroll_end=True,animate=True)
            except socket.error:
                chat_log.write(Rule("DISCONNECTED FROM SERVER", style="dark_red"))
                break
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield RichLog()
        yield Input(placeholder="Type out something...",validate_on=["submitted"])
        yield Footer()
        self.run_worker(self.update_chat_log,thread=True)
        
    def action_toggle_dark(self) -> None:
        return super().action_toggle_dark()
    
    
    
    
        
    
if __name__ == "__main__":
    CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    CLIENT.connect((HOST_IP,HOST_PORT))
    client_login(NAME,CLIENT)
    data = format_for_print(get_data(CLIENT))
    ChatLanClientApp = ClientApp()
    ChatLanClientApp.run()