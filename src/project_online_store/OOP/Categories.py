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

    def get_products(self) -> str:
        products = []

        for product in self.products:
            products.append(json.loads(str(product)))

        return json.dumps(products)

    def get_product_by_id(self, product_id: int) -> str:
        products = []

        for product in self.products:
            if product.idd == product_id:
                products.append(json.loads(str(product)))

        return json.dumps(products)