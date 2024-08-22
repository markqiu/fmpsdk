import logging
import typing
import os

import requests

from .general import __quotes
from .settings import (
    DOWJONES_CONSTITUENTS_FILENAME,
    NASDAQ_CONSTITUENTS_FILENAME,
    SP500_CONSTITUENTS_FILENAME,
    BASE_URL_v3,
)
from .url_methods import __return_json_v3
from .data_compression import compress_json_to_tuples

API_KEY = os.getenv('FMP_API_KEY')


def indexes(
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Query FMP /quotes/index API for major stock market indices.

    Retrieves a list of all major stock market indices, such as the S&P 500, 
    the Dow Jones Industrial Average, and the Nasdaq Composite Index and 
    returns their performance.

    :param condensed: If True, return data as a tuple of tuples. Defaults to True.
    :return: If condensed, tuple of tuples ((field_names), (index1_data), (index2_data), ...).
             Otherwise, list of dictionaries containing index data. None if request fails.
    :example: indexes(condensed=True)
    """
    path = "quotes/index"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    
    return compress_json_to_tuples(result, condensed)


def sp500_constituent(
    download: bool = False,
    filename: str = SP500_CONSTITUENTS_FILENAME,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...], None]:
    """
    Query FMP /sp500_constituent/ API

    :param download: True/False
    :param filename: Name of saved file.
    :param condensed: If True, return data as a tuple of tuples. Defaults to True.
    :return: A list of dictionaries or tuple of tuples if condensed.
    """
    path = f"sp500_constituent"
    query_vars = {"apikey": API_KEY}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving SP500 Constituents as {filename}.")
        return None
    else:
        result = __return_json_v3(path=path, query_vars=query_vars)
        return compress_json_to_tuples(result, condensed)


def historical_sp500_constituent(
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...], None]:
    """
    Query FMP /historical/sp500_constituent/ API.

    :param condensed: If True, return data as a tuple of tuples. Defaults to True.
    :return: A list of dictionaries or tuple of tuples if condensed.
    """
    path = f"historical/sp500_constituent"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)


def nasdaq_constituent(
    download: bool = False,
    filename: str = NASDAQ_CONSTITUENTS_FILENAME,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...], None]:
    """
    Query FMP /nasdaq_constituent/ API

    :param download: True/False
    :param filename: Name of saved file.
    :param condensed: If True, return data as a tuple of tuples. Defaults to True.
    :return: A list of dictionaries or tuple of tuples if condensed.
    """
    path = f"nasdaq_constituent"
    query_vars = {"apikey": API_KEY}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving NASDAQ Constituents as {filename}.")
        return None
    else:
        result = __return_json_v3(path=path, query_vars=query_vars)
        return compress_json_to_tuples(result, condensed)


def historical_nasdaq_constituent(
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...], None]:
    """
    Query FMP /historical/nasdaq_constituent/ API.

    :param condensed: If True, return data as a tuple of tuples. Defaults to True.
    :return: A list of dictionaries or tuple of tuples if condensed.
    """
    path = f"historical/nasdaq_constituent"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)


def dowjones_constituent(
    download: bool = False,
    filename: str = DOWJONES_CONSTITUENTS_FILENAME,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...], None]:
    """
    Query FMP /dowjones_constituent/ API

    :param download: True/False
    :param filename: Name of saved file.
    :param condensed: If True, return data as a tuple of tuples. Defaults to True.
    :return: A list of dictionaries or tuple of tuples if condensed.
    """
    path = f"dowjones_constituent"
    query_vars = {"apikey": API_KEY}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving DOWJONES Constituents as {filename}.")
        return None
    else:
        result = __return_json_v3(path=path, query_vars=query_vars)
        return compress_json_to_tuples(result, condensed)


def historical_dowjones_constituent(
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...], None]:
    """
    Query FMP /historical/dowjones_constituent/ API.

    :param condensed: If True, return data as a tuple of tuples. Defaults to True.
    :return: A list of dictionaries or tuple of tuples if condensed.
    """
    path = f"historical/dowjones_constituent"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)


def available_indexes(
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...], None]:
    """
    Query FMP /symbol/available-indexes/ API

    :param condensed: If True, return data as a tuple of tuples. Defaults to True.
    :return: A list of dictionaries or tuple of tuples if condensed.
    """
    path = f"symbol/available-indexes"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)