from order import Order


order = Order(
    side="BUY",
    quantity=100,
    price=105,
    order_type="LIMIT"
)

print(order)