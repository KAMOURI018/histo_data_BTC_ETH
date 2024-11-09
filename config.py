# config.py

# MongoDB connection URI
MONGO_URI = "mongodb://localhost:27017/"

# Name of the MongoDB database
DATABASE_NAME = "crypto_data"

# Name of the MongoDB collection where historical data will be stored
COLLECTION_NAME = "historical_data"

# TWS API configurations for connecting to the Interactive Brokers platform
TWS_HOST = "127.0.0.1"  # Replace with actual host if different
TWS_PORT = 7497         # Port for TWS API (7497 for paper trading, 4001 for live trading)
TWS_CLIENT_ID = 1       # Unique client ID for TWS connection
