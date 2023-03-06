class Stock():
    __slots__ = ('name', '_shares', 'price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"Stock({self.name!r}, {self.shares!r}, {self.price!r})"

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, amount):
        if not isinstance(amount, int):
            raise TypeError("Must be integer")
        self._shares = amount

    @property
    def cost(self):
        return self.shares * self.price
    
    def sell(self, amount):
        self.shares -= amount


class MyStock(Stock):
    def panic(self):
        self.sell(self.shares)
