from textual.app import App,ComposeResult
from textual.binding import Binding
from textual.widgets import Input,Header,Footer
from textual.containers import VerticalScroll
import socket
from client import *
from chat_widget import Message

    



class ClientApp(App):
    
    BINDINGS = [
        Binding("ctrl+d","toggle_dark","Toggle the app dark mode"),
        Binding("ctrl+q","close_app","Close the terminal application")
    ]
    
    def update_chat_log(self):
        while True:
            data = get_data(CLIENT)
            latest_msg = format_for_print(data)
            chat_log = self.query_one("#chat_log")
            if latest_msg == None:
                break
            pass
            self.call_from_thread(chat_log.write,latest_msg,scroll_end=True,animate=True)
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield VerticalScroll(id="chat_log")
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
    ChatLanClientApp = ClientApp()
    ChatLanClientApp.run()