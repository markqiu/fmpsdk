import typing
import os

from .url_methods import (
    __return_json_v3,
    __validate_statistics_type,
    __validate_technical_indicators_time_delta,
)
from .data_compression import compress_json_to_tuples

API_KEY = os.getenv('FMP_API_KEY')

def technical_indicators(
    symbol: str,
    period: int = 10,
    statistics_type: str = "sma",
    time_delta: str = "1day",
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Get technical indicator data for a stock symbol.

    :param symbol: Stock ticker (e.g., 'AAPL')
    :param period: Data points for calculation (default: 10)
    :param statistics_type: Indicator type (default: 'sma')
        Options: 'sma', 'ema', 'wma', 'dema', 'tema', 'williams', 'rsi', 'adx', 'standardDeviation'
    :param time_delta: Time interval (default: '1day')
        Options: '1min', '5min', '15min', '30min', '1hour', '4hour', '1day', '1week', '1month', '1year'
    :param condensed: If True, return tuple of tuples; else, list of dicts (default: True)
    :return: Technical indicator data or None if request fails
    :example: technical_indicators('AAPL', period=14, statistics_type='rsi', time_delta='1hour')
    """
    path = f"technical_indicator/{__validate_technical_indicators_time_delta(time_delta)}/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "period": period,
        "type": __validate_statistics_type(statistics_type),
    }
    result = __return_json_v3(path=path, query_vars=query_vars)
    
    return compress_json_to_tuples(result, condensed)