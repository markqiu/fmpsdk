import typing
import os
from .url_methods import __return_json_v4
from .data_compression import compress_json_to_tuples

# Read API key from environment variable
API_KEY = os.environ.get('FMP_API_KEY')

def commitment_of_traders_report_list(
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Query FMP /commitment_of_traders_report/list API.

    List of symbols for COT.
    :param condensed: If True, return data as a tuple of tuples. Defaults to True.
    :return: List of dictionaries or tuple of tuples if condensed.
    :example: commitment_of_traders_report_list()
    :endpoint: https://financialmodelingprep.com/api/v4/commitment_of_traders_report/list
    """
    path = "commitment_of_traders_report/list"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v4(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)

def commitment_of_traders_report(
    symbol: str,
    from_date: str = None,
    to_date: str = None,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Query FMP /commitment_of_traders_report API.

    The CFTC publishes COT reports to help understand market dynamics.
    :param symbol: COT symbol (required).
    :param from_date: Optional. Start date in YYYY-MM-DD format.
    :param to_date: Optional. End date in YYYY-MM-DD format.
    :param condensed: If True, return data as a tuple of tuples. Defaults to True.
    :return: List of dictionaries or tuple of tuples if condensed.
    :example: commitment_of_traders_report('COT_SYMBOL', '2023-01-01', '2023-12-31')
    """
    path = f"commitment_of_traders_report/{symbol}"
    query_vars = {"apikey": API_KEY}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    result = __return_json_v4(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)

def commitment_of_traders_report_analysis(
    symbol: str,
    from_date: str,
    to_date: str,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Query FMP /commitment_of_traders_report_analysis API.

    Analysis of reports for time period or symbol.
    :param symbol: Trading symbol.
    :param from_date: YYYY-MM-DD string.
    :param to_date: YYYY-MM-DD string.
    :param condensed: If True, return data as a tuple of tuples. Defaults to True.
    :return: List of dictionaries or tuple of tuples if condensed.
    :example: commitment_of_traders_report_analysis('AAPL', '2023-01-01', '2023-12-31')
    """
    path = f"commitment_of_traders_report_analysis"
    query_vars = {"apikey": API_KEY}
    if symbol:
        path = f"{path}/{symbol}"
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    result = __return_json_v4(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)