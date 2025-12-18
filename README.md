# ChatLan

<p align="center">
  <img src="images/preview.png" alt="preview image">
</p>


## an easy to use chat app command line interface tool

**ChatLan** is a lightweight command-line interface (CLI) tool designed to facilitate peer-to-peer chatting over a Local Area Network (LAN). It allows users to easily spin up a chat server and connect to it from different machines on the same network without complex configuration.


# Table Of Contents
- [Install](#install)
- [Quick Overview](#quick-overview)
- [Commands](#commands)
    - [Initialize a Chatlan server (init)](#init)
    - [Connect To a ChatLan Server (connect)](#connect)
- [Examples](#examples)
- [Notes and Limitations](#notes-and-limitations)
- [Troubleshooting](#troubleshooting)
- [Planned Features](#planned-features)


# Install
In order to use **ChatLan**, you must install it with the following command:

```bash
pip install chatlan
```

# Quick overview

In order to use **Chatlan** you have two options
- [Start a Chatlan server (init) ](#init) 
- [Connect to a ChatLan server](#connect)

the most common use flow being the following

1. First, let's start a ChatLan Server with the command:

```bash
$ chat init
```
this will show the following screen:
![server app TUI](images/server_startup.png)

- **At your left is a list of all the poeple connected to the server as a the table**

for example:

| username          | address      |
--------------------|--------------|
|   USERNAME  (you) | 192.168.1.9  |
|       mobsy       | 192.168.1.25 |
|        mob        | 192.168.1.11 |

> [!NOTE]
> The First row is always the server

- **At your right is the Chat Panel composed of the Chat Log and Your Chat Input**
  - On the top of the Chat Panel is the **ChatLog** inside of it, every events are displayed

    For ChatLan an event is either when a client joined/leaved the server the always start with **`[-]`** or **`[+]`**
    or When a user send a message, those don't start with a given prefix

  - on the bottom of the Chat Panel is your Chat Input, this works in the same way as the client, you use it to send messages as the server admin


2. In order for anyone to chat just need to use the following command:

```bash
$ chat connect ADDRESS 
```

for example if someone wants to connect to the server '192.168.1.9:8888' as 'Mobsy'
they must run
```bash
$ chat connect 192.168.1.9:8888 -u Mobsy
# or also
$ chat connect -u Mobsy 192.168.1.9:8888
```

Then the user can chat as Mob as long as the server is running:

![The Client App Interface](images/client_app.png)

> [!IMPORTANT]
> **The Users and The Server must be on the same network/wifi** 

# Commands

**chatlan** is in the first place a command line interface program (CLI)
the command name of the **ChatLan** is **chat**

the availvable commands are:
 - [chat](#chat)
 - [chat init](#init)
 - [chat connect](#connect)

- ## chat
the chat command doesn't do anythig by itself, except displaying a help menu

```bash
$ chat
```

this will show the following
![chat command help menu](images/chat_command.png)

- ## init

**Usage: chat init [options] [IP]** 

> **Initialize a chatlan server at a given ip address**

![init command help menu](images/init_command.png)

- arguments:
    - IP optional [default: your current ip address]:
        
        a string representing the ip to use in the server runtime, this argument is only meant for advanced configuration most users are advise to only use the options of **`chat init`**

        i.e: `chat init 192.168.2.54`

- options:
    - -p, --port \<PORT> [DEFAULT: 8888]: 
    
        \<PORT> must be an integer between 8000 and 9000

        **if ignored the default ChatLan PORT (8888) is used**
    
    - -u, --username \<USERNAME>:

        USERNAME is a string representing the server username for the chat session, this is only relevant if you plan to use the server to chat directly

        **if ignored your computer hostname is used instead**

    - -- help:
        
        Display the help menu

- ## connect

**Usage: chat connect \<ADDRESS> [options]**

> **Connect to a ChatLan Server**

![connect command help menu](images/connect.png)

- arguments:
    - \<ADDRESS>:

        the address of the ChatLan Server.
        
        this argument is a string in the format IP:PORT

        i.e: 
            
            192.168.1.9:8888
            192.168.1.10:8888

> [!NOTE]
> The any ADDRESS with '127.*' or '0.0.0.0' as the IP are invalid
> i.e : 127.0.0.1, 127.0.0.2, 127.20.50,254

- options:
    - -u, --username [DEFAULT: your machine hostname]:

        this option is the name you wish to use for the chat session.

        by default your username is your machine hostname

        i.e: 'mob-hpprobook'

> [!NOTE]
> If your username contains spaces you must surround it with quotes or double quotes **(i.e: "Cool User")**
    

# Examples

In This section are snippets on actual use case of ChatLan

**Starting A ChatLan Server**

The most basic approach is to use

```bash
$ chat init
```

note that this running the above command will start a ChatLan Server on the **8888** port.

### Why is this important ? 
This is due to the fact that the server must be started on a port that's not used by any programm

for example the vscode extension Live server/Five Server runs on the 8000 port 

so if you have Live Server Running on and run `chat init -p 8000`

**ChatLan won't be able to start the server as Live Server is already using the 8000 port**

This also means that if you run `chat init` and see an error this is very likely because another service is already using the 8888 port

To solve this you must try to run The ChatLan server on another port 8815 for example

> [!IMPORTANT]
> In This Version ChatLan doesn't prevent you to start a server  on an 'unreachable address' an address is juged unreachable if the IP part of the ADDRESS is either 127.0.0.1 or 0.0.0.0


## Connecting to a ChatLan Server

**In order o connect to a ChatLan server you must check two thing**

1. your computer is connected to a LAN or WLAN (wifi for example)

2. A ChatLan Server is running

3. Your Computer and The ChatLan Server are on the same network

the most 'rough' use of the connect command is:

```bash
$ chat connect <ADDRESS>
```

> [!NOTE]
> When a ChatLan server is started it will display 'Server Started Successfully at ADDRESS' in the first line of the Chat View, the ADDRESS is what the clients must pass to chat connect

for example let's say i wanna connect to the ChatLan server 192.168.1.9:8888

i'll run
```bash
$ chat connect 192.168.1.9:8888
```

this will connect me to the server as 'mob-hpprobook' 

# why 'mob-hpprobook' ? that's oddly specific...

Well if you run `chat connect` without using the -u,--username option ChatLan is going to use your machine hostname as your username

In my case this is 'mob-hpprobook'

# What if i want to have a cool username ?

Simple, just add the -u or --username option followed by your USERNAME

for example if i prefer 'Mobsy' rather than 'mob-hpprobook'

i just need to run

```bash
$ chat connect <ADDRESS> -u Mobsy
# or
$ chat connect -u Mobsy <ADDRESS>
``` 

in our previous example this will be
```bash
$ chat connect 192.168.1.9:8888 -u Mobsy
# or
$ chat connect -u Mobsy 192.168.1.9:8888
```

> [!NOTE]
> If the username you wish to use contains Spaces like 'Cool User 2025' you must surround the USERNAME with quotes (') or double quotes (")

```bash
$ chat connect 192.168.1.9:8888 -u "Cool User 2025"
# or
$ Chat connect -u "Cool User 2025" 192.168.1.9:8888
```
# Troubleshooting

> [!IMPORTANT]
> On Linux/Mac, you may get the address '127.0.1.1:8888' when starting the chatlan server, 
> This is an unreachable address caused by an incorrect network configuration
> To fix this you must edit the `/etc/hosts` file. for example make sure that it's the same as the snippet below:
```bash
# Standard host addresses
127.0.0.1  localhost
::1        localhost ip6-localhost ip6-loopback
ff02::1    ip6-allnodes
ff02::2    ip6-allrouters
# This host address
# 127.0.1.1  mob-hpprobook # you just need to add a `#` at the start of the line `mob-hpprobook` should be your machine hostname 
```

# Notes and limitations

> [!IMPORTANT]
> No Secure Messaging System: **The message aren't actually encrypted, so don't use ChatLan for a professional/marketing context**

- Same network required: Clients and server must be on the same LAN/Wi-Fi network.

- No server-side chat input (yet): Server cannot send messages from the UI in this release — planned for the next update.

- User table: The server TUI shows connected users dynamically (username + IP). Disconnects are handled and reflected in the table.

-  Address validation: Addresses containing 127.0.0.1 are treated as invalid for client connections (client must reach server on LAN IP).

# Planned features: 

- [x] server broadcast input
- [ ] message widget UI.
- [ ] user random colors
