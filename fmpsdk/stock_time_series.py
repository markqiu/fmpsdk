import typing
import os

from .general import __quotes
from .url_methods import __return_json_v3, __return_json_v4

API_KEY = os.getenv('FMP_API_KEY')

def quote_short(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve a simple, real-time stock quote.

    Provides a quick snapshot of a stock's performance, including current price,
    price change, and trading volume. Useful for rapid market analysis,
    calculating stock valuations, or making quick investment decisions.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: List of dicts with short quote data or None if request fails.
    :example: quote_short('AAPL')
    """
    path = f"quote-short/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def exchange_realtime(exchange: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/ API.

    :param exchange: Exchange symbol.
    :return: A list of dictionaries containing real-time quotes for the exchange.
    :example: exchange_realtime('NASDAQ')
    """
    return __quotes(value=exchange)

def historical_stock_dividend(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve historical dividend payments for a publicly traded company.

    Provides valuable insights for dividend analysis, including payment dates,
    ex-dividend dates, and dividend per share. Useful for analyzing dividend
    history, identifying consistent dividend payers, and tracking dividend growth.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: List of dicts with historical dividend data or None if request fails.
    :example: historical_stock_dividend('AAPL')
    """
    path = f"historical-price-full/stock_dividend/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def historical_stock_split(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve historical stock splits for a publicly traded company.

    Provides information on past stock splits, including the date, split ratio,
    and type of split. Useful for analyzing a company's growth history,
    identifying rapidly growing companies, and understanding stock price trends.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: List of dicts with historical stock split data or None if request fails.
    :example: historical_stock_split('AAPL')
    """
    path = f"historical-price-full/stock_split/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)