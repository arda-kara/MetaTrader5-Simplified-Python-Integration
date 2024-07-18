import MetaTrader5 as mt5

class MT5Account:
    """
    A class to represent the MetaTrader 5 account and provide methods to retrieve account information.

    Attributes:
    -----------
    connection : object
        An instance of the MT5Connection class to manage the connection to the MT5 terminal.

    Methods:
    --------
    get_account_info():
        Retrieves the account information.
    get_margin_level():
        Retrieves the margin level of the account.
    get_balance():
        Retrieves the balance of the account.
    get_equity():
        Retrieves the equity of the account.
    """

    def __init__(self, connection):
        """
        Initializes the MT5Account class with a connection object.

        Parameters:
        -----------
        connection : object
            An instance of the MT5Connection class to manage the connection to the MT5 terminal.
        """
        self.connection = connection

    def get_account_info(self):
        """
        Retrieves the account information.

        Returns:
        --------
        account_info : object or None
            An object containing account information if successful, None otherwise.
        """
        if not self.connection.connected:
            print("MT5 is not initialized")
            return None
        account_info = mt5.account_info()
        if account_info is None:
            print("Failed to get account info:", mt5.last_error())
        return account_info

    def get_margin_level(self):
        """
        Retrieves the margin level of the account.

        Returns:
        --------
        margin_level : float or None
            The margin level of the account if successful, None otherwise.
        """
        account_info = self.get_account_info()
        if account_info is None:
            return None
        return account_info.margin_level

    def get_balance(self):
        """
        Retrieves the balance of the account.

        Returns:
        --------
        balance : float or None
            The balance of the account if successful, None otherwise.
        """
        account_info = self.get_account_info()
        if account_info is None:
            return None
        return account_info.balance

    def get_equity(self):
        """
        Retrieves the equity of the account.

        Returns:
        --------
        equity : float or None
            The equity of the account if successful, None otherwise.
        """
        account_info = self.get_account_info()
        if account_info is None:
            return None
        return account_info.equity
