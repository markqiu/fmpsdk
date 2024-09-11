"""
   https://site.financialmodelingprep.com/developer/docs#share-float
"""

import typing
import os
from .url_methods import __return_json_v4
from .data_compression import format_output

API_KEY = os.getenv('FMP_API_KEY')

def shares_float(
    symbol: str,
    all: bool = False,
    output: str = 'markdown'
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Query FMP /shares_float/ API.

    Provides the total number of shares that are publicly traded for a given company.
    :param symbol: Ticker of Company.
    :param all: Optional boolean attribute. If True, changes the API url to the "all" endpoint.
    :param output: Output format ('tsv', 'json', or 'markdown'). Defaults to 'markdown'.
    :return: List of dicts or formatted string with shares float data.
    """
    if all:
        path = "shares_float/all"
    else:
        path = f"shares_float?symbol={symbol}"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v4(path=path, query_vars=query_vars)
    return format_output(result, output)

def historical_share_float(
    symbol: str,
    output: str = 'markdown'
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Query FMP /historical/shares_float API.

    Get historical data on the number of shares that are publicly traded for a given company.
    
    :param symbol: Ticker symbol of the company.
    :param output: Output format ('tsv', 'json', or 'markdown'). Defaults to 'markdown'.
    :return: List of dicts or formatted string with historical share float data.
    :example: historical_share_float('AAPL', output='markdown')
    """
    path = "historical/shares_float"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    result = __return_json_v4(path=path, query_vars=query_vars)
    return format_output(result, output)