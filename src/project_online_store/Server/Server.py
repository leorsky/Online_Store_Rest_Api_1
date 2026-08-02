import socket
import threading
import json

HOST = 'localhost'
PORT = 8000

def handle_client(client_socket, client_address):
    pass

def start_server():
    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server_socket.bind((HOST, PORT))

    server_socket.listen()

    print(f"Server started on http://{HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()

        print(f"Client connected: {client_address}")

        thread = threading.Thread(
            target=handle_client,
            args=(client_socket,client_address),
        )
        thread.start()



if __name__ == '__main__':
    start_server()