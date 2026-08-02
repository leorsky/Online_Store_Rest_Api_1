import socket
import threading
import json

HOST = 'localhost'
PORT = 8000

products = [
    {
        "id": 1,
        "name": "iPhone 15",
        "category": "phone",
        "price": 999,
    },
    {
        "id": 2,
        "name": "Samsung Galaxy S24",
        "category": "phone",
        "price": 899,
    },
]

def create_response(status_code, data):
    response_body = json.dumps(data)

    response = (
        f"HTTP/1.1 {status_code}\r\n"
        "Content-Type: application/json\r\n"
        f"Content-Length: {len(response_body.encode('utf-8'))}\r\n"
        "\r\n"
        f"{response_body}"
    )

    return response.encode("utf-8")

def handle_client(client_socket, client_address):
    try:
        request = client_socket.recv(4096).decode()

        if request == '':
            client_socket.close()

        request_line = request.split('\r\n')[0]

        method, path, http_version = request_line.split()

        print(f"Method: {method}")
        print(f"Path: {path}")


    except Exception as e:
        print(e)






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