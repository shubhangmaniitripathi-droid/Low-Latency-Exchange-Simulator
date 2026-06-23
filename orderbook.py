from collections import deque
import heapq


class OrderBook:
    def __init__(self):

        self.buy_levels = {} #dictionary of deque to store price levels allowing O(1) lookup time for the price level and then FIFO for the earliest buy order
        self.sell_levels = {} #same as above

        self.buy_prices = [] #min heap with negative prices to maintain the highest buy price\bid at top
        self.sell_prices = [] #min heap to ensure lowest sell price\ask at top

        self.order_lookup = {} #to keep track of orders and order ids for deletion
    def add_order(self, order):
        self.order_lookup[order.order_id] = order
        if order.side == "BUY":
            if order.price not in self.buy_levels: #if the price level is not already present, we add it
                self.buy_levels[order.price] = deque()
                heapq.heappush(self.buy_prices,-order.price)

            self.buy_levels[order.price].append(order)
        else:
            if order.price not in self.sell_levels: #if this sell price doesnt already have a level
                self.sell_levels[order.price] = deque()
                heapq.heappush(self.sell_prices,order.price)

            self.sell_levels[order.price].append(order)
    def best_bid(self):
        if not self.buy_prices:
            return None
        return -self.buy_prices[0]
    def best_ask(self):
        if not self.sell_prices:
            return None
        return self.sell_prices[0]
    def display(self):
        print("\nBUY SIDE")
        for price in sorted(self.buy_levels.keys(),reverse=True):
            volume = sum(
                order.quantity
                for order in self.buy_levels[price]
            )
            print(
                f"Price: {price} | Volume: {volume}"
            )
        print("\nSELL SIDE")
        for price in sorted(self.sell_levels.keys()):
            volume = sum(
                order.quantity
                for order in self.sell_levels[price]
            )
            print(
                f"Price: {price} | Volume: {volume}"
            )