# Histo Data BTC/ETH Collector

This project pulls historical data for Bitcoin (BTC) and Ethereum (ETH) from the Interactive Brokers TWS API and stores it in a MongoDB database. The collected data can then be used for analysis, backtesting, or further processing in trading applications.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Data Collection Process](#data-collection-process)

---

## Project Overview

The `Histo Data BTC/ETH Collector` fetches historical data for BTC and ETH across different timeframes (e.g., 1 minute, 1 hour, 1 day) using the TWS API from Interactive Brokers. This data is stored in a MongoDB collection for easy querying and analysis.

## Features

- Retrieve historical data for BTC and ETH with configurable timeframes.
- Store data in a MongoDB collection for analysis and backtesting.
- Clear the MongoDB collection before each run to ensure fresh data.
- Flexible configuration for TWS API and MongoDB settings.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/KAMOURI018/histo_data_BTC_ETH.git
   cd histo_data_BTC_ETH
   ```

2. **Install Required Packages**:

   ```bash
   pip install -r requirements.txt
   ```

   Ensure that the required packages, including `pymongo` and `ib_insync`, are installed.

3. **Install MongoDB** (if not already installed):

   - On Ubuntu, you can install MongoDB by running:
     ```bash
     sudo apt update
     sudo apt install -y mongodb
     ```
   - Start MongoDB:
     ```bash
     sudo systemctl start mongodb
     ```

4. **Install and Configure TWS or IB Gateway**:
   - Download and install TWS or IB Gateway from Interactive Brokers.
   - Open TWS, navigate to **Edit > Global Configuration > API > Settings**, and ensure "Enable ActiveX and Socket Clients" is checked.
   - Set the TWS API socket port (default is `7497` for paper trading).

## Configuration

The configuration settings for MongoDB and TWS API are stored in `config.py`. Update this file to match your environment.

```python
# config.py

# MongoDB Configuration
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "crypto_data"
COLLECTION_NAME = "historical_data"

# TWS API Configuration
TWS_HOST = "127.0.0.1"
TWS_PORT = 7497
TWS_CLIENT_ID = 1
```

- **MONGO_URI**: The connection string for your MongoDB instance.
- **DATABASE_NAME**: The name of the database where data will be stored.
- **COLLECTION_NAME**: The collection within the database for storing historical data.
- **TWS_HOST**: IP address for the TWS API server.
- **TWS_PORT**: Port number for the TWS API (default is `7497`).
- **TWS_CLIENT_ID**: Unique client ID to identify the connection.

## Usage

1. **Run the Data Collection Script**:
   The `data_collector.py` script clears the existing MongoDB collection and collects historical data for BTC and ETH with the configured timeframes.

   ```bash
   python data_collector.py
   ```

2. **Verify Data in MongoDB**:
   You can view the collected data by connecting to MongoDB with MongoDB Compass, `mongosh`, or a Python script.

### Example: View Data with `mongosh`

```bash
mongosh
use crypto_data
db.historical_data.find().pretty()
```

## File Structure

```
histo_data_BTC_ETH/
├── data_collector.py       # Main script to collect and store data
├── config.py               # Configuration file for MongoDB and TWS API settings
├── requirements.txt        # List of Python dependencies
└── utils/
    ├── __init__.py         # Init file for utils module
    └── tws_client.py       # Wrapper for TWS API connection and data retrieval
```

## Data Collection Process

1. **Initialize MongoDB and TWS Connection**:

   - The `main()` function in `data_collector.py` sets up a MongoDB client and TWS API client.

2. **Clear Existing Data**:

   - The `collection.delete_many({})` command clears the `historical_data` collection in MongoDB at the start of each run.

3. **Retrieve Data**:

   - The `get_historical_data()` function retrieves data for BTC and ETH across the configured timeframes and duration (e.g., `1 min`, `1 hour`, `1 day`, with `1 M` duration).

4. **Store Data**:
   - The `store_data_in_mongodb()` function converts the data to a suitable format and stores it in MongoDB.

---


