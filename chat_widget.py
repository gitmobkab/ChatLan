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
    width: 75vw;
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
    

class Alert(Static):

    DEFAULT_CSS="""Alert{
    height: auto;
    margin: 2 40;
    border: outer $foreground;
    padding: 2;
    width: 50vw;
    text-align: center;
    content-align: center middle;
}"""

    def __init__(self, content = "", *, expand = False, shrink = False, markup = True, name = None, id = None, classes = None, disabled = False,
                 type: Literal["new_connection","disconnection"] | None = None):
        super().__init__(content, expand=expand, shrink=shrink, markup=markup, name=name, id=id, classes=classes, disabled=disabled)
        self.type = type
        
    def on_mount(self): 
        self.border_subtitle = strftime("[ %I:%M ]")
    
    def render(self) -> RenderResult:
        if self.type:
            self.add_class(self.type)
        markdown_text = Markdown(self.content)
        return markdown_text
    
class MyMessageApp(App):
    CSS_PATH="chatlan.tcss"
    
    
    def compose(self) -> ComposeResult:
        yield Message(content="Message, `world`")
        yield Message(content="Message, `world`" ,mode="info")
        yield Message(content="Message, `world`" ,mode="warning")
        yield Message(content="Message, `world`" ,mode="alert")
        yield Alert(content="Hello *friend*")
        yield Alert(content="Heelo *Boys*", type="new_connection")
        yield Alert(content="HELLO `GIRLS`", type="disconnection")
        
        
    
if __name__=="__main__":
    app = MyMessageApp()
    app.run()
