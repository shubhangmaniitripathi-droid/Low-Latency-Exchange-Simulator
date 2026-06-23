from dataclasses import dataclass, field
from datetime import datetime
import uuid


@dataclass
class Order:
    side: str          # BUY or SELL
    quantity: int
    price: float
    order_type: str    # LIMIT or MARKET

    order_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=datetime.now)

    def __post_init__(self):

        self.side = self.side.upper()
        self.order_type = self.order_type.upper()

        if self.side not in ["BUY", "SELL"]:
            raise ValueError("side must be BUY or SELL")

        if self.order_type not in ["LIMIT", "MARKET"]:
            raise ValueError("order_type must be LIMIT or MARKET")

        if self.quantity <= 0:
            raise ValueError("quantity must be positive")

        if self.order_type == "LIMIT" and self.price <= 0:
            raise ValueError("price must be positive")