import asyncio
from textual.binding import Binding
from textual.app import App,ComposeResult
from textual.widgets import Header,Footer,DataTable,RichLog,Input
from textual.containers import HorizontalGroup,VerticalGroup
from contextlib import suppress
from .utils import format_msg,unformat_msg



class ServerApp(App):
    
    AUTO_FOCUS = "RichLog"
    
    CSS = """
        DataTable{
            width: 30%;
        }
    """
    
    
    BINDINGS = [
        Binding("ctrl+d","toggle_dark","Toggle the app dark mode"),
        Binding("ctrl+q","close_app","Close the terminal application")
    ]
    
    def __init__(   self,
                    server_ip: str,
                    server_port: int,
                    server_username: str,
                    driver_class = None,
                    css_path = None,
                    watch_css = True,
                    ansi_color = False
                 ):
        super().__init__(driver_class, css_path, watch_css, ansi_color)
        self._clients: list[asyncio.StreamWriter] = list() 
        self._server_task: asyncio.Task | None = None
        self._server: asyncio.Server | None = None
        self.server_ip = server_ip
        self.server_port = server_port
        self.server_username = server_username
        
    
    def compose(self) -> ComposeResult:
        yield Header()
        with HorizontalGroup():
            yield DataTable(fixed_columns=2,fixed_rows=1)
            with VerticalGroup():
                yield RichLog()
                yield Input(placeholder="Type out something...")
        yield Footer()
       
    
    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns("username","address")
        table.add_row(f"{self.server_username} (you)",self.server_ip) 
        
    def on_ready(self) -> None:
        asyncio.create_task(self.start_server())
        self.notify("[b]Welcome To ChatLan Server !")
        
        
        chat_view = self.query_one(RichLog)
        chat_view.write(f"[-] Server started at '{self.server_ip}:{self.server_port}'")
    
    def on_input_submitted(self):
        input_widget = self.query_one(Input)
        text = input_widget.value
        if text:
            msg = f"{self.server_username}(server admin): {text}"
            asyncio.create_task(self.broadcast(msg))
            input_widget.clear()
    
    async def start_server(self):
        self._server = await asyncio.start_server(self.handle_new_user,
                                                 self.server_ip,
                                                 self.server_port)
        
        self._server_task = asyncio.create_task(self._server.serve_forever())
        self.notify("READY TO SCREAM",title="Server Started Successfully")
     
    def action_toggle_dark(self) -> None:
        return super().action_toggle_dark()
    
    async def handle_new_user(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        peer = writer.get_extra_info("peername")
        username_msg = await reader.readline() # b"Mobsy\n" for example
        username = unformat_msg(username_msg) # "Mobsy" as the username
        
        # QUERIES
        chat_view = self.query_one(RichLog)
        table = self.query_one(DataTable)
        table.add_row(username,peer[0],key=username)
        
        
        chat_view.write(f"[+] New connection: {username}")        
        await self.broadcast(f"{username} joined the chat")
        self._clients.append(writer)

        try:
            while True:
                data = await reader.readline()
                if not data:
                    break
                # echo and broadcast
                await self.broadcast(data)
        except Exception as exc:
            chat_view.write(f"[!] Client handler error: {exc}")
        finally:
            self._clients.remove(writer)
            with suppress(Exception):
                writer.close()
                await writer.wait_closed()
            chat_view.write(f"[-] Disconnected: {username}")
            await self.broadcast(f"{username} left the chat")
            table.remove_row(username)
            
    
    async def broadcast(self, message: bytes | str) -> None:
        """A function to broadcast a given message
    
        This function encrypt the message to be compatible with `reader.readline()` so you don't need to add `\\n` yourself
        
        Also it will log the message content inside of the first RichLog is found
        """
        chat_log = self.query_one(RichLog)
        if type(message) is bytes:
            chat_log.write(unformat_msg(message)) # quickly display the message 
        else:
            chat_log.write(message)
        message = format_msg(message) # format the message for broadcasting
        
        for writer in self._clients:
            try:
                writer.write(message)
            except Exception:
                # skip broken writers (they'll be cleaned up elsewhere)
                continue

        # gather drains; return_exceptions to avoid one slow client canceling broadcast
        if self._clients:
            await asyncio.gather(*(w.drain() for w in self._clients), return_exceptions=True)
            
    async def stop_server(self):
        # cancel _server serve_forever task
        if self._server_task:
            self._server_task.cancel()
            with suppress(asyncio.CancelledError):
                await self._server_task

        if self._server:
            self._server.close()
            await self._server.wait_closed()

        # close all client writers
        
        for writer in self._clients:
            with suppress(Exception):
                writer.close()
                await writer.wait_closed()
        self._clients.clear()
        
    def action_close_app(self):
        if self._server is not None:
            asyncio.create_task(self.stop_server())
        return super().action_quit()
        