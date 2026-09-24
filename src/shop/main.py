from products import Product
from shopping import ShoppingCart


cart = ShoppingCart()

laptop = Product(
    "Laptop",
    50000,
    1
)

mouse = Product(
    "Mouse",
    1000,
    2
)


cart.add_product(laptop)
cart.add_product(mouse)

total = cart.calculate_total()

print("Total:", total)