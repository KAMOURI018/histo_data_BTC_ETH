# data_collector.py

# Import MongoDB client, custom TWSClient, and configuration settings
from pymongo import MongoClient
from utils.tws_client import TWSClient
from datetime import datetime, date  # Import both datetime and date types
import config

def store_data_in_mongodb(data, collection, symbol, timeframe):
    """
    Store historical data in MongoDB.

    :param data: List of historical bars from TWS API
    :param collection: MongoDB collection where data will be stored
    :param symbol: The symbol of the cryptocurrency (e.g., BTC, ETH)
    :param timeframe: The timeframe for the data (e.g., "1 hour")
    """
    # Iterate through each data entry and store it in MongoDB
    for entry in data:
        # Convert date to datetime if it's a date object (not datetime)
        entry_date = entry.date
        if isinstance(entry_date, date) and not isinstance(entry_date, datetime):
            entry_date = datetime.combine(entry_date, datetime.min.time())
        
        # Create a dictionary for the current data entry
        record = {
            "symbol": symbol,            # Set cryptocurrency symbol
            "date": entry_date,          # Store date as datetime
            "open": entry.open,          # Open price
            "high": entry.high,          # High price
            "low": entry.low,            # Low price
            "close": entry.close,        # Close price
            "volume": entry.volume,      # Trade volume
            "timeframe": timeframe       # Store timeframe
        }
        # Insert the record into the MongoDB collection
        collection.insert_one(record)

def main():
    """
    Main function to pull historical data from TWS API and store it in MongoDB.
    """
    # Set up MongoDB client and select database and collection
    mongo_client = MongoClient(config.MONGO_URI)
    db = mongo_client[config.DATABASE_NAME]
    collection = db[config.COLLECTION_NAME]
    
    # Clear the collection before inserting new data
    collection.delete_many({})  # This removes all documents in the collection

    # Initialize TWSClient to connect to TWS API
    tws_client = TWSClient(config.TWS_HOST, config.TWS_PORT, config.TWS_CLIENT_ID)

    # Define the cryptocurrencies and timeframes for data retrieval
    symbols = ["BTC", "ETH"]              # Symbols for Bitcoin and Ethereum
    timeframes = ["1 min"]      # Different data intervals
    duration = "1 D"                      # Duration for data retrieval (1 month)

    # Loop through each symbol and timeframe to retrieve and store data
    for symbol in symbols:
        for timeframe in timeframes:
            # Retrieve historical data for the current symbol and timeframe
            data = tws_client.get_historical_data(symbol, timeframe, duration)
            
            # Store retrieved data in MongoDB
            store_data_in_mongodb(data, collection, symbol, timeframe)

if __name__ == "__main__":
    main()  # Run main function if script is executed directly
