import typing
import os

from .settings import DEFAULT_LINE_PARAMETER
from .url_methods import (
    __return_json_v3,
    __return_json_v4,
    __validate_series_type,
    __validate_time_delta,
)

API_KEY = os.getenv('FMP_API_KEY')

def __quotes(value: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/ API.

    :param value: The Ticker(s), Index(es), Commodity(ies), etc. symbol to query for.
    :return: A list of dictionaries containing quote data.
    :example: __quotes('AAPL')
    """
    path = f"quotes/{value}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def quote(
    symbol: typing.Union[str, typing.List[str]]
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve real-time full quote data for one or multiple stocks.

    Provides the latest bid and ask prices, volume, and last trade price.
    Useful for getting a real-time snapshot of stock performance and
    making informed investment decisions.

    :param symbol: Ticker symbol(s) (e.g., 'AAPL' or ['AAPL', 'GOOGL']).
    :return: List of dicts with full quote data or None if request fails.
    :example: quote('AAPL')
    :example: quote(['AAPL', 'GOOGL'])
    """
    if type(symbol) is list:
        symbol = ",".join(symbol)
    path = f"quote/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def historical_chart(
    symbol: str,
    timeframe: str,
    from_date: str,
    to_date: str,
    time_series: str = DEFAULT_LINE_PARAMETER,
    time_delta: str = None,  # For backward compatibility
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve historical price data for a specific stock or financial instrument.

    Provides intraday or daily historical price data for analysis and charting.
    Useful for technical analysis, trend identification, and backtesting strategies.

    :param symbol: The Ticker, Index, Commodity, etc. symbol to query for (e.g., 'AAPL').
    :param timeframe: Time interval ('1min', '5min', '15min', '30min', '1hour', '4hour', '1day').
    :param from_date: Start date in 'YYYY-MM-DD' format.
    :param to_date: End date in 'YYYY-MM-DD' format.
    :param time_series: Time series parameter, default is 'line'.
    :param time_delta: Deprecated. Use 'timeframe' instead.
    :return: List of dicts with historical price data or None if request fails.
    :example: historical_chart('AAPL', '1day', '2023-08-10', '2023-09-10')
    """
    if time_delta is not None:
        timeframe = time_delta  # For backward compatibility

    path = f"historical-chart/{__validate_time_delta(timeframe)}/{symbol}"
    query_vars = {"apikey": API_KEY}
    if time_series:
        query_vars["timeseries"] = time_series
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v3(path=path, query_vars=query_vars)


def historical_price_full(
    symbol: typing.Union[str, typing.List],
    from_date: str = None,
    to_date: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve daily historical price data for a stock or list of stocks.

    Provides up to 5 years of daily stock data by default, including open, high,
    low, and closing prices. Useful for trend analysis and charting.

    :param symbol: Ticker symbol(s) (e.g., 'AAPL' or ['AAPL', 'GOOGL']).
    :param from_date: Start date in 'YYYY-MM-DD' format.
    :param to_date: End date in 'YYYY-MM-DD' format.
    :return: List of dicts with historical price data or None if request fails.
    :example: historical_price_full('AAPL', '2023-01-01', '2023-12-31')

    Note: Use from_date and to_date for custom ranges, each limited to 5 years.
    """
    if type(symbol) is list:
        symbol = ",".join(symbol)
    path = f"historical-price-full/{symbol}"
    query_vars = {"apikey": API_KEY}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date

    res = __return_json_v3(path=path, query_vars=query_vars)
    if res:
        return res.get("historicalStockList", res.get("historical", None))
    else:
        return res