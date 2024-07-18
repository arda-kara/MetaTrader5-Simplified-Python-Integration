import MetaTrader5 as mt5

class MT5Trading:
    """
    A class to handle trading operations in the MetaTrader 5 terminal.
    """

    def __init__(self, connection):
        """
        Initialize the MT5Trading instance.

        Args:
            connection (MT5Connection): An instance of MT5Connection to manage the terminal connection.
        """
        self.connection = connection

    def place_order(self, symbol, order_type, volume, price, stop_loss, take_profit, comment):
        """
        Place an order in the MetaTrader 5 terminal.

        Args:
            symbol (str): The symbol to trade.
            order_type (int): The type of the order (e.g., mt5.ORDER_TYPE_BUY or mt5.ORDER_TYPE_SELL).
            volume (float): The volume of the order.
            price (float): The price at which to execute the order.
            stop_loss (float): The stop loss price.
            take_profit (float): The take profit price.
            comment (str): A comment for the order.

        Returns:
            dict: The result of the order_send request if successful, None otherwise.
        """
        if not self.connection.connected:
            print("MT5 is not initialized")
            return None
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": volume,
            "type": order_type,
            "price": price,
            "sl": stop_loss,
            "tp": take_profit,
            "deviation": 20,
            "magic": 123456,
            "comment": comment,
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_RETURN,
        }
        result = mt5.order_send(request)
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print("Order send failed, retcode =", result.retcode)
            print("Result", result)
            return None
        return result

    def check_order(self, ticket):
        """
        Check the status of an order by its ticket number.

        Args:
            ticket (int): The ticket number of the order.

        Returns:
            dict: The order information if found, None otherwise.
        """
        if not self.connection.connected:
            print("MT5 is not initialized")
            return None
        order = mt5.order_get(ticket)
        if order is None:
            print(f"Order {ticket} not found")
            return None
        return order
