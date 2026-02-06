import os
from alpaca.data.live import StockDataStream
from datetime import datetime
import pytz

# Read API keys from environment variables
api_key = os.getenv("ALPACA_API_KEY")
secret_key = os.getenv("ALPACA_SECRET_KEY")

# Check if markets are open
def is_market_open():
    ny_tz = pytz.timezone('America/New_York')
    now = datetime.now(ny_tz)
    
    # Check if weekend
    if now.weekday() >= 5:  # Saturday=5, Sunday=6
        return False
    
    # Check if during trading hours (9:30 AM - 4:00 PM EST)
    market_open = now.replace(hour=9, minute=30, second=0)
    market_close = now.replace(hour=16, minute=0, second=0)
    
    return market_open <= now <= market_close

if not is_market_open():
    print("Markets are currently closed. They open Monday-Friday 2:30 PM - 9:00 PM Dublin time (9:30 AM - 4:00 PM New York time / EST).")
    exit()

# Create connection to Alpaca WebSocket
stream = StockDataStream(api_key, secret_key)

# Handler for incoming price data
async def handle_bar(data):
    print(f"Price update: {data.symbol} - ${data.close} at {data.timestamp}")

# Subscribe to SPY (S&P 500 ETF)
stream.subscribe_bars(handle_bar, "SPY")

# Start streaming
print("Connecting to Alpaca market data stream...")
stream.run()
