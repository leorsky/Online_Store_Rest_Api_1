class Products:
    def __init__(self, idd: int, name: str, price: float) -> None:
        if not isinstance(idd, int):
            raise TypeError("ID must be an integer")
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")

        if idd <= 0:
            raise ValueError("ID must be a positive integer")
        if price < 0:
            raise ValueError("Price must be a non-negative number")

        self._idd = idd
        self._name = name
        self._price = float(price)

    @property
    def idd(self) -> int:
        return self._idd

    @idd.setter
    def idd(self, idd: int) -> None:
        if not isinstance(idd, int):
            raise TypeError("ID must be an integer")
        if idd <= 0:
            raise ValueError("ID must be a positive integer")

        self._idd = idd

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Name must be a string")

        self._name = name

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, price: float) -> None:
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")
        if price < 0:
            raise ValueError("Price must be a non-negative number")

        self._price = float(price)

    def __str__(self) -> str:
        return (
            f"ID: {self._idd}\r\n"
            f"Name: {self._name}\r\n"
            f"Price: {self._price}"
        )

    def __repr__(self) -> str:
        return (
            f"Products("
            f"idd={self._idd}, "
            f"name='{self._name}', "
            f"price={self._price})"
        )