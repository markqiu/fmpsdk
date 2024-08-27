import typing
import os
from .url_methods import __return_json_v4
from .data_compression import compress_json_to_tuples

API_KEY = os.getenv('FMP_API_KEY')


def price_targets(
    symbol: str,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Retrieve price targets for a company's stock.

    Provides analyst-estimated fair value prices, useful for investment
    decisions. Includes target price, analyst name, and publication date.

    :param symbol: Stock symbol (e.g., 'AAPL')
    :param condensed: If True, return data as a tuple of tuples. Defaults to True.
    :return: List of dicts or tuple of tuples with price target data
    :example: price_targets('AAPL')
    """
    path = "price-target"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    result = __return_json_v4(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)


def price_target_summary(
    symbol: str,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Retrieve a summary of price targets for a company from various analysts.

    Provides average, high, and low price targets, useful for gauging overall
    analyst sentiment. Includes number of analysts and other relevant metrics.

    :param symbol: Stock symbol (e.g., 'AAPL')
    :param condensed: If True, return data as a tuple of tuples. Defaults to True.
    :return: List of dicts or tuple of tuples with price target summary data
    :example: price_target_summary('AAPL')
    """
    path = "price-target-summary"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    result = __return_json_v4(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)


def price_target_by_analyst_name(
    name: str,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Retrieve price targets from a specific analyst for various companies.

    Useful for tracking price targets of a particular trusted analyst.
    Provides target prices, company symbols, and publication dates.

    :param name: Name of the analyst (e.g., 'Tim Anderson')
    :param condensed: If True, return data as a tuple of tuples. Defaults to True.
    :return: List of dicts or tuple of tuples with price target data
    :example: price_target_by_analyst_name('Tim Anderson')
    """
    path = "price-target-analyst-name"
    query_vars = {"apikey": API_KEY, "name": name}
    result = __return_json_v4(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)


def price_target_by_company(
    company: str,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Retrieve price targets from a specific analyst company for various stocks.

    Useful for comparing price targets across different companies in the same
    industry or sector. Provides target prices, symbols, and analyst details.

    :param company: Name of the analyst company (e.g., 'Barclays')
    :param condensed: If True, return data as a tuple of tuples. Defaults to True.
    :return: List of dicts or tuple of tuples with price target data
    :example: price_target_by_company('Barclays')
    """
    path = "price-target-analyst-company"
    query_vars = {"apikey": API_KEY, "company": company}
    result = __return_json_v4(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)


def price_target_consensus(
    symbol: str,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Retrieve consensus price target for a company's stock.

    Provides the average of all price targets from different analysts,
    offering a general view of market expectations for the stock's value.

    :param symbol: Stock symbol (e.g., 'AAPL')
    :param condensed: If True, return data as a tuple of tuples. Defaults to True.
    :return: List of dicts or tuple of tuples with consensus price target data
    :example: price_target_consensus('AAPL')
    """
    path = "price-target-consensus"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    result = __return_json_v4(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)


def price_target_rss_feed(
    page: int = 0,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Retrieve an RSS feed of price target updates for companies.

    Provides the latest analyst price target updates across various companies.
    Useful for staying informed about recent changes in market expectations.

    :param page: Page number for pagination (default is 0)
    :param condensed: If True, return data as a tuple of tuples. Defaults to True.
    :return: List of dicts or tuple of tuples with price target updates
    :example: price_target_rss_feed(page=1)
    """
    path = "price-target-rss-feed"
    query_vars = {"apikey": API_KEY, "page": page}
    result = __return_json_v4(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)