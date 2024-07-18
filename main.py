from datetime import datetime
from connection import MT5Connection
from data import MT5Data
from trading import MT5Trading
from account import MT5Account

# Initialize connection
conn = MT5Connection()
if not conn.initialize():
    exit()

# Print terminal info and version
print(conn.terminal_info())
print(conn.version())

# Account information
account = MT5Account(conn)
print("Account balance:", account.get_balance())
print("Account equity:", account.get_equity())
print("Margin level:", account.get_margin_level())

# Fetch data
data = MT5Data(conn)
euraud_ticks = data.fetch_ticks("EURAUD", datetime(2020, 1, 28, 13), 1000)
if euraud_ticks is not None:
    print('EURAUD ticks:', euraud_ticks[:10])

last_tick = data.fetch_last_tick("EURUSD")
if last_tick is not None:
    print("Last tick for EURUSD:", last_tick)

# Trading operations
trading = MT5Trading(conn)
order_result = trading.place_order(
    symbol="EURUSD",
    order_type=mt5.ORDER_TYPE_BUY,
    volume=0.1,
    price=1.12345,
    stop_loss=1.12200,
    take_profit=1.12500,
    comment="Test order"
)
if order_result is not None:
    print('Order placed:', order_result)

open_orders = trading.get_open_orders()
if open_orders is not None:
    print("Open orders:", open_orders)

# Shutdown connection
conn.shutdown()
