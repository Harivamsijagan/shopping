class Product:

    def __init__(self, name, price, quantity):

        if price < 0:
            raise ValueError("Price cannot be negative")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }