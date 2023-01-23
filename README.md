
# Chat Application

This is a simple chat application that allows multiple clients to connect to a server and chat with each other.
It uses sockets and threading technology to allow clients to interact with each other

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

-   Python 3.x
-   tkinter (if you want the GUI version)

### Installing

-   Clone the repository:

`git clone https://github.com/<Gojimandev/>/python-socket-chat.git` 


### Running the server

To run the server, navigate to the root of the project in the command prompt and run the following command:

`python server.py` 

### Running the client

To run the client, navigate to the root of the project in the command prompt and run the following command:

`python client.py` 

### Usage

-   When the client is launched, it prompts the user to enter a username.
-   Once a username is entered and set, the user can start sending messages to the server, which will then be broadcasted to all connected clients.
-   User can also receive messages from other clients.

## Built With

-   [Python](https://www.python.org/) - The programming language used
-   [socketserver](https://docs.python.org/3/library/socketserver.html) - The built-in Python library used for the server
-   [socket](https://docs.python.org/3/library/socket.html) - The built-in Python library used for the client
-   [tkinter](https://docs.python.org/3/library/tkinter.html) - The built-in Python library used for the GUI

## Authors

-   **Gojibo** - _Initial work_ - [Gojimandev/](https://github.com/Gojimandev/)

## License

This project is licensed under the MIT License 

## Acknowledgments

-   [Nico](https://github.com/NicoLeiner)
