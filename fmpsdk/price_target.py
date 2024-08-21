import typing
import os
from .url_methods import __return_json_v4

API_KEY = os.getenv('FMP_API_KEY')

def price_targets(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve price targets for a company's stock.

    Provides analyst-estimated fair value prices, useful for investment
    decisions. Includes target price, analyst name, and publication date.

    :param symbol: Stock symbol (e.g., 'AAPL')
    :return: List of dicts with price target data or None if request fails
    :example: price_targets('AAPL')
    """
    path = "price-target"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def price_target_summary(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve a summary of price targets for a company from various analysts.

    Provides average, high, and low price targets, useful for gauging overall
    analyst sentiment. Includes number of analysts and other relevant metrics.

    :param symbol: Stock symbol (e.g., 'AAPL')
    :return: List of dicts with price target summary data or None if request fails
    :example: price_target_summary('AAPL')
    """
    path = "price-target-summary"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def price_target_by_analyst_name(name: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve price targets from a specific analyst for various companies.

    Useful for tracking price targets of a particular trusted analyst.
    Provides target prices, company symbols, and publication dates.

    :param name: Name of the analyst (e.g., 'Tim Anderson')
    :return: List of dicts with price target data or None if request fails
    :example: price_target_by_analyst_name('Tim Anderson')
    """
    path = "price-target-analyst-name"
    query_vars = {"apikey": API_KEY, "name": name}
    return __return_json_v4(path=path, query_vars=query_vars)

def price_target_by_company(company: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve price targets from a specific analyst company for various stocks.

    Useful for comparing price targets across different companies in the same
    industry or sector. Provides target prices, symbols, and analyst details.

    :param company: Name of the analyst company (e.g., 'Barclays')
    :return: List of dicts with price target data or None if request fails
    :example: price_target_by_company('Barclays')
    """
    path = "price-target-analyst-company"
    query_vars = {"apikey": API_KEY, "company": company}
    return __return_json_v4(path=path, query_vars=query_vars)

def price_target_consensus(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve consensus price target for a company's stock.

    Provides the average of all price targets from different analysts,
    offering a general view of market expectations for the stock's value.

    :param symbol: Stock symbol (e.g., 'AAPL')
    :return: List of dicts with consensus price target data or None if request fails
    :example: price_target_consensus('AAPL')
    """
    path = "price-target-consensus"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def price_target_rss_feed(page: int = 0) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve an RSS feed of price target updates for companies.

    Provides the latest analyst price target updates across various companies.
    Useful for staying informed about recent changes in market expectations.

    :param page: Page number for pagination (default is 0)
    :return: List of dicts with price target updates or None if request fails
    :example: price_target_rss_feed(page=1)
    """
    path = "price-target-rss-feed"
    query_vars = {"apikey": API_KEY, "page": page}
    return __return_json_v4(path=path, query_vars=query_vars)