from dataclasses import dataclass
from datetime import datetime


@dataclass
class Trade:
    buyer_order_id: str
    seller_order_id: str
    quantity: int
    price: float

    timestamp: datetime = datetime.now()