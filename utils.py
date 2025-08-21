import socket

DEFAULT_BYTES_SIZE = 1024

def get_pure_data(sender: socket.socket,bytes_size:int = DEFAULT_BYTES_SIZE) -> bytes:
    data = sender.recv(bytes_size)
    return data

def get_data(sender: socket.socket ,bytes_size:int =DEFAULT_BYTES_SIZE, data_encoding:str ="utf-8") -> str:
    data = sender.recv(bytes_size)
    data = data.decode(data_encoding)
    return data

def echo(sender: socket.socket, data = "None is meaningless", data_encoding: str = "utf-8"):
    try:
       data = data.encode(data_encoding)
       sender.sendall(data)     
    except Exception as error:
        print(f"Echo Failed with exception: {error}")
        