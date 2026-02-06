# Low-Latency Trading System

Market data ingestion system optimized for latency through geographic deployment.

## Architecture
- **VM Location**: Azure East US
- **Target**: Alpaca Markets API
- **Language**: Python 3.12

## Latency Results
- **Dublin → Alpaca**: 81ms average
- **East US VM → Alpaca**: 6ms average  
- **Improvement**: 92% latency reduction

## Setup
```bash
pip install -r requirements.txt
export ALPACA_API_KEY="your-key"
export ALPACA_SECRET_KEY="your-secret"
python dataFetcher.py
```
