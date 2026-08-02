

class Products:
    def __init__(self, idd: int, name: str, price: float) -> None:
        if not isinstance(idd, int):
            raise TypeError("idd must be an integer")
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(price, (int, float)):
            raise TypeError("price must be a number")

        if idd <= 0:
            raise ValueError("idd must be a positive integer")
        if price < 0:
            raise ValueError("price must be a non-negative number")

        self._idd = idd
        self._name = name
        self._price = float(price)

    @property
    def idd(self) -> int:
        return self._idd
    @idd.setter
    def idd(self, idd: int) -> None:
        if not isinstance(idd, int):
            raise TypeError("idd must be an integer")
        if idd <= 0:
            raise ValueError("idd must be a positive integer")
        self._idd = idd

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self._name = name

    @property
    def price(self) -> float:
        return self._price
    @price.setter
    def price(self, price: float) -> None:
        if not isinstance(price, (int, float)):
            raise TypeError("price must be a number")
        if price < 0:
            raise ValueError("price must be a non-negative number")
        self._price = float(price)

    def get_product_by_id(self, idd: int):
        if not isinstance(idd, int):
            raise TypeError("idd must be an integer")
        if idd <= 0:
            raise ValueError("idd must be a positive integer")

        if self._idd == idd:
            return {
                "id": self._idd,
                "name": self._name,
                "price": self._price,
            }
        else:
            return None