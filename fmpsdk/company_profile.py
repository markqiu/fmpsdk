import typing
import os
from .url_methods import __return_json_v3

API_KEY = os.getenv('FMP_API_KEY')

def company_profile(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve a comprehensive overview of a company.

    Provides key information such as price, beta, market capitalization,
    description, headquarters, industry, sector, CEO, website, and more.
    Useful for identifying investment opportunities, tracking performance,
    and conducting competitive research.

    :param symbol: Ticker symbol of the company (e.g., 'AAPL').
    :return: List of dicts with company profile data or None if request fails.
    :example: company_profile('AAPL')
    """
    path = f"profile/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def key_executives(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve standardized data for key executives from SEC filings.

    Useful for analyzing corporate governance, executive incentives, and 
    comparing compensation across companies.

    :param symbol: Ticker symbol of the company (e.g., 'AAPL').
    :return: List of dicts with key executives data or None if request fails.
    :example: key_executives('AAPL')
    """
    path = f"key-executives/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)