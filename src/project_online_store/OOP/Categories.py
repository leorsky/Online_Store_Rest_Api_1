import json


class Categories:
    def __init__(self, category_id: int, products: list | None = None ) -> None:
        if products is None:
            products = []

        if not isinstance(category_id, int):
            raise TypeError("Category ID must be an integer")
        if not isinstance(products, list):
            raise TypeError("Products must be a list")

        if category_id <= 0:
            raise ValueError("Category ID must be positive")

        self._category_id = category_id
        self._products = products

    @property
    def category_id(self) -> int:
        return self._category_id

    @category_id.setter
    def category_id(self, category_id: int) -> None:
        if not isinstance(category_id, int):
            raise TypeError("Category ID must be an integer")

        if category_id <= 0:
            raise ValueError("Category ID must be positive")

        self._category_id = category_id

    @property
    def products(self) -> list:
        return self._products

    def get_products(self, categories: list) -> str:
        products = []

        for category in categories:
            for product in category.products:
                products.append({
                    "id": product.idd,
                    "name": product.name,
                    "price": product.price,
                })

        return json.dumps(products)

    def get_products_by_category(self, category_id: int, categories: list) -> str | None:
        for category in categories:
            if category.category_id == category_id:
                products = []

                for product in category.products:
                    products.append({
                        "id": product.idd,
                        "name": product.name,
                        "price": product.price,
                    })

                return json.dumps(products)

        return None

    def get_product_by_id(self, category_id: int, product_id: int, categories: list) -> str | None:
        for category in categories:
            if category.category_id == category_id:

                for product in category.products:
                    if product.idd == product_id:
                        return json.dumps({
                            "id": product.idd,
                            "name": product.name,
                            "price": product.price,
                        })

                return None

        return None