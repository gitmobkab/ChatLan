import asyncio
from textual.app import App,ComposeResult
from textual.binding import Binding
from textual.widgets import Input,Header,Footer
from textual.containers import VerticalScroll
from .utils import format_msg,unformat_msg,parse_chatlan_msg  
from .message_widget import Message


class ClientApp(App):
    
    
    BINDINGS = [
        Binding("ctrl+d","toggle_dark","Toggle the app dark mode"),
        Binding("ctrl+q","close_app","Close the terminal application")
    ]
    
    def __init__(   self,
                    ip: str,
                    port: int,
                    client_name: str,
                    driver_class = None,
                    css_path = None,
                    watch_css = True,
                    ansi_color = False
                 ):
        super().__init__(driver_class, css_path, watch_css, ansi_color)

        self.ip = ip
        self.port = port
        self.client_name = client_name
        self._reader: asyncio.StreamReader | None = None
        self._writer: asyncio.StreamWriter | None = None
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield VerticalScroll(id="chat_view")
        yield Input(placeholder="Type out something...",validate_on=["submitted"])
        yield Footer()
        
    def on_ready(self) -> None:
        asyncio.create_task(self.connect_to_server())
        self.notify("Welcome To ChatLan Client")
        
    def draw(self, title: str = "Title",value: str="", color :str = "white" ,selector: str = "#chat_view"):
        """Draw/Mount a ChatLan.Message widget on a selected widget, the widget must be mount compatible"""
        selected_widget = self.query_one(selector)
        selected_widget.anchor()
        message_widget = Message(title=title, content=value, color=color)
        selected_widget.mount(message_widget)
    
    async def connect_to_server(self):
        self._reader, self._writer = await asyncio.open_connection(self.ip,self.port) 
        await self.send_message(self.client_name)
        asyncio.create_task(self.listen_for_messages())
        self.notify("Connected to Server !")
            
    async def listen_for_messages(self):
        if self._reader is None:
            self.notify("Connection to server Failed",severity="error") # For whatever reason this is never triggered
            return                                                      # but at least it stop the type checker from complaining
        try: 
            while True:
                data = await self._reader.readline()
                if not data:
                    DISCONNECTION_MESSAGE_TITLE = "[!] Disconnected from server"
                    DISCONNECTION_MESSAGE = "It seems that you have been disconnected from the server, maybe the server is closed or maybe your network is too slow"
                    DISCONNECTION_MESSAGE_COLOR = "red"
                    self.draw(DISCONNECTION_MESSAGE_TITLE,DISCONNECTION_MESSAGE,DISCONNECTION_MESSAGE_COLOR)
                    self.notify("Disconnected from server",severity="error",timeout=10)
                    break
                msg = unformat_msg(data)
                if msg:
                    msg_content = parse_chatlan_msg(msg)
                    self.draw(*msg_content)
        except Exception as error:
            self.draw("[!] Unexpected Error occured",
                      str(error),
                      "red")
        finally:
            if self._writer:
                asyncio.create_task(self.disconnect())
        
    async def disconnect(self):
        if self._writer is not None:
            self._writer.close()
            await self._writer.wait_closed()
        self._writer = None
    
    async def send_message(self,message: str):
        if self._writer is not None:
            data = format_msg(message)
            self._writer.write(data)
            await self._writer.drain()
            return
        self.notify("Unable To send message",severity="error")    
        
    def action_toggle_dark(self) -> None:
        return super().action_toggle_dark()
    
    def action_close_app(self):
        asyncio.create_task(self.disconnect())
        return self.action_quit()
    
    
    def on_input_submitted(self):
        input_widget = self.query_one(Input)
        if input_widget.value:
            msg = f"{self.client_name}: {input_widget.value}"
            asyncio.create_task(self.send_message(msg))
            input_widget.clear()