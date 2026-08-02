

class Products:
    def __init__(self, idd: int, name: str, category: str, price: float) -> None:
        self._idd = idd
        self._name = name
        self._category = category
        self._price = price