# ChatLan

<p align="center">
  <img src="images/preview.png" alt="preview image">
</p>


## an easy to use chat app command line interface tool

**ChatLan** is a lightweight and fast hybrid command-line interface (CLI) and Text User Interface (TUI) tool designed to facilitate peer-to-peer chatting over a Local Area Network (LAN). 

It allows users to easily spin up a chat server and connect to it from different machines on the same network without complex configuration.

> [!IMPORTANT]
> Before using Chatlan for production purposes, please be aware that it currently lacks encryption and advanced security features. It is recommended to use Chatlan in trusted environments only. for more information see the [Notes and Limitations](#notes-and-limitations) section.

# Features
- **Easy to use CLI commands to start a server and connect clients.**
- Real-time messaging between multiple clients.
- Simple and intuitive text-based user interface (TUI).
- **Socket-based communication for low latency.**
- **Asynchronous handling of messages for smooth user experience, less 'stressful' than multi-threaded approaches.**
- Powerful markup system to format messages with **colors**, **bold**, *italics*, underline, ~~strikethrough~~ and more.
- Powered by the **Bests** when it comes to TUI/CLI based Applications:
    - [Rich](https://github.com/Textualize/rich)
    - [Textual](https://github.com/Textualize/textual)
    - [Typer](https://github.com/fastapi/typer)

# Table Of Contents
- [Install](#install)
  - [Automatic Installation](#automatic-installation)
  - [Manual Installation](#manual-installation)
- [Contributing](#contributing)
- [Quick Overview](#quick-overview)
    - [ChatLan markup system](#chatlan-markup-system)
- [Commands](#commands)
    - [Initialize a Chatlan server (init)](#init)
    - [Connect To a ChatLan Server (connect)](#connect)
- [Examples](#examples)
- [Notes and Limitations](#notes-and-limitations)
- [Troubleshooting](#troubleshooting)
- [Planned Features](#planned-features)


# Install
In order to use **ChatLan**, you must install it with the following command:

- ## Automatic Installation

```bash
$ pip install chatlan
```
- ## Manual Installation
1. First, clone the repository:

```bash
$ git clone https://github.com/gitmobkab/ChatLan.git
```
2. Navigate to the project directory:

```bash
$ cd ChatLan
```
3. Install the required dependencies:

- through poetry (recommended):
```bash
$ poetry install
```

- Through pip:
```bash
$ pip install -r requirements.txt
```

> [!NOTE]
> It's recommended to use a virtual environment to avoid dependency conflicts.  
> For more information on setting up virtual environments, refer to the [Python Virtual Environments Documentation](https://docs.python.org/3/tutorial/venv.html).

# Contributing
If you wish to contribute to this project (which is highly appreciated), see the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.


# Quick overview

In order to use **Chatlan** you have two options
- [Start a Chatlan server (init) ](#init) 
- [Connect to a ChatLan server (connect) ](#connect)

the most common use flow being the following

1. First, let's start a ChatLan Server with the command:

```bash
$ chat init
```

this will show the following screen:

<p align="center">
  <img src="images/server_startup_2.png" alt="new server app TUI (v0.3.0)">
</p>


- **At your left is a list of all the poeple connected to the server as a the table**

for example:

| username          | address      |    color    |
--------------------|--------------|-------------|
|   USERNAME  (you) | 192.168.1.9  | #FFD700   |
|       mobsy       | 192.168.1.25 | #BC00A9   |
|        mob        | 192.168.1.11 | #0D13EA   |


> [!NOTE]
> The First row is always the server

- **At your right is the Chat Panel composed of the Chat Log and Your Chat Input**
  - On the top of the Chat Panel is the **ChatLog** inside of it, every events are displayed

    For ChatLan an event is either when a client joined/leaved the server the always start with **`[-]`** or **`[+]`**
    or When a user send a message, those don't start with a given prefix

  - on the bottom of the Chat Panel is your Chat Input, this works in the same way as the client, you use it to send messages as the server admin

# ChatLan markup system
**ChatLan** supports a simple yet powerful markup system to format messages.

this syntax is composed of two use cases, simple and advanced
- 1. Simple Markup: 
   - **To make text bold**, wrap it with `*` (e.g., `*bold text*`).
   - *To italicize text*, use `/` (e.g., `/italic text/`).

the availables markup chars with their effects are:
| Markup Char | Effect        | Example               |
|-------------|---------------|-----------------------|
| `*`         | **Bold**      | `*bold text*`         |
| `/`         | *Italic*      | `/italic text/`       |
| `_`         | Underline     | `_underlined text_`   |
| `~`         | ~~Strikethrough~~ | `~strikethrough~`     |
| `^`         | reversed text color | `^reversed color^`    | 

> [!NOTE]
> You can combine multiple markup styles by nesting them, e.g., `*/bold and italic/*`.
> ChatLan doesn't care if the markup chars are not closed properly, for example `*This is bold and /this is italic* but this is still italic/` will work as expected

- 2. advanced Markup:

  - this one is based on Rich Text Markup Syntax allowing to change the color of the text and even make blinking text (i don't recommend using blinking text it's annoying)
- to use advanced markup you must use the following syntax
    - `[style] your text`
        As you can see the style is surrounded by square brackets
    - the style can be a color name (red, green, blue, yellow, etc) or a hex color code (#RRGGBB)
    - you can also combine multiple styles by separating them with a space
    - for example to make a text red and bold you can use `[red bold] your text`
    - to make blinking text you can use the `blink` style
    - for example `[blink red] your text` will make the text red and blinking
    ## exemples:  
    - `[red] This text is red`
    - `[red] i'm angry ! but sometimes... [blue] i'm blue ba di bi ba da ba`
    - `[blink] this text is mostly annoying`

> [!IMPORTANT]
> Be careful when using advanced markup as not all terminal emulators support all styles and colors.

> [!WARNING]
> In this version of chatlan any text containing square brackets `[` or `]` will be considered as advanced markup, so if you want to send a message containing those chars you must surround them with quotes or double quotes

i.e:

> "This [text] won't be displayed in your message"

> "But '['text']' will be displayed properly"

(We excuse for this inconvenience, this will be fixed in future versions)

2. In order for anyone to chat just need to use the following command:

```bash
$ chat connect ADDRESS 
```

**ADDRESS** is the address of the ChatLan server in the format IP:PORT
**IP** is a string of four numbers separated by dots (.) each number must be between 0 and 255
**PORT** is an integer between 8000 and 9000 (by defaulf ChatLan uses the 8888 port)

for example if someone wants to connect to the server '192.168.1.9:8888' as 'Mobsy'
they must run
```bash
$ chat connect 192.168.1.9:8888 -u Mobsy
# or also
$ chat connect -u Mobsy 192.168.1.9:8888
```

Then the user can chat as Mob as long as the server is running:

<p align="center">
  <img src="images/client_app_2.png" alt=" new client app interface">
</p>

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
# 127.0.1.1  mob-hpprobook # you just need to add a `#` at the start of this line `mob-hpprobook` should be your machine hostname 
```
> [!NOTE]
> After editing the `/etc/hosts` file you must restart your computer for the changes to take effect
> This issue does not occur on Windows systems and is specific to certain Linux distributions (EndeavourOs,Arch based distros).

# Notes and limitations

> [!IMPORTANT]
> No Secure Messaging System: **The message aren't actually encrypted, so don't use ChatLan for a professional/marketing context**

- Same network required: Clients and server must be on the same LAN/Wi-Fi network.

- User table: The server TUI shows connected users dynamically (username + IP). Disconnects are handled and reflected in the table.

-  Address validation: Addresses containing 127.0.0.1 are treated as invalid for client connections (client must reach server on LAN IP).

- Limited to text: ChatLan only supports text messages; no multimedia support.

- No authentication: There's no user authentication; anyone who knows the server address can join.

- No proper server controls: The server admin can chat but has no advanced controls (e.g., kicking users, banning users).

- The client App is unable to reconnect automatically if the connection is lost, the user must restart the client app to reconnect and can't properly tell if the first connection attempts succeeded, the only feedback is when the user tries to send a message and it fails 
    - a notification will be displayed each time the user tries to send a message while disconnected

# Planned features: 

> [!NOTE]
> ChatLan is currently in a paused development state, as i'm focusing on other projects ([TFM](https://github.com/gitmobkab/mob-tfm), [TabControl](https://github.com/gitmobkab/TabControl),[DataFy](https://github.com/gitmobkab/DataFy)), but i still plan to add more features in the future

- [x] server broadcast input
- [X] message widget UI.
- [X] user random colors
- [X] advanced markup system
- [ ] Proper reconnection system for clients
- [ ] encryption system (probably through TLS)
- [ ] user authentication system