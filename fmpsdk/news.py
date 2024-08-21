import typing
from .url_methods import __return_json_v3, __return_json_v4
import os
from .settings import (
    DEFAULT_LIMIT,
)
API_KEY = os.getenv('FMP_API_KEY')

def fmp_articles(page: int = 0, size: int = 5) -> typing.Optional[typing.List[typing.Dict]]: 
    """
    Query FMP /fmp/articles/ API.

    Get a list of the latest articles from Financial Modeling Prep, including the headline, snippet, and publication URL.

    :param page: The page number for pagination (default: 0).
    :param size: The number of articles per page (default: 5).
    :return: A list of dictionaries containing FMP articles information or None if the request fails.
    :example: fmp_articles(page=1, size=5)
    :endpoint: https://financialmodelingprep.com/api/v3/fmp/articles?page={page}&size={size}
    """
    path = "fmp/articles"
    query_vars = {"apikey": API_KEY, "page": page, "size": size}
    return __return_json_v3(path=path, query_vars=query_vars)

def general_news(page: int = 0) -> typing.Optional[typing.List[typing.Dict]]: 
    """
    Query FMP /general_news/ API.

    Get a list of the latest general news articles from a variety of sources, including the headline, snippet, and publication URL.

    :param page: The page number for pagination (default: 0).
    :return: A list of dictionaries containing general news articles information or None if the request fails.
    :example: general_news(page=1)
    :endpoint: https://financialmodelingprep.com/api/v4/general_news?page={page}
    """
    path = "general_news"
    query_vars = {"apikey": API_KEY, "page": page}
    return __return_json_v4(path=path, query_vars=query_vars)

def stock_news(
    tickers: typing.Union[str, typing.List] = "",
    limit: int = DEFAULT_LIMIT,
    page: int = 0,
    from_date: str = "",
    to_date: str = "",
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /stock_news/ API for latest stock news articles.

    :param tickers: Ticker symbol(s) (e.g., 'AAPL' or ['AAPL', 'GOOGL']).
    :param limit: Number of results per page. Default is DEFAULT_LIMIT.
    :param page: Page number for pagination. Default is 0.
    :param from_date: Start date for news articles (format: YYYY-MM-DD).
    :param to_date: End date for news articles (format: YYYY-MM-DD).
    :return: List of dictionaries with stock news articles or None if request fails.
    :example: stock_news(['AAPL', 'GOOGL'], limit=10, page=1, from_date='2024-01-01', to_date='2024-03-01')
    :endpoint: https://financialmodelingprep.com/api/v3/stock_news
    """
    path = "stock_news"
    query_vars = {"apikey": API_KEY, "limit": limit, "page": page}
    if tickers:
        query_vars["tickers"] = ",".join(tickers) if isinstance(tickers, list) else tickers
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date
    return __return_json_v3(path=path, query_vars=query_vars)