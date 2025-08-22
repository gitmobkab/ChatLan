import socket


DEFAULT_BYTES_SIZE = 1024


def get_data(conn: socket.socket ,bytes_size:int =DEFAULT_BYTES_SIZE, data_encoding:str ="utf-8") -> str:
    data = conn.recv(bytes_size)
    data = data.decode(data_encoding)
    return data

def echo_str(conn: socket.socket, data = "None is meaningless", data_encoding: str = "utf-8"):
    try:
       data = data.encode(data_encoding)
       conn.sendall(data)     
    except Exception as error:
        print(f"Echo Failed with exception: {error}")
        
def echo(conn: socket.socket, bytes_size:int = DEFAULT_BYTES_SIZE):
    try:
        data = conn.recv(bytes_size)
        if data:
            conn.sendall(data)
    except Exception as error:
        print(f"Echo Failed: {error}")
        
        
class Client():
    def __init__(self,name:str ,socket: socket.socket ,addr: tuple) -> None:
        self.name = name
        self.socket = socket
        self.addr = addr
    
    def  __repr__(self) -> str:
        return f"{self.name}/{self.addr}"
    
    def __str__(self) -> str:
        return f"{self.name}/{self.addr}"
    
    