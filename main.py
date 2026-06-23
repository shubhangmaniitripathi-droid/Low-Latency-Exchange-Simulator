from order import Order


ord1 = Order(
    side="BUY",
    quantity=100,
    price=105,
    order_type="LIMIT"
)

print(ord1)