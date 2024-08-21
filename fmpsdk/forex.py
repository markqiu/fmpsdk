import typing
import os

from .general import __quotes
from .url_methods import __return_json_v3

API_KEY = os.getenv('FMP_API_KEY')

def forex() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Get real-time forex prices for all currency pairs.

    Retrieves a list of current exchange rates for all available forex pairs.
    Useful for getting an overview of the forex market or tracking multiple
    currency pairs simultaneously.

    :return: List of dicts with forex prices or None if request fails.
    :example: forex()
    """
    path = "fx"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def forex_list() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Get a full quote list for all forex currency pairs.

    Provides comprehensive quote information for all available forex pairs,
    including current rates, daily highs/lows, and trading volumes.

    :return: List of dicts with full forex quotes or None if request fails.
    :example: forex_list()
    """
    path = "quotes/forex"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def available_forex() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Get a list of all available forex currency pairs.

    Retrieves a comprehensive list of all currency pairs traded on the
    forex market. Useful for identifying available trading options.

    :return: List of dicts with available forex pairs or None if request fails.
    :example: available_forex()
    """
    path = "symbol/available-forex-currency-pairs"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def forex_quote(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Get a full quote for a specific forex currency pair.

    Retrieves detailed quote information for a single currency pair,
    including current exchange rate, daily high/low, open rates,
    spread, and trading volume.

    :param symbol: Currency pair symbol (e.g., 'EURUSD').
    :return: List with a single dict containing full quote info or None if request fails.
    :example: forex_quote('EURUSD')
    """
    path = f"quote/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def forex_historical(symbol: str, from_date: str, to_date: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Get historical daily price data for a specific forex currency pair.

    Retrieves historical exchange rates and related data for a currency pair
    within a specified date range. Useful for analyzing forex trends and
    performing historical analysis.

    :param symbol: Currency pair symbol (e.g., 'EURUSD').
    :param from_date: Start date in 'YYYY-MM-DD' format.
    :param to_date: End date in 'YYYY-MM-DD' format.
    :return: List of dicts with historical forex data or None if request fails.
    :example: forex_historical('EURUSD', '2023-01-01', '2023-12-31')
    """
    path = f"historical-price-full/{symbol}"
    query_vars = {"apikey": API_KEY, "from": from_date, "to": to_date}
    return __return_json_v3(path=path, query_vars=query_vars)