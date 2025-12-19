from textual.app import App, ComposeResult, RenderResult 
from textual.widget import Widget
from textual.color import Color
from re import findall
from time import strftime
from .exceptions import DangerousOperation

class Message(Widget):
    """
    The ChatLan Message widget
    
    title -> The title to use to display the widget
    
    content -> the content to display inside of the widget
    
    
    color -> an hex or color string representing the color of the border
    """
    
    DEFAULT_CSS="""
    Message {
    height: auto;
    margin: 2 0;
    color: $text;
    background: $panel;
    padding: 2;
    width: 75%;
}"""

    def __init__(self,
                 *children: Widget,
                 name: str | None = None,
                 id: str | None = None,
                 classes : str | None = None,
                 disabled: bool = False,
                 markup: bool = True,
                 title: str = "Title",
                 content: str = "",
                 color: str = "white"
                 ) -> None:
        super().__init__(*children, name=name, id=id, classes=classes,disabled=disabled,markup=markup)
        
        self.title = title
        self.content = content
        self.color: Color = Color.parse(color)
    
    def parse_content(self,content: str) -> str:
        """
        take a string and return a appropriate content_markup string (a rich contetn markup) or raise ChatLan.DangerousOperation
        
        i.e: 
            self.parse_content("\\*Mobsy\\*") -> "[b]Mobsy[/b]"
            self.parse_content("\\*Mobsy \\_Some Text\\_ \\*") -> "[b]Mobsy [u]Some Text[/u] [/b]"
            self.parse_content("the result is actually: 5*5 = 25") -> "the result is actually: 5*5 = 25"
        
        :param content: a string to evaluate as rich content markup
        :return: a string that can be evaluated a rich content markup, raise chatlan.exception.DangerousOperation on any '@','$','(',')' inside of a bracket []
        preventing use of textual advanced call within a content markup
        :rtype: str
        """
        
        
        if not content:
            return ""
        
        test_matches = findall(r"\[[^\]]*[@$()][^\]]*\]",content)
        if test_matches:
            raise DangerousOperation(f"Caught attempt/s to run arbitrary code, got {test_matches}")
                
        
        MARKUPS: dict[str,str] = {
            "*": "b",
            "/": "i",
            "`": "d",
            "~": "s",
            "_": "u",
            "^": "r"
        }
        content_markup: str = ""
        stack : list[str] = []
        
        for char in content:
            found_markup = MARKUPS.get(char)
            CLOSING_TAG = f"[/{found_markup}]"
            
            if stack and stack[-1] == char:
                stack.pop()
                content_markup += CLOSING_TAG
            elif char in MARKUPS:
                stack.append(char)
                content_markup += f"[{found_markup}]"
            elif found_markup is None:
                content_markup += char
            
        if len(stack) != 0:
            return content
        
        return content_markup
            
            
                
    def render(self) -> RenderResult:
        self.styles.auto_border_title_color = True
        self.border_title = self.title
        self.border_subtitle = strftime("%H:%M:%S -- %d %A %m %Y")
        self.styles.border = ("panel", self.color)
    
        try:
            content_markup = self.parse_content(self.content)
            return content_markup
        except DangerousOperation as error:
            self.border_title = "Maliscious code detected"
            self.styles.border = ("panel", "red")
            return f"[red bold]{error}"
            
    
    
class MyMessageApp(App):
    """
    Docstring for MyMessageApp
    """

    SOME_GENERIC_USERNAME = "mob"    
    CSS = f"Message.{SOME_GENERIC_USERNAME}" + "{offset:30% 0;}"
    
    

    
    def compose(self) -> ComposeResult:
        yield Message(content=f"[bold blue]blue text", classes="mob")
        yield Message(content="`dimmed`")
        yield Message(content="5*5", classes="mob")
        yield Message(content="*bold*")
        yield Message(content="`dimmed _underline and dimmed_`")
        yield Message(content="^reversed inside of custom hex panel^",color="#5AFC09F3")
        yield Message(content="[@click=self.notify('MASLISCIOUS CODE AH AH AH')]Will render as invalid text", classes="mob")
        

        
        
    
if __name__=="__main__":
    app = MyMessageApp()
    app.run()
