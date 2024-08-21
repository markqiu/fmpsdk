import logging
import typing
import os

import requests

from .settings import DEFAULT_LIMIT, SEC_RSS_FEEDS_FILENAME, BASE_URL_v3
from .url_methods import __return_json_v3, __return_json_v4

API_KEY = os.getenv('FMP_API_KEY')

def institutional_holders(
    symbol: str
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve institutional holders for a specific company.

    Provides information on major institutional investors holding the company's stock.
    Useful for understanding institutional ownership and potential market influences.

    :param symbol: Company ticker symbol (e.g., 'AAPL').
    :return: List of dicts with institutional holder data or None if request fails.
    :example: institutional_holders('AAPL')
    """
    path = f"institutional-holder/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def mutual_fund_holders(
    symbol: str
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve mutual fund holders for a specific company.

    Provides information on mutual funds holding the company's stock.
    Useful for understanding mutual fund ownership and investment trends.

    :param symbol: Company ticker symbol (e.g., 'AAPL').
    :return: List of dicts with mutual fund holder data or None if request fails.
    :example: mutual_fund_holders('AAPL')
    """
    path = f"mutual-fund-holder/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def etf_holders(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve ETF holders for a specific company.

    Provides information on ETFs holding the company's stock.
    Useful for understanding ETF ownership and potential market impacts.

    :param symbol: Company ticker symbol (e.g., 'AAPL').
    :return: List of dicts with ETF holder data or None if request fails.
    :example: etf_holders('AAPL')
    """
    path = f"etf-holder/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def etf_sector_weightings(
    symbol: str
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve sector weightings for a specific ETF.

    Provides a breakdown of the percentage of an ETF's assets invested in each sector.
    Useful for understanding ETF risk profiles, sector exposure, and portfolio diversification.

    :param symbol: ETF ticker symbol (e.g., 'SPY').
    :return: List of dicts with sector weighting data or None if request fails.
    :example: etf_sector_weightings('SPY')
    """
    path = f"etf-sector-weightings/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def etf_country_weightings(
    symbol: str
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve country weightings for a specific ETF.

    Provides a breakdown of the percentage of an ETF's assets invested in each country.
    Useful for understanding geographic exposure, identifying country-specific
    investment opportunities, and diversifying portfolios.

    :param symbol: ETF ticker symbol (e.g., 'QDVE.DE').
    :return: List of dicts with country weighting data or None if request fails.
    :example: etf_country_weightings('QDVE.DE')
    """
    path = f"etf-country-weightings/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def sec_rss_feeds(
    limit: int = DEFAULT_LIMIT,
    download: bool = False,
    filename: str = SEC_RSS_FEEDS_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP /rss_feed/ API.

    :param limit: Number of rows to return.
    :param download: True/False
    :param filename: Name of saved file.
    :return: A list of dictionaries.
    """
    path = f"rss_feed"
    query_vars = {"apikey": API_KEY}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving SEC RSS Feeds as {filename}.")
    else:
        query_vars["limit"] = limit
        return __return_json_v3(path=path, query_vars=query_vars)


def cik_list() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /cik_list/ API.

    Complete list of all institutional investment managers by cik
    :return: A list of dictionaries.
    """
    path = f"cik_list"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def cik_search(name: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /cik-search/ API.

    FORM 13F cik search by name
    :param name: Name
    :return: A list of dictionaries.
    """
    path = f"cik-search/{name}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def cik(cik_id: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /cik/ API.

    FORM 13F get company name by cik
    :param cik_id: CIK value
    :return: A list of dictionaries.
    """
    path = f"cik/{cik_id}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def form_13f(
    cik_id: str, date: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /form-thirteen/ API.

    FORM 13F statements provides position-level report of all institutional investment managers with more than $100m
    in assets under management.
    :param cik_id: CIK value
    :param date: 'YYYY-MM-DD'
    :return: A list of dictionaries.
    """
    path = f"form-thirteen/{cik_id}"
    query_vars = {"apikey": API_KEY}
    if date:
        query_vars["date"] = date
    return __return_json_v3(path=path, query_vars=query_vars)


def cusip(cik_id: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /cusip/ API.

    Cusip mapper
    :param cik_id: CIK value
    :return: A list of dictionaries.
    """
    path = f"cusip/{cik_id}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def institutional_symbol_ownership(
    symbol: str,
    limit: int,
    includeCurrentQuarter: bool = False,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /institutional-ownership/symbol-ownership API.

    :param symbol: Company ticker.
    :param limit: up to how many quarterly reports to return.
    :param includeCurrentQuarter: Whether to include any available data in the current quarter.
    :return: A list of dictionaries.
    """
    path = f"institutional-ownership/symbol-ownership"
    query_vars = {
        "symbol": symbol,
        "apikey": API_KEY,
        "includeCurrentQuarter": includeCurrentQuarter,
        "limit": limit,
    }
    return __return_json_v4(path=path, query_vars=query_vars)