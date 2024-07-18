from datetime import datetime
import MetaTrader5 as mt5

class MT5Data:
    """
    A class to handle data retrieval from the MetaTrader 5 terminal.
    """

    def __init__(self, connection):
        """
        Initialize the MT5Data instance.

        Args:
            connection (MT5Connection): An instance of MT5Connection to manage the terminal connection.
        """
        self.connection = connection

    def check_symbol(self, symbol):
        """
        Ensure the specified symbol is available and selected in the MetaTrader 5 terminal.

        Args:
            symbol (str): The symbol to check and select.

        Returns:
            bool: True if the symbol is successfully selected, False otherwise.
        """
        if not mt5.symbol_select(symbol, True):
            print(f"Failed to select {symbol}")
            return False
        return True

    def fetch_ticks(self, symbol, from_date, count):
        """
        Fetch a specified number of ticks for a symbol starting from a given date.

        Args:
            symbol (str): The symbol to fetch ticks for.
            from_date (datetime): The starting date and time for tick data retrieval.
            count (int): The number of ticks to retrieve.

        Returns:
            numpy.array: An array of tick data if successful, None otherwise.
        """
        if not self.check_symbol(symbol):
            return None
        ticks = mt5.copy_ticks_from(symbol, from_date, count, mt5.COPY_TICKS_ALL)
        if ticks is None:
            print(f"Failed to get {symbol} ticks:", mt5.last_error())
        return ticks

    def fetch_ticks_range(self, symbol, from_date, to_date):
        """
        Fetch ticks for a symbol within a specified date range.

        Args:
            symbol (str): The symbol to fetch ticks for.
            from_date (datetime): The starting date and time for tick data retrieval.
            to_date (datetime): The ending date and time for tick data retrieval.

        Returns:
            numpy.array: An array of tick data if successful, None otherwise.
        """
        if not self.check_symbol(symbol):
            return None
        ticks = mt5.copy_ticks_range(symbol, from_date, to_date, mt5.COPY_TICKS_ALL)
        if ticks is None:
            print(f"Failed to get {symbol} ticks:", mt5.last_error())
        return ticks

    def fetch_rates(self, symbol, timeframe, from_date, count):
        """
        Fetch a specified number of bars (rates) for a symbol starting from a given date and timeframe.

        Args:
            symbol (str): The symbol to fetch rates for.
            timeframe (int): The timeframe for the rates (e.g., mt5.TIMEFRAME_M1).
            from_date (datetime): The starting date and time for rate data retrieval.
            count (int): The number of rates to retrieve.

        Returns:
            numpy.array: An array of rate data if successful, None otherwise.
        """
        if not self.check_symbol(symbol):
            return None
        rates = mt5.copy_rates_from(symbol, timeframe, from_date, count)
        if rates is None:
            print(f"Failed to get {symbol} rates:", mt5.last_error())
        return rates
