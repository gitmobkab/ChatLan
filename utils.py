import socket

DEFAULT_BYTES_SIZE = 8192


def get_data(conn: socket.socket ,bytes_size:int =DEFAULT_BYTES_SIZE, data_encoding:str ="utf-8") -> str:
    data = conn.recv(bytes_size)
    data = data.decode(data_encoding)
    return data

def send_data(conn: socket.socket, data: str, data_encoding: str = "utf-8"):
    try:
        words = data.split()
        if not words:
            return
        msg = " ".join(words)
        encoded_data = msg.encode(data_encoding)
        conn.sendall(encoded_data)   
    except Exception as error:
        print(f"Sending data failed: {error}")
        
def echo(conn: socket.socket, bytes_size:int = DEFAULT_BYTES_SIZE):
    try:
        data = conn.recv(bytes_size)
        if data:
            conn.sendall(data)
    except Exception as error:
        print(f"Echo Failed: {error}")
        
def format_for_send(user: str, data: str, role: str = "client") -> str:
    words = data.split()
    if not words:
        return ""
    formatted_data = f"{user} " + " ".join(words) + f" @{role}"
    return formatted_data
        
        
class Client():
    def __init__(self,name:str ,socket: socket.socket ,addr: tuple) -> None:
        self.name = name
        self.socket = socket
        self.addr = addr
    
    def  __repr__(self) -> str:
        return f"{self.name}/{self.addr}"
    
    def __str__(self) -> str:
        return f"{self.name}/{self.addr}"
    
    def __eq__(self, value: object) -> bool:
        return isinstance(value,Client) and self.socket == value.socket
    

if __name__ == "__main__":
    pass