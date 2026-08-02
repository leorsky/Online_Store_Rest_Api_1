import socket
import json

HOST = 'localhost'
PORT = 8000


while True:
    try:
        method = input("\nYour method: ").upper()
        path = input("Your path: ")

        if method == "GET":
            request = (
                f"{method} {path} HTTP/1.1\r\n"
                f"Host: {HOST}:{PORT}\r\n"
                "Accept: application/json\r\n"
                "Content-Type: application/json\r\n"
                "\r\n"
            )
        elif method == "POST":
            body = input("Your request body: ")
            request = (
                f"{method} {path} HTTP/1.1\r\n"
                f"Host: {HOST}:{PORT}\r\n"
                "Accept: application/json\r\n"
                "Content-Type: application/json\r\n"
                f"Content-Length: {len(body)}\r\n"
                "\r\n"
                f"{body}"
            )
        elif method == "PUT":
            pass
        elif method == "DELETE":
            request = (
                f"{method} {path} HTTP/1.1\r\n"
                f"Host: {HOST}:{PORT}\r\n"
                "Accept: application/json\r\n"
                "Content-Type: application/json\r\n"
                "\r\n"
            )
        else:
            print("Invalid method. Please use GET, POST, PUT, or DELETE.")
            continue

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

        headers, body = response.decode("utf-8").split("\r\n\r\n", 1)

        print("\nSERVER RESPONSE:")
        print(headers)

        print("\nBODY:")

        try:
            json_body = json.loads(body)

            print(
                json.dumps(
                    json_body,
                    indent=4,
                    ensure_ascii=False
                )
            )

        except json.JSONDecodeError:
            print(body)

        client_socket.close()

    except (ConnectionResetError, OSError) as error:
        print(f"Connection error: {error}")
        break