# utils/tws_client.py

# Import necessary modules from ib_insync and datetime
from ib_insync import IB, Contract
import datetime

class TWSClient:
    """
    TWSClient is a wrapper around the Interactive Brokers TWS API
    to retrieve historical data for cryptocurrencies.
    """

    def __init__(self, host, port, client_id):
        """
        Initialize TWSClient with connection details.

        :param host: IP address or hostname of TWS server
        :param port: Port number for TWS connection
        :param client_id: Unique client ID to maintain connection session
        """
        self.ib = IB()  # Initialize IB instance for TWS connection
        self.ib.connect(host, port, client_id)  # Connect to TWS with given parameters

    def get_historical_data(self, symbol, timeframe, duration):
        """
        Retrieve historical data for a given symbol and timeframe.

        :param symbol: Cryptocurrency symbol (e.g., BTC, ETH)
        :param timeframe: Data interval (e.g., 1 sec, 1 min, etc.)
        :param duration: Duration of data to retrieve (e.g., 1 M for 1 month)
        :return: List of bars containing historical data
        """
        # Define contract for cryptocurrency symbol on the PAXOS exchange
        contract = Contract(symbol=symbol, secType="CRYPTO", exchange="PAXOS", currency="USD")
        
        # Set the end datetime to current (empty string for current date/time)
        end_datetime = ""

        # Request historical data from TWS
        bars = self.ib.reqHistoricalData(
            contract,                     # Contract object for the symbol
            endDateTime=end_datetime,     # End time for data retrieval (now)
            durationStr=duration,         # Duration (e.g., "1 M")
            barSizeSetting=timeframe,     # Bar size (e.g., "1 min")
            whatToShow="MIDPOINT",        # Data type (e.g., "MIDPOINT")
            useRTH=True,                  # Use regular trading hours
            formatDate=1                  # Date format
        )
        
        return bars  # Return list of historical bars
