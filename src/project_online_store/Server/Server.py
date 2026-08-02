import socket
import json
import re

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

categories = [category_1, category_2, category_3]


def create_response(status_code, data):
    response = (
        f"HTTP/1.1 {status_code}\r\n"
        "Content-Type: application/json\r\n"
        f"Content-Length: {len(data.encode('utf-8'))}\r\n"
        "\r\n"
        f"{data}"
    )

    return response.encode("utf-8")


def handle_client(client_socket):
    try:
        request = client_socket.recv(4096).decode()

        if not request:
            return

        request_line = request.split('\r\n')[0]

        method, path, http_version = request_line.split()
        if method == "POST":
            body = request.split("\r\n\r\n", 1)[-1]

        print(f"Method: {method}")
        print(f"Path: {path}")

        # GET /api/v1/products
        if method == "GET" and path == "/api/v1/products":
            data = []

            for category in categories:
                data.extend(
                    json.loads(category.get_products())
                )

            response = create_response(
                "200 OK",
                json.dumps(data)
            )

        # GET /api/v1/products/{id_category}
        elif method == "GET" and re.fullmatch(r"/api/v1/products/\d+$", path):
            category_id = int(path.split("/")[-1])

            for category in categories:
                if category.category_id == category_id:
                    data = category.get_products()
                    break
            else:
                data = None

            if data is not None:
                response = create_response(
                    "200 OK",
                    data,
                )
            else:
                response = create_response(
                    "404 Not Found",
                    json.dumps({
                        "detail": "Product not found"
                    }),
                )

        # GET /api/v1/products/{id_category}/{id_product}
        elif method == "GET" and re.fullmatch(r"/api/v1/products/\d+/\d+", path):
            category_id = int(path.split("/")[-2])
            product_id = int(path.split("/")[-1])

            for category in categories:
                if category.category_id == category_id:
                    data = category.get_product_by_id(product_id)
                    break
            else:
                data = None

            if data is not None:
                response = create_response(
                    "200 OK",
                    data,
                )
            else:
                response = create_response(
                    "404 Not Found",
                    json.dumps({
                        "detail": "Product not found"
                    }),
                )

        # POST /api/v1/products/{id_category}
        elif method == "POST" and re.fullmatch(r"/api/v1/products/\d+", path):
            category_id = int(path.split("/")[-1])

            try:
                product_data = json.loads(body)

                product_id = product_data["id"]
                product_name = product_data["name"]
                product_price = product_data["price"]

                new_product = Products(
                    product_id,
                    product_name,
                    product_price
                )

                for category in categories:
                    if category.category_id == category_id:
                        category.products.append(new_product)

                        response = create_response(
                            "201 Created",
                            json.dumps({
                                "id": product_id,
                                "name": product_name,
                                "price": product_price
                            })
                        )
                        break
                else:
                    response = create_response(
                        "404 Not Found",
                        json.dumps({
                            "detail": "Category not found"
                        })
                    )

            except json.JSONDecodeError:
                response = create_response(
                    "400 Bad Request",
                    json.dumps({
                        "detail": "Invalid JSON in request body"
                    })
                )

        # DELETE /api/v1/products/{id_category}/{id_product}
        elif method == "DELETE" and re.fullmatch(r"/api/v1/products/\d+/\d+", path):
            category_id = int(path.split("/")[-2])
            product_id = int(path.split("/")[-1])

            for category in categories:
                if category.category_id == category_id:
                    for product in category.products:
                        if product.idd == product_id:
                            data = category.get_product_by_id(product_id)
                            category.products.remove(product)
                            response = create_response(
                                "204 No Content",
                                data
                            )
                            break
                    break
            else:
                response = create_response(
                    "404 Not Found",
                    json.dumps({
                        "detail": "Category not found"
                    })
                )


        else:
            response = create_response(
                "404 Not Found",
                json.dumps({
                    "detail": "Endpoint not found"
                }),
            )

        client_socket.sendall(response)

    except Exception as error:
        print(f"Error: {error}")

        response = create_response(
            "500 Internal Server Error",
            json.dumps({
                "detail": "Internal server error"
            }),
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

        handle_client(client_socket)


if __name__ == '__main__':
    start_server()