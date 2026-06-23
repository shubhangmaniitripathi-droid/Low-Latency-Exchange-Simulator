from dataclasses import dataclass, field
from datetime import datetime
import uuid

@dataclass
class Trade:
    buyer_order_id: str
    seller_order_id: str
    quantity: int
    price: float

    timestamp: datetime = field(init = False, default_factory=datetime.now)
    trade_id: str = field(init = False, default_factory=uuid.uuid4)