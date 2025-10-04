from textual.app import App, ComposeResult, RenderResult 
from textual.widgets import Static
from rich.markdown import Markdown
from typing import Literal
from time import strftime

class Message(Static):
    
    DEFAULT_CSS="""Message {
    height: auto;
    margin: 2 0;
    border: panel $foreground;
    padding: 2;
}"""

    def __init__(self, *children: Static, name: str | None = None, id: str | None = None, classes: str | None = None, disabled: bool = False, markup: bool = True,title: str = "Title", content: str = "", mode: Literal["info","warning","alert"] | None = None) -> None:
        super().__init__(*children, name=name, id=id, classes=classes, disabled=disabled, markup=markup)
        self.title = title
        self.content = content
        self.mode = mode
    
    def on_mount(self):
        self.border_title = self.title
        self.border_subtitle = strftime("%I:%M %p")
    
    def render(self) -> RenderResult:
        if self.mode:
           self.add_class(self.mode) 
        markdown_text = Markdown(self.content)
        return markdown_text
    
class MyMessageApp(App):
    CSS_PATH="message.tcss"
    
    
    def compose(self) -> ComposeResult:
        yield Message(content="Message, `world`")
        yield Message(content="Message, `world`" ,mode="info")
        yield Message(content="Message, `world`" ,mode="warning")
        yield Message(content="Message, `world`" ,mode="alert")
        
    
if __name__=="__main__":
    app = MyMessageApp()
    app.run()