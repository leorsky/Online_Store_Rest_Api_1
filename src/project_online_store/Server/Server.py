import socket
import threading
import json

from project_online_store.src.project_online_store.OOP.Categories import Categories
from project_online_store.src.project_online_store.OOP.Products import Products

HOST = 'localhost'
PORT = 8000

product_1_1 = Products(1, "iPhone 15", 999)
product_1_2 = Products(2, "Samsung Galaxy S24", 899)
product_1_3 = Products(3, "iPhone 11", 800)

product_2_1 = Products(1, "Samsung QLED 4K TV", 1299)
product_2_2 = Products(2, "LG OLED C4", 1499)

product_3_1 = Products(1, "MacBook Air M3", 1099)
product_3_2 = Products(2, "ASUS ROG Zephyrus G14", 1599)
product_3_3 = Products(3, "Lenovo ThinkPad X1 Carbon", 1399)

category_1 = Categories(1, [product_1_1, product_1_2, product_1_3])
category_2 = Categories(2, [product_2_1, product_2_2])
category_3 = Categories(3, [product_3_1, product_3_2, product_3_3])

category = [category_1, category_2, category_3]

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

        # GET /api/v1/products
        if method == "GET" and path == "/api/v1/products":
            response = create_response(
                "200 OK",
                products,
            )

        # GET /api/v1/products/1
        elif method == "GET" and path.startswith("/api/v1/products/"):
            product_id = int(path.split("/")[-1])

            product = next(
                (
                    product
                    for product in products
                    if product["id"] == product_id
                ),
                None,
            )

            if product:
                response = create_response(
                    "200 OK",
                    product,
                )
            else:
                response = create_response(
                    "404 Not Found",
                    {"detail": "Product not found"},
                )

        else:
            response = create_response(
                "404 Not Found",
                {"detail": "Endpoint not found"},
            )

        client_socket.sendall(response)

    except Exception as error:
        print(f"Error: {error}")

        response = create_response(
            "500 Internal Server Error",
            {"detail": "Internal server error"},
        )

        client_socket.sendall(response)

    finally:
        client_socket.close()





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