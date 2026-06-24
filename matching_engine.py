from trade import Trade

class MatchingEngine:
    def __init__(self, orderbook):
        self.orderbook = orderbook
        self.trade_history = []
    def process_order(self, order):
        if order.side == "BUY":
            self._process_buy(order)
        else:
            self._process_sell(order)

    def _process_buy(self, buy_order):
        while buy_order.quantity > 0:
            best_ask = self.orderbook.get_best_ask()
            if best_ask is None:
                break
            if (buy_order.order_type == "LIMIT" and buy_order.price < best_ask): #to account for market orders which dont care about price
                break
            sell_queue = self.orderbook.sell_levels[best_ask]
            sell_order = sell_queue[0]
            
            trade_qty = min(
                buy_order.quantity,
                sell_order.quantity
            )

            print("BUY TRADE CREATED:",trade_qty,"@",best_ask)
            trade = Trade(
                buyer_order_id=buy_order.order_id,
                seller_order_id=sell_order.order_id,
                quantity=trade_qty,
                price=best_ask
            )

            self.trade_history.append(trade)

            buy_order.quantity -= trade_qty
            sell_order.quantity -= trade_qty

            if sell_order.quantity == 0:
                sell_queue.popleft()
                if len(sell_queue) == 0:
                    self.orderbook.remove_price_level("SELL",best_ask)
        if buy_order.quantity > 0 and buy_order.order_type == "LIMIT":
            self.orderbook.add_order(buy_order)

    def _process_sell(self, sell_order):
        while sell_order.quantity > 0:
            best_bid = self.orderbook.get_best_bid()

            if best_bid is None:
                break
            if (sell_order.order_type == "LIMIT" and sell_order.price > best_bid): #to account for market orders
                break

            buy_queue = self.orderbook.buy_levels[best_bid]
            buy_order = buy_queue[0]

            trade_qty = min(
                sell_order.quantity,
                buy_order.quantity
            )
            print("SELL TRADE CREATED:",trade_qty,"@",best_bid)
            trade = Trade(
                buyer_order_id=buy_order.order_id,
                seller_order_id=sell_order.order_id,
                quantity=trade_qty,
                price=best_bid
            )

            self.trade_history.append(trade)

            sell_order.quantity -= trade_qty
            buy_order.quantity -= trade_qty

            if buy_order.quantity == 0:
                buy_queue.popleft()
                if len(buy_queue) == 0:
                    self.orderbook.remove_price_level("BUY",best_bid)
        if sell_order.quantity > 0 and sell_order.order_type ==  "LIMIT":
            self.orderbook.add_order(
                sell_order
            )