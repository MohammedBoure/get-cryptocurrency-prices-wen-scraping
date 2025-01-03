# Cryptocurrency Price Fetcher

This script is designed to fetch the current prices of cryptocurrencies from [CoinMarketCap](https://coinmarketcap.com).

## Installation

To install this library, run the following command:

```bash
pip install git+https://github.com/MohammedBoure/get-cryptocurrency-prices-wen-scraping.git
```

Ensure you have a working Python environment and `pip` installed before executing the command.

## Description

The library provides a simple API to fetch cryptocurrency prices. The primary function `PriceFlow.fetch_rates()` allows you to retrieve the prices of all available cryptocurrencies or specific ones by passing their symbols.

### Features
- Fetch real-time cryptocurrency prices.
- Retrieve prices for all cryptocurrencies at once or for specific symbols.

### Usage

#### Fetch rates for all cryptocurrencies

You can fetch the prices of all available cryptocurrencies using the following code:

```python
import PriceFlow
PriceFlow.fetch_rates("ALL")
```

Example output:

```python
{
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
    'PEPU': 0.010985799597800246
}
```

#### Fetch rates for specific cryptocurrencies

To fetch the price of a specific cryptocurrency, pass its symbol as an argument:

```python
PriceFlow.fetch_rates("BTC")
```

Example output:

```python
97187.99576969755
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

If you’d like to contribute to this project, feel free to fork the repository and submit a pull request. Contributions are always welcome!

