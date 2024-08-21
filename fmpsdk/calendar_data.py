import typing
import os
from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3

API_KEY = os.getenv('FMP_API_KEY')

def earning_calendar(
    from_date: str = None,
    to_date: str = None,
    estimate_required: bool = True,
    condensed: bool = True,
    revenue_minimum: float = 1000000000
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve a list of upcoming and past earnings announcements.

    Provides valuable insights into companies' financial performance and outlook.

    :param from_date: Start date in 'YYYY-MM-DD' format.
    :param to_date: End date in 'YYYY-MM-DD' format.
    :param estimate_required: If True, exclude entries where either 'epsEstimated'
                              or 'revenueEstimated' is null. Defaults to True.
    :param condensed: If True, return only key fields in each entry. Defaults to True.
    :param revenue_minimum: Minimum 'revenueEstimated' value to include an entry.
                            Defaults to 1,000,000,000 (1 billion).
    :return: List of dicts with earnings data, or None if request fails.
    :example: earning_calendar('2023-01-01', '2023-12-31', estimate_required=True, 
                                condensed=True, revenue_minimum=500000000)
    """
    path = "earning_calendar"
    query_vars = {"apikey": API_KEY}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    
    result = __return_json_v3(path=path, query_vars=query_vars)
    
    if result is not None:
        if estimate_required:
            result = [entry for entry in result if entry.get('epsEstimated') is not None and entry.get('revenueEstimated') is not None]
        
        result = [entry for entry in result if entry.get('revenueEstimated', 0) >= revenue_minimum]
        
        if condensed:
            condensed_fields = ['date', 'eps', 'epsEstimated', 'revenue', 'revenueEstimated', 'symbol']
            result = [{field: entry.get(field) for field in condensed_fields} for entry in result]
        
        return result
    
    return None

def historical_earning_calendar(
    symbol: str, limit: int = DEFAULT_LIMIT
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve historical and upcoming earnings announcements for a specific company.

    Provides valuable insights into a company's past performance and future outlook.
    Useful for analyzing earnings trends, identifying surprises, and making
    informed investment decisions.

    :param symbol: Ticker symbol of the company (e.g., 'AAPL').
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :return: List of dicts with earnings data, including date, estimated EPS,
             and actual EPS, or None if request fails.
    :example: historical_earning_calendar('AAPL', limit=10)
    """
    path = f"historical/earning_calendar/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "symbol": symbol,
        "limit": limit,
    }
    return __return_json_v3(path=path, query_vars=query_vars)

def ipo_calendar(
    from_date: str = None, to_date: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve a list of confirmed upcoming IPOs.

    Provides information on scheduled Initial Public Offerings, including
    company name, symbol, IPO date, exchange, and pricing details. Useful
    for tracking new investment opportunities and market trends.

    :param from_date: Start date for IPO range (format: YYYY-MM-DD).
    :param to_date: End date for IPO range (format: YYYY-MM-DD).
    :return: List of dicts with IPO calendar data.
    :example: ipo_calendar(from_date='2023-01-01', to_date='2023-12-31')
    """
    path = f"ipo_calendar"
    query_vars = {"apikey": API_KEY}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v3(path=path, query_vars=query_vars)

def stock_split_calendar(
    from_date: str = None, to_date: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve upcoming stock split data for publicly traded companies.

    Provides information on scheduled stock splits, including split date,
    ratio, and type. Useful for identifying potential investment opportunities,
    tracking increased liquidity, and monitoring changes in share affordability.

    :param from_date: Start date for the split calendar (format: YYYY-MM-DD).
    :param to_date: End date for the split calendar (format: YYYY-MM-DD).
    :return: List of dicts with stock split calendar data.
    :example: stock_split_calendar(from_date='2023-08-10', to_date='2023-10-10')
    """
    path = f"stock_split_calendar"
    query_vars = {"apikey": API_KEY}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v3(path=path, query_vars=query_vars)

def dividend_calendar(
    from_date: str = None, to_date: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve upcoming dividend payments for publicly traded companies.

    Provides a list of dividend payments within a specified date range,
    including payment date, ex-dividend date, and dividend per share.
    Useful for identifying high-yield stocks, tracking dividend histories,
    and planning income-focused investment strategies.

    :param from_date: Start date for dividend calendar (format: YYYY-MM-DD).
    :param to_date: End date for dividend calendar (format: YYYY-MM-DD).
    :return: List of dicts with dividend calendar data.
    :example: dividend_calendar(from_date='2023-10-01', to_date='2023-10-31')
    Note: Maximum time interval between from_date and to_date is 3 months.
    """
    path = f"stock_dividend_calendar"
    query_vars = {"apikey": API_KEY}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v3(path=path, query_vars=query_vars)

def economic_calendar(
    from_date: str = None, to_date: str = None
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve a calendar of upcoming economic data releases.

    Provides insights into future economic events that may impact markets.
    Useful for staying informed, preparing for market reactions, and making
    investment decisions based on economic data releases.

    :param from_date: Start date in 'YYYY-MM-DD' format.
    :param to_date: End date in 'YYYY-MM-DD' format.
    :return: List of dicts with economic calendar data or None if request fails.
    :example: economic_calendar('2023-08-10', '2023-10-10')
    Note: Maximum time interval between from_date and to_date is 3 months.
    """
    path = f"economic_calendar"
    query_vars = {"apikey": API_KEY}
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v3(path=path, query_vars=query_vars)