

class Products:
    def __init__(self, idd: int, name: str, category: str, price: float) -> None:
        if not isinstance(idd, int):
            raise TypeError("idd must be an integer")
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(category, str):
            raise TypeError("category must be a string")
        if not isinstance(price, (int, float)):
            raise TypeError("price must be a number")



        self._idd = idd
        self._name = name
        self._category = category
        self._price = float(price)