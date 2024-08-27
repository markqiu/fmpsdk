import typing
import os
from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3, __return_json_v4, __validate_period
from .data_compression import compress_json_to_tuples

API_KEY = os.getenv('FMP_API_KEY')

def discounted_cash_flow(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve discounted cash flow (DCF) valuation data for a company.

    Provides a method to estimate a company's intrinsic value based on
    future cash flows. Useful for identifying potential undervalued or
    overvalued companies.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: List of dicts with DCF valuation data or None if request fails.
    :example: discounted_cash_flow('AAPL')
    """
    path = f"discounted-cash-flow/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def advanced_discounted_cash_flow(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve advanced discounted cash flow (DCF) valuation data for a company.

    Provides a more detailed method to estimate a company's intrinsic value
    based on future cash flows. Useful for identifying potential undervalued
    or overvalued companies.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: List of dicts with advanced DCF valuation data or None if request fails.
    :example: advanced_discounted_cash_flow('AAPL')
    """
    path = f"advanced_discounted_cash_flow"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def historical_daily_discounted_cash_flow(symbol: str, limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve daily historical discounted cash flow (DCF) valuation data for a company.

    Provides a method to analyze a company's historical intrinsic value
    based on daily cash flows. Useful for identifying trends and patterns
    in a company's valuation over time.

    :param symbol: Company ticker.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :return: List of dicts with daily historical DCF valuation data or None if request fails.
    :example: historical_daily_discounted_cash_flow('AAPL', limit=5)
    """
    path = f"historical-daily-discounted-cash-flow/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)

def market_capitalization(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve a company's current market capitalization.

    Provides the total value of a company's outstanding shares. Useful for
    identifying large-cap, mid-cap, or small-cap companies.

    :param symbol: Company ticker.
    :return: List of dicts with market capitalization data or None if request fails.
    :example: market_capitalization('AAPL')
    """
    path = f"market-capitalization/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def historical_market_capitalization(symbol: str, limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve historical market capitalization data for a company.

    Provides up to five years of data to analyze growth trajectory and
    performance trends. Useful for tracking company growth over time and
    identifying potential underperformance relative to the market.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :return: List of dicts with historical market cap data or None if request fails.
    :example: historical_market_capitalization('AAPL', limit=100)
    """
    path = f"historical-market-capitalization/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)

def discounted_cash_flow(
    symbol: str,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Retrieve the discounted cash flow (DCF) valuation for a company.

    Provides a valuation estimate based on future cash flows and a discount rate.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param condensed: If True, return compact tuple format. Defaults to True.
    :return: List of dicts or tuple of tuples with DCF valuation data.
    :example: discounted_cash_flow('AAPL')
    """
    path = f"discounted-cash-flow/{symbol}"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)


def advanced_discounted_cash_flow(
    symbol: str,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Retrieve advanced DCF valuation data for a company.

    Provides a more comprehensive valuation estimate based on various factors.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param condensed: If True, return compact tuple format. Defaults to True.
    :return: List of dicts or tuple of tuples with advanced DCF valuation data.
    :example: advanced_discounted_cash_flow('AAPL')
    """
    path = f"advanced_discounted_cash_flow"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    result = __return_json_v4(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)


def historical_daily_discounted_cash_flow(
    symbol: str,
    limit: int = DEFAULT_LIMIT,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Retrieve daily historical DCF valuation data for a company.

    Provides insights into a company's daily DCF valuations and trends.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :param condensed: If True, return compact tuple format. Defaults to True.
    :return: List of dicts or tuple of tuples with daily historical DCF data.
    :example: historical_daily_discounted_cash_flow('AAPL', limit=5)
    """
    path = f"historical-daily-discounted-cash-flow/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)

