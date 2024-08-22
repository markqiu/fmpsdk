import typing
import os
from .url_methods import __return_json_v3
from .general import historical_price_full

API_KEY = os.getenv('FMP_API_KEY')

def available_commodities() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /symbol/available-commodities API

    :return: A list of dictionaries containing available commodities.
    :example: available_commodities()
    """
    path = "symbol/available-commodities"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def commodities_list() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /quotes/commodity API

    :return: A list of dictionaries containing full quotes for all commodities.
    :example: commodities_list()
    """
    path = "quotes/commodity"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

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
    :param condensed: If True, return data as a tuple of tuples. Defaults to True.
    :return: If condensed, tuple of tuples ((field_names), (data1), (data2), ...).
             Otherwise, list of dicts with historical price data. None if request fails.
    :example: commodity_price('ZGUSD', from_date='2023-01-01', to_date='2023-12-31', condensed=True)
    """
    return historical_price_full(symbol, from_date, to_date, condensed)