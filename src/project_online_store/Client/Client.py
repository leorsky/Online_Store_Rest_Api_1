import socket
import threading
import json

HOST = 'localhost'
PORT = 8000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def receive_messages() -> None:
    pass

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    pass

client_socket.close()