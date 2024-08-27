import typing
import os
from .url_methods import __return_json_v3, __validate_time_delta
from .settings import DEFAULT_LIMIT, DEFAULT_LINE_PARAMETER
from .data_compression import compress_json_to_tuples

API_KEY = os.getenv('FMP_API_KEY')


def exchange_realtime(
    exchange: str,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Query FMP /quotes/ API.

    :param exchange: Exchange symbol.
    :param condensed: If True, return compact tuple format. Defaults to True.
    :return: Real-time quotes for the exchange.
    :example: exchange_realtime('NASDAQ')
    """
    result = __quotes(value=exchange)
    return compress_json_to_tuples(result, condensed)


def cryptocurrency_quote(
    symbol: str,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Query FMP /quote/{symbol} API for cryptocurrency quote

    :param symbol: The symbol of the cryptocurrency (e.g., 'BTCUSD')
    :param condensed: If True, return compact tuple format. Defaults to True.
    :return: Full quote for the specified cryptocurrency.
    :example: cryptocurrency_quote('BTCUSD')
    :endpoint: https://financialmodelingprep.com/api/v3/quote/BTCUSD
    """
    path = f"quote/{symbol}"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)


def commodity_price(
    symbol: str,
    from_date: str = None,
    to_date: str = None,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Query FMP /historical-price-full/{symbol} API for commodity price data

    :param symbol: The symbol of the commodity (e.g., 'ZGUSD')
    :param from_date: Start date in 'YYYY-MM-DD' format (optional)
    :param to_date: End date in 'YYYY-MM-DD' format (optional)
    :param condensed: If True, return compact tuple format. Defaults to True.
    :return: Historical price data for the specified commodity.
    :example: commodity_price('ZGUSD', from_date='2023-01-01', to_date='2023-12-31')
    """
    return historical_price_full(symbol, from_date, to_date, condensed)


def commodities_list(
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Query FMP /quotes/commodity API

    :param condensed: If True, return compact tuple format. Defaults to True.
    :return: Full quotes for all commodities.
    :example: commodities_list()
    """
    path = "quotes/commodity"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)


def mutual_fund_list(
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Query FMP /quotes/mutual_fund/ API

    :param condensed: If True, return compact tuple format. Defaults to True.
    :return: List of mutual funds data.
    """
    path = "quotes/mutual_fund"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)


def quote(
    symbol: typing.Union[str, typing.List[str]],
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Retrieve real-time full quote data for one or multiple stocks.

    Provides the latest bid and ask prices, volume, and last trade price.
    Useful for getting a real-time snapshot of stock performance and
    making informed investment decisions.

    :param symbol: Ticker symbol(s) (e.g., 'AAPL' or ['AAPL', 'GOOGL']).
    :param condensed: If True, return compact tuple format. Defaults to True.
    :return: Full quote data for the specified symbol(s).
    :example: quote('AAPL')
    :example: quote(['AAPL', 'GOOGL'])
    """
    if isinstance(symbol, list):
        symbol = ",".join(symbol)
    path = f"quote/{symbol}"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)


def is_market_open(
    exchange: str = "NASDAQ",
    condensed: bool = True
) -> typing.Union[typing.Dict, typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Check if a specific exchange is currently open or closed.

    Useful for determining market hours and availability of data.

    :param exchange: Exchange name (e.g., 'NASDAQ'). Default is 'NASDAQ'.
    :param condensed: If True, return compact tuple format. Defaults to True.
    :return: Market open/close status for the specified exchange.
    :example: is_market_open('NYSE')
    """
    path = "is-the-market-open"
    query_vars = {"apikey": API_KEY, "exchange": exchange}
    result = __return_json_v3(path=path, query_vars=query_vars)
    
    if result is not None and condensed:
        fields = tuple(result.keys())
        return (fields, tuple(str(result.get(field, '')) for field in fields))
    return result


def tsx_list(
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Query FMP /quotes/tsx/ API

    :return: List of TSX stocks data.
    """
    path = f"tsx"
    return __quotes(value=path)


def forex(
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Get real-time forex prices for all currency pairs.

    Retrieves a list of current exchange rates for all available forex pairs.
    Useful for getting an overview of the forex market or tracking multiple
    currency pairs simultaneously.

    :param condensed: If True, return compact tuple format. Defaults to True.
    :return: Forex prices for all currency pairs.
    :example: forex()
    """
    path = "fx"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)


def forex_list(
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Get a full quote list for all forex currency pairs.

    Provides comprehensive quote information for all available forex pairs,
    including current rates, daily highs/lows, and trading volumes.

    :param condensed: If True, return compact tuple format. Defaults to True.
    :return: Full quotes for all forex currency pairs.
    :example: forex_list()
    """
    path = "quotes/forex"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)


def forex_quote(
    symbol: str,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Get a full quote for a specific forex currency pair.

    Retrieves detailed quote information for a single currency pair,
    including current exchange rate, daily high/low, open rates,
    spread, and trading volume.

    :param symbol: Currency pair symbol (e.g., 'EURUSD').
    :param condensed: If True, return compact tuple format. Defaults to True.
    :return: Full quote for the specified forex currency pair.
    :example: forex_quote('EURUSD')
    """
    path = f"quote/{symbol}"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)


def __quotes(
    value: str,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Query FMP /quotes/ API.

    :param value: The Ticker(s), Index(es), Commodity(ies), etc. symbol to query for.
    :param condensed: If True, return compact tuple format. Defaults to True.
    :return: Quote data for the specified value.
    :example: __quotes('AAPL')
    """
    path = f"quotes/{value}"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)


def historical_chart(
    symbol: str,
    timeframe: str,
    from_date: str,
    to_date: str,
    time_series: str = DEFAULT_LINE_PARAMETER,
    time_delta: str = None,  # For backward compatibility
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Retrieve historical price data for a specific stock or financial instrument.

    :param symbol: The Ticker, Index, Commodity, etc. symbol to query for (e.g., 'AAPL').
    :param timeframe: Time interval ('1min', '5min', '15min', '30min', '1hour', '4hour', '1day').
    :param from_date: Start date in 'YYYY-MM-DD' format.
    :param to_date: End date in 'YYYY-MM-DD' format.
    :param time_series: Time series parameter, default is 'line'.
    :param time_delta: Deprecated. Use 'timeframe' instead.
    :param condensed: If True, return compact tuple format. Defaults to True.
    :return: Historical price data for the specified symbol and timeframe.
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
    
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)


def historical_price_full(
    symbol: typing.Union[str, typing.List],
    from_date: str = None,
    to_date: str = None,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Retrieve daily historical price data for a stock or list of stocks.

    Provides up to 5 years of daily stock data by default, including open, high,
    low, and closing prices. Useful for trend analysis and charting.

    :param symbol: Ticker symbol(s) (e.g., 'AAPL' or ['AAPL', 'GOOGL']).
    :param from_date: Start date in 'YYYY-MM-DD' format.
    :param to_date: End date in 'YYYY-MM-DD' format.
    :param condensed: If True, return data as a tuple of tuples. Defaults to True.
    :return: If condensed, tuple of tuples ((field_names), (data1), (data2), ...).
             Otherwise, list of dicts with historical price data. None if request fails.
    :example: historical_price_full('AAPL', '2023-01-01', '2023-12-31', condensed=True)

    Note: Use from_date and to_date for custom ranges, each limited to 5 years.
    """
    if isinstance(symbol, list):
        symbol = ",".join(symbol)
    path = f"historical-price-full/{symbol}"
    query_vars = {"apikey": API_KEY}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date

    result = __return_json_v3(path=path, query_vars=query_vars)
    
    if result:
        historical_data = result.get("historicalStockList", result.get("historical", None))
        if historical_data:
            return compress_json_to_tuples(historical_data, condensed)
    
    return None


def forex_historical(
    symbol: str,
    from_date: str,
    to_date: str,
    condensed: bool = True
) -> typing.List[typing.Dict]:
    """
    Get historical daily price data for a specific forex currency pair.

    Retrieves historical exchange rates and related data for a currency pair
    within a specified date range. Useful for analyzing forex trends and
    performing historical analysis.

    :param symbol: Currency pair symbol (e.g., 'EURUSD').
    :param from_date: Start date in 'YYYY-MM-DD' format.
    :param to_date: End date in 'YYYY-MM-DD' format.
    :return: Historical forex data for the specified currency pair.
    :example: forex_historical('EURUSD', '2023-01-01', '2023-12-31')
    """
    path = f"historical-price-full/{symbol}"
    query_vars = {"apikey": API_KEY, "from": from_date, "to": to_date}
    return __return_json_v3(path=path, query_vars=query_vars)