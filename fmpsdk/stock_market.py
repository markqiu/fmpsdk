import typing
import os
from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3, __return_json_v4
from datetime import date
from .url_methods import __return_json_v4

API_KEY = os.getenv('FMP_API_KEY')

def actives() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve a list of the most actively traded stocks on a given day.

    Provides information on stocks with the highest trading volume,
    indicating high market interest or significant news events. This data
    can be used to identify liquid stocks and potential trading opportunities.

    :return: List of dicts with data on most active stocks or None if request fails.
    :example: actives()

    Each dict in the returned list contains details such as:
    - symbol: The stock's ticker symbol
    - name: The company name
    - change: Price change
    - price: Current stock price
    - changesPercentage: Percentage change in price
    - volume: Trading volume
    """
    path = f"actives"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def gainers() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve a list of stocks that have gained the most value on a given day.

    Provides insights into stocks with positive momentum, helping identify
    potential investment opportunities. Useful for traders looking for
    stocks with upward trends or significant price movements.

    :return: List of dicts with data on biggest gainers or None if request fails.
    :example: gainers()
    """
    path = f"gainers"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def losers() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve a list of stocks that have lost the most value on a given day.

    Provides insights into stocks with negative momentum, helping identify
    underperforming stocks and potential trading opportunities. This data
    can be used to assess market sentiment and identify stocks that may
    continue to depreciate.

    :return: List of dicts with data on biggest losers or None if request fails.
    :example: losers()
    """
    path = f"losers"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def market_hours() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve information about market hours for various exchanges.

    Provides data on opening and closing times for different stock markets,
    helping traders plan their activities around market schedules.

    :return: List of dicts with market hours data or None if request fails.
    :example: market_hours()
    """
    path = f"market-hours"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def sectors_performance(
    limit: int = DEFAULT_LIMIT
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve performance data for various market sectors.

    Provides insights into sector-specific performance, helping investors
    identify trends and make informed decisions about sector allocation.

    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :return: List of dicts with sector performance data or None if request fails.
    :example: sectors_performance(limit=5)
    """
    path = f"sectors-performance"
    query_vars = {"apikey": API_KEY, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)

def fail_to_deliver(symbol: str, page: int = 0) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /fail_to_deliver API for fail to deliver data.

    :param symbol: Company ticker symbol.
    :param page: Page number for pagination (default is 0).
    :return: A list of dictionaries containing fail to deliver data.
    :example: fail_to_deliver('AAPL', page=1)
    """
    path = "fail_to_deliver"
    query_vars = {
        "apikey": API_KEY,
        "symbol": symbol,
        "page": page
    }
    return __return_json_v4(path=path, query_vars=query_vars)

def sector_pe_ratio(date: date, exchange: str = "NYSE") -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /sector_price_earning_ratio API.

    :param date: The date for which to retrieve the sector PE ratios in 'yyyy-mm-dd' format.
    :param exchange: The stock exchange (default is NYSE).
    :return: A list of dictionaries containing sector PE ratios.
    :example: sector_pe_ratio('2023-01-01', exchange='NASDAQ')
    """
    path = f"sector_price_earning_ratio"
    query_vars = {
        "date": date,
        "exchange": exchange,
        "apikey": API_KEY
    }
    return __return_json_v4(path=path, query_vars=query_vars)

def industry_pe_ratio(date: str, exchange: str = "NYSE") -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve industry-specific price-to-earnings (PE) ratios.

    Provides PE ratios for various industries in the stock market, helping to
    identify potentially overvalued or undervalued sectors. This data is useful
    for comparing valuations across different industries and making informed
    investment decisions.

    :param date: Date for which to retrieve industry PE ratios (format: 'YYYY-MM-DD').
    :param exchange: Stock exchange (default is NYSE).
    :return: List of dictionaries containing industry PE ratios or None if request fails.
    :example: industry_pe_ratio('2024-08-01', exchange='NYSE')

    Data can be used to:
    - Compare PE ratios across industries
    - Identify potential investment opportunities
    - Assess relative valuations within the market
    """
    path = "industry_price_earning_ratio"
    query_vars = {
        "date": date, 
        "exchange": exchange,
        "apikey": API_KEY
    }
    return __return_json_v4(path=path, query_vars=query_vars)

def batch_eod_prices(date: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Get batch request that contains all end of day prices for a specific date.

    :param date: The date in format YYYY-MM-DD
    :return: A list of dictionaries containing EOD prices for multiple stocks
    """
    path = "batch-request-end-of-day-prices"
    query_vars = {"apikey": API_KEY, "date": date}
    return __return_json_v4(path=path, query_vars=query_vars)

def multiple_company_prices(
    symbols: typing.Union[str, typing.List[str]]
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve real-time price data for multiple companies in a single request.

    Provides key information such as current price, change, percent change,
    day low/high, year low/high, market cap, volume, and more for each symbol.
    Useful for tracking multiple stocks efficiently.

    :param symbols: Single stock symbol as string or list of stock symbols
                    (e.g., 'AAPL' or ['AAPL', 'MSFT'])
    :return: List of dicts with price information for the requested symbols
    :example: multiple_company_prices('AAPL,MSFT')
              multiple_company_prices(['AAPL', 'MSFT'])
    """
    symbols_str = ','.join(symbols) if isinstance(symbols, list) else symbols
    path = f"quote/{symbols_str}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def historical_sectors_performance(from_date: str, to_date: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve historical performance data for stock market sectors.

    Provides insights into sector trends over time, helping investors identify
    patterns and make informed decisions. Useful for comparing sector
    performance and spotting potential investment opportunities.

    :param from_date: Start date in format YYYY-MM-DD.
    :param to_date: End date in format YYYY-MM-DD.
    :return: List of dicts with historical sector performance data,
             including date and performance for each sector.
    :example: historical_sectors_performance('2024-01-01', '2024-03-01')
    """
    path = "historical-sectors-performance"
    query_vars = {
        "apikey": API_KEY,
        "from": from_date,
        "to": to_date
    }
    return __return_json_v3(path=path, query_vars=query_vars)