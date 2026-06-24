from order import Order
from orderbook import OrderBook
from matching_engine import MatchingEngine


book = OrderBook()

engine = MatchingEngine(book)

engine.process_order(
    Order("BUY",100,105,"LIMIT"))

engine.process_order(
    Order("SELL",50,104,"LIMIT"))

engine.process_order(
    Order("BUY",100,105,"LIMIT")
)

engine.process_order(
    Order("BUY",50,105,"LIMIT")
)

engine.process_order(
    Order("SELL",120,105,"LIMIT")
)

engine.process_order(
    Order("SELL",50,105,"LIMIT"))

engine.process_order(
    Order("SELL",100,106,"LIMIT"))

engine.process_order(
    Order("BUY",120,0,"MARKET"))

engine.process_order(
    Order("BUY",120,0,"MARKET"))

engine.process_order(
    Order("SELL",240,105,"LIMIT"))
book.display()

print()

for trade in engine.trade_history:
    print(trade.quantity,end = " ")
    print(trade.price, end = " ")
    print(trade.timestamp, end = "\n")
