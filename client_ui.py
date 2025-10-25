from textual.app import App,ComposeResult
from textual.binding import Binding
from textual.widgets import RichLog,Input,Header,Footer
import socket
from rich.rule import Rule
from client import *

    



class ClientApp(App):
    
    BINDINGS = [
        Binding("ctrl+d","toggle_dark","Toggle the app dark mode"),
        Binding("ctrl+q","close_app","Close the terminal application")
    ]
    
    def update_chat_log(self):
        while True:
            data = get_data(CLIENT)
            latest_msg = format_for_print(data)
            chat_log = self.query_one(RichLog)
            if latest_msg == None:
                chat_log.write(Rule("DISCONNECTED FROM SERVER", style="dark_red"))
                break
            self.call_from_thread(chat_log.write,latest_msg,scroll_end=True,animate=True)
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield RichLog()
        yield Input(placeholder="Type out something...",validate_on=["submitted"])
        yield Footer()
        self.run_worker(self.update_chat_log,thread=True)
        
    def action_toggle_dark(self) -> None:
        return super().action_toggle_dark()
    
    def action_close_app(self):
        send_data(CLIENT)
        CLIENT.close()
        return self.action_quit()
    
    
    def on_input_submitted(self):
        input_widget = self.query_one(Input)
        if input_widget.value == "!quit":
            send_data(CLIENT)
            CLIENT.close()
            return self.action_quit()
        data_to_sent = format_for_send(NAME,input_widget.value)
        send_data(CLIENT,data_to_sent)
        input_widget.clear()
    
    
    
        
    
if __name__ == "__main__":
    CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    CLIENT.connect((HOST_IP,HOST_PORT))
    client_login(NAME,CLIENT)
    data = format_for_print(get_data(CLIENT))
    ChatLanClientApp = ClientApp()
    ChatLanClientApp.run()