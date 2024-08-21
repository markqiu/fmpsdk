import typing
import os

from .url_methods import (
    __return_json_v3,
    __validate_statistics_type,
    __validate_technical_indicators_time_delta,
)

API_KEY = os.getenv('FMP_API_KEY')

def technical_indicators(
    symbol: str,
    period: int = 10,
    statistics_type: str = "sma",
    time_delta: str = "daily",
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve technical indicator data for a given stock symbol.

    Calculates various technical indicators based on historical market data.
    Useful for analyzing price trends and potential trading signals.

    :param symbol: Stock ticker symbol (e.g., 'AAPL')
    :param period: Number of data points for calculation (default: 10)
    :param statistics_type: Indicator type (default: 'sma'). Options:
        'sma', 'ema', 'wma', 'dema', 'tema', 'williams', 'rsi', 'adx', 'standardDeviation'
    :param time_delta: Time interval (default: 'daily'). Options:
        '1min', '5min', '15min', '30min', '1hour', '4hour', '1day', '1week', '1month', '1year'
    :return: List of dicts with indicator data or None if request fails
    :example: technical_indicators('AAPL', period=14, statistics_type='rsi', time_delta='1hour')
    """
    path = f"technical_indicator/{__validate_technical_indicators_time_delta(time_delta)}/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "period": period,
        "type": __validate_statistics_type(statistics_type),
    }
    return __return_json_v3(path=path, query_vars=query_vars)