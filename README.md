# Low-Latency Trading System, what it does?

I deployed a high-performance VM as close as I can to the NYSE.

The physical proximity is what makes my ping faster than yours if you are not in US east.

I have high computing power in my VM that is useful for intensive backtesting (tbd)

## Latency Results (pings, trade algos to be implemented in another project)
- **Dublin → S&P data**: 81ms average
- **East US VM → S&P data**: 6ms average  
- **Improvement**: 92% latency reduction

## Infrastructure 
![Built in Azure](./assets/infra.png)

Can you be faster than me? :) --> if you want to try:

# Setup

0. go to Alpaca, create account, get API keys for paper trading from your dashboard
1. clone repo in VS code
2. in VS terminal bash: pip install -r requirements.txt
3. in VS terminal bash:
   $env:ALPACA_API_KEY="your-key-here"
   $env:ALPACA_SECRET_KEY="your-secret-here"
5. go
   
##Prerequisits:
- Python 3.12+
- Azure account (for VM deployment)
- Alpaca Markets account (free paper trading account)

