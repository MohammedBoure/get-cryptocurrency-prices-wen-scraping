# Cryptocurrency Price Fetcher

This script is used to get the current prices of cryptocurrencies from the website [CoinMarketCap](https://coinmarketcap.com).

## Description

The `PriceFlow.fetch_rates()` function fetches the current prices of various cryptocurrencies. You can use it to get the prices for all available cryptocurrencies, or you can specify individual cryptocurrencies.

### Usage

- **Fetch rates for all cryptocurrencies**:
  ```python

    PriceFlow.fetch_rates("ALL") #==>
    """{
            'BTC': 97464.9355661884, 
            'SOL': 208.1784786823789, 
            'ETH': 3481.4720216113105, 
            'DOGE': 0.33924587405640866, 
            'ADA': 0.9612922716514437, 
            'AIC': 0.11036414449324485, 
            'MYSTERY': 2.0755174599986863e-08, 
            'EGO': 0.01681662711432389, 
            'GOAT': 0.0022834497172278274, 
            'SEN': 0.34426732369227026, 
            'XRP': 2.4055545818731288, 
            'HUND': 0.015414844831137198, 
            'KEKIUS': 0.0007084154141021092, 
            'XLM': 0.43093308850030937, 
            'PEPE': 2.060636761521872e-05, 
            'PI': 49.85667416582935, 
            'SHIB': 2.281007479266283e-05, 
            'VIRTUAL': 4.608674078321856, 
            'HBAR': 0.29309682104105017, 
            'PEPU': 0.010985799597800246}"""
    
    PriceFlow.fetch_rates("BTC")# ==> 97187.99576969755

