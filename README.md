# ChatLan 
> [!IMPORTANT]
> This version is considered as the old/legacy version of chatlan
> if you're looking for the latest version go to **[Chatlan rewrite branch](https://github.com/gitmobkab/ChatLan/tree/rewrite "chatlan rewrite branch")** instead
> 
> **We strongly discourage you to use it because of many bugs, Use at your own risk**


## What is it ?

ChatLan is a TUI project designed for Chatting with a bunch of friends on a LAN network

It is compatible with Linux, Windows and Mac

## Setup

- PREREQUISITES:
    - [The Python Interpreter](https://www.python.org/downloads/) installed in your system (Version >= 3.8 but Latest is recommended)
    - [The Textual Library](https://textual.textualize.io)
    - A Lan Network (It is mostly intended to be used on WIFI)
 

## Usage

To use ChatLan, first clone the repository into your machine with the command

```
git clone https://github.com/gitmobkab/ChatLan.git
cd ChatLan
```

1. Starting the Server

In order to use you'll need to setup the server for the chat 

You can do that with the command on each system:

- Windows:

```
server.py
```

or 

```
python server.py
```

- Linux/mac

```
python3 server.py
```

after that if the operation is succesfull you'll see the following output
```
---------------------Chat Lan-------------------
Server successfully started
IP ADDRESS: TheServerAddress
```

2. Using Chat Lan to chat with your friends

After The Server successfully started you just have to launch the client_ui script

It requires one argument(The server Address) and an optional one (-n: Your UserName for the session) 

**NOTE : DO NOT USE `client.py` instead of `client_ui.py` since it doesn't have the features to enhance the UX**

- Windows: 
```
client_ui.py <TheServerAddress> [-n Your_Username]
```
or 

```
python client_ui.py <TheServerAddress> [-n Your_Username]
```

- Mac/Linux:

```
python3 client_ui.py <TheServerAddress> [-n Your_username]
```

if you run `client_ui.py` without providing a username yours is going to be User(random_number)

**Note: ChatLan has been designed to allow multiple users to have the same username**



