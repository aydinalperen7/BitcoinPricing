# BitcoinPricing

This repository is dedicated to the collection and analysis of Bitcoin pricing data for the purpose of machine learning and price prediction. The data is sourced from two primary resources: [TradingView](https://www.tradingview.com/) and [CoinMarketCap](https://coinmarketcap.com/).

## Data Collection

Data collection is achieved through a combination of web scraping and API calls. 

- For TradingView, we employ web scraping techniques to gather the necessary data.
- For CoinMarketCap, we utilize their API to access the required information.

The collected data is then stored in a JSON file, providing a structured and easily accessible format for further use.

## Usage

This project is designed to run continuously on a server, allowing for the constant collection and updating of data. This makes it ideal for training machine learning models that require up-to-date information.

To start collecting data in your own local environment, you will need to obtain your own API key from CoinMarketCap.

## Future Work

While the current focus is on data collection, future updates will include the implementation of machine learning models for Bitcoin price prediction. 

## Performance

Please note that there may be room for performance optimization in the current codebase. While we have not yet focused on this aspect, removing unnecessary clutter could potentially improve overall performance.

## Contribution

This project can be expanded to collect more data from a larger variety of resources. We welcome contributions that help in expanding the scope of data collection or in improving the efficiency of the existing codebase.

Stay tuned for more updates on this project!