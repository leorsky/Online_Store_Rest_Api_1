import socket

HOST = 'localhost'
PORT = 8000


while True:
    try:
        method = input("\nYour method: ")
        path = input("Your path: ")

        request = (
            f"{method} {path} HTTP/1.1\r\n"
            f"Host: {HOST}:{PORT}\r\n"
            "Accept: application/json\r\n"
            "Content-Type: application/json\r\n"
            "\r\n"
        )

        client_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        client_socket.connect(
            (HOST, PORT)
        )

        client_socket.sendall(
            request.encode("utf-8")
        )

        response = client_socket.recv(4096)

        print("\nSERVER RESPONSE:")
        print(response.decode("utf-8"))

        client_socket.close()

    except (ConnectionResetError, OSError) as error:
        print(f"Connection error: {error}")
        break