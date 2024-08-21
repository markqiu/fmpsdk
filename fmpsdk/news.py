import typing
from .url_methods import __return_json_v3, __return_json_v4
import os
from .settings import (
    DEFAULT_LIMIT,
)
API_KEY = os.getenv('FMP_API_KEY')

def fmp_articles(page: int = 0, size: int = 5) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve the latest articles from Financial Modeling Prep.

    Provides access to FMP's latest financial news and analysis articles.
    Useful for staying updated on market trends, company news, and financial insights.

    :param page: Page number for pagination (default: 0).
    :param size: Number of articles per page (default: 5).
    :return: List of dicts with article data or None if request fails.
    :example: fmp_articles(page=1, size=5)
    """
    path = "fmp/articles"
    query_vars = {"apikey": API_KEY, "page": page, "size": size}
    return __return_json_v3(path=path, query_vars=query_vars)

def general_news(page: int = 0) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve the latest general news articles from a variety of sources.

    Provides access to a daily-updated list of general news articles.
    Useful for staying informed on current events and market trends.
    Each article includes headline, snippet, and publication URL.

    :param page: Page number for pagination (default: 0).
    :return: List of dicts with general news data or None if request fails.
    :example: general_news(page=1)
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
    Retrieve the latest stock-specific news articles from various sources.

    Provides news articles related to specific stocks or companies, including
    headline, snippet, publication URL, and ticker symbol. Updated daily to
    offer the most current stock market news.

    :param tickers: Ticker symbol(s) (e.g., 'AAPL' or ['AAPL', 'FB']).
    :param limit: Number of results per page (default: DEFAULT_LIMIT).
    :param page: Page number for pagination (default: 0).
    :param from_date: Start date for news articles (format: YYYY-MM-DD).
    :param to_date: End date for news articles (format: YYYY-MM-DD).
    :return: List of dicts with stock news data or None if request fails.
    :example: stock_news(['AAPL', 'FB'], limit=10, page=3, from_date='2024-01-01', to_date='2024-03-01')
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