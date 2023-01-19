import socket
import threading
import tkinter as tk

def receive(client):
    while True:
        data = client.recv(1024).strip()
        if not data:
            break
        text_widget.insert(tk.END, data.decode() + "\n")

def send_message():
    message = message_entry.get()
    client.sendall((username + ": " + message).encode())
    message_entry.delete(0, tk.END)

def set_username():
    global username
    username = username_entry.get()
    username_entry.delete(0, tk.END)
    username_label.config(text=username)

if __name__ == "__main__":
    HOST, PORT = "localhost", 40010

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    receive_thread = threading.Thread(target=receive, args=(client,))
    receive_thread.start()

    root = tk.Tk()
    root.title("Secrete Chat")

    username_label = tk.Label(root, text="Enter your username:")
    username_label.pack()

    username_entry = tk.Entry(root)
    username_entry.pack()

    set_username_button = tk.Button(root, text="Set Username", command=set_username)
    set_username_button.pack()

    text_widget = tk.Text(root)
    text_widget.pack()

    message_entry = tk.Entry(root)
    message_entry.pack()

    send_button = tk.Button(root, text="Send", command=send_message)
    send_button.pack()

    root.mainloop()
