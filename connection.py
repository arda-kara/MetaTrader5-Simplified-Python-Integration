import MetaTrader5 as mt5

class MT5Connection:
    """
    A class to manage the connection to the MetaTrader 5 terminal.
    """

    def __init__(self):
        """
        Initialize the MT5Connection instance.

        Attributes:
            connected (bool): Indicates whether the connection to the MT5 terminal is established.
        """
        self.connected = False

    def initialize(self):
        """
        Initialize the connection to the MetaTrader 5 terminal.

        Returns:
            bool: True if the connection is successfully established, False otherwise.
        """
        if not mt5.initialize():
            print("initialize() failed")
            print(mt5.last_error())
            return False
        self.connected = True
        return True

    def shutdown(self):
        """
        Shutdown the connection to the MetaTrader 5 terminal.
        """
        if self.connected:
            mt5.shutdown()
            self.connected = False

    def terminal_info(self):
        """
        Get the terminal information of the connected MetaTrader 5 terminal.

        Returns:
            mt5.TerminalInfo: An object containing information about the MT5 terminal if connected, None otherwise.
        """
        if not self.connected:
            print("MT5 is not initialized")
            return None
        return mt5.terminal_info()

    def version(self):
        """
        Get the version of the connected MetaTrader 5 terminal.

        Returns:
            tuple: A tuple containing the build number, build date, and build time if connected, None otherwise.
        """
        if not self.connected:
            print("MT5 is not initialized")
            return None
        return mt5.version()
