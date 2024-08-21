import logging
import typing
import os
import requests
from bs4 import BeautifulSoup

from .settings import DEFAULT_LIMIT
from .url_methods import (
    __return_json_v3,
    __return_json_v4,
    __validate_industry,
    __validate_period,
    __validate_sector,
)

API_KEY = os.getenv('FMP_API_KEY')

# Get the SEC User-Agent from environment variable
SEC_USER_AGENT = os.getenv('SEC_USER_AGENT')

def financial_statement_symbol_lists() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve a list of symbols with available financial statements.

    Useful for identifying companies with accessible financial data for analysis.

    :return: List of dicts with symbols and their available financial statements.
    :example: financial_statement_symbol_lists()
    """
    path = "financial-statement-symbol-lists"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def enterprise_values(symbol: str, period: str = "annual", limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve enterprise value data for a company.

    Provides the total value of a company, including equity and debt.
    Useful for assessing overall company value and comparing with peers.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param period: Reporting period ('annual' or 'quarter'). Default is 'annual'.
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :return: List of dicts with enterprise value data or None if request fails.
    :example: enterprise_values('AAPL', period='quarter', limit=5)
    """
    path = f"enterprise-values/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "period": __validate_period(value=period),
        "limit": limit,
    }
    return __return_json_v3(path=path, query_vars=query_vars)

def key_metrics_ttm(symbol: str, limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve trailing twelve months (TTM) key metrics for a company.

    Provides essential financial metrics for recent performance analysis.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :return: List of dicts with TTM key metrics data or None if request fails.
    :example: key_metrics_ttm('AAPL', limit=5)
    """
    path = f"key-metrics-ttm/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)

def key_metrics(symbol: str, period: str = "annual", limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve key financial metrics for a company's performance assessment.

    Provides crucial KPIs including revenue, net income, EPS, and P/E ratio.
    Useful for financial analysis, competitor comparisons, and goal tracking.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param period: Reporting period ('annual' or 'quarter'). Default is 'annual'.
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :return: List of dicts with key financial metrics or None if request fails.
    :example: key_metrics('AAPL', period='quarter', limit=5)
    """
    path = f"key-metrics/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "period": __validate_period(value=period),
        "limit": limit,
    }
    return __return_json_v3(path=path, query_vars=query_vars)

def rating(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve a comprehensive rating for a company based on various financial factors.

    Provides an assessment of a company's financial health, including ratings
    derived from financial statements, DCF analysis, ratios, and intrinsic value.
    Useful for quick company comparisons and identifying investment opportunities.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: List of dicts with rating data or None if request fails.
    :example: rating('AAPL')
    """
    path = f"rating/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def historical_rating(symbol: str, limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve historical ratings for a company over time.

    Provides insights into a company's rating changes, helping investors
    track performance trends and identify potential investment opportunities.
    Includes rating, recommendation, and DCF score for each time period.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param limit: Number of records to retrieve. Default is 10.
    :return: List of dicts with historical rating data or None if request fails.
    :example: historical_rating('AAPL', limit=5)
    """
    path = f"historical-rating/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)

def discounted_cash_flow(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve the discounted cash flow (DCF) valuation for a company.

    Provides a valuation estimate based on future cash flows and a discount rate.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: List of dicts with DCF valuation data or None if request fails.
    :example: discounted_cash_flow('AAPL')
    """
    path = f"discounted-cash-flow/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def advanced_discounted_cash_flow(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve advanced DCF valuation data for a company.

    Provides a more comprehensive valuation estimate based on various factors.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: List of dicts with advanced DCF valuation data or None if request fails.
    :example: advanced_discounted_cash_flow('AAPL')
    """
    path = f"advanced_discounted_cash_flow"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def historical_discounted_cash_flow(symbol: str, period: str = "annual", limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve historical DCF valuation data for a company.

    Provides insights into a company's past DCF valuations and trends.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param period: Reporting period ('annual' or 'quarter'). Default is 'annual'.
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :return: List of dicts with historical DCF valuation data or None if request fails.
    :example: historical_discounted_cash_flow('AAPL', period='quarter', limit=5)
    """
    path = f"historical-discounted-cash-flow/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
        "period": __validate_period(value=period),
    }
    return __return_json_v3(path=path, query_vars=query_vars)

def historical_daily_discounted_cash_flow(symbol: str, limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve daily historical DCF valuation data for a company.

    Provides insights into a company's daily DCF valuations and trends.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :return: List of dicts with daily historical DCF valuation data or None if request fails.
    :example: historical_daily_discounted_cash_flow('AAPL', limit=5)
    """
    path = f"historical-daily-discounted-cash-flow/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)

def symbols_list() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve a list of all available stock symbols.

    Useful for exploring and analyzing a wide range of stocks.

    :return: List of dicts with stock symbols data or None if request fails.
    :example: symbols_list()
    """
    path = f"stock/list"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def etf_list() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve a list of all available ETF symbols.

    Useful for exploring and analyzing a wide range of ETFs.

    :return: List of dicts with ETF symbols data or None if request fails.
    :example: etf_list()
    """
    path = "etf/list"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def available_traded_list() -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve a list of all available tradable symbols.

    Useful for exploring and analyzing a wide range of tradable securities.

    :return: List of dicts with tradable symbols data or None if request fails.
    :example: available_traded_list()
    """
    path = "available-traded/list"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def delisted_companies(limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve a list of delisted companies.

    Useful for tracking and analyzing companies that have been delisted from exchanges.

    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :return: List of dicts with delisted companies data or None if request fails.
    :example: delisted_companies(limit=10)
    """
    path = "delisted-companies"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def earnings_surprises(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve earnings surprises for a company.

    Provides insights into a company's financial performance vs. market expectations.
    Useful for identifying earnings beats/misses and analyzing trends that can
    impact stock prices and investor sentiment.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: List of dicts with earnings surprises data, including date,
             actual EPS, estimated EPS, and surprise percentage.
    :example: earnings_surprises('AAPL')
    """
    path = f"earnings-surprises/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def earning_call_transcript(symbol: str, year: int, quarter: int) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve the earning call transcript for a specific quarter and year.

    Provides insights into a company's financial performance and management discussions.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param year: Year of the transcript (e.g., 2023).
    :param quarter: Quarter of the transcript (1-4).
    :return: List of dicts with earning call transcript data or None if request fails.
    :example: earning_call_transcript('AAPL', 2023, 1)
    """
    path = f"earning_call_transcript/{symbol}"
    query_vars = {"apikey": API_KEY, "year": year, "quarter": quarter}
    return __return_json_v3(path=path, query_vars=query_vars)

def batch_earning_call_transcript(symbol: str, year: int) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve batch earning call transcripts for a specific year.

    Provides insights into a company's financial performance and management discussions
    for multiple quarters in a single year.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param year: Year of the transcripts (e.g., 2023).
    :return: List of dicts with batch earning call transcript data or None if request fails.
    :example: batch_earning_call_transcript('AAPL', 2023)
    """
    path = f"batch_earning_call_transcript/{symbol}"
    query_vars = {"apikey": API_KEY, "year": year}
    return __return_json_v4(path=path, query_vars=query_vars)

def earning_call_transcripts_available_dates(symbol: str) -> typing.Optional[typing.List[typing.List]]:
    """
    Retrieve available dates for earning call transcripts.

    Useful for planning and accessing transcripts for specific quarters and years.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: List of lists with available dates for earning call transcripts or None if request fails.
    :example: earning_call_transcripts_available_dates('AAPL')
    """
    path = f"earning_call_transcript"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def sec_filings(symbol: str, filing_type: str = "", limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve links to a company's SEC filings.

    Provides access to important financial documents and regulatory filings.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param filing_type: SEC filing type (e.g., '10-K', '10-Q', '8-K'). Default is all types.
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :return: List of dicts with SEC filings data or None if request fails.
    :example: sec_filings('AAPL', filing_type='10-K', limit=10)
    """
    path = f"sec_filings/{symbol}"
    query_vars = {"apikey": API_KEY, "type": filing_type, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)

def clean_html_content(soup):
    # Remove script and style elements
    for script in soup(["script", "style"]):
        script.decompose()

    # Remove all attributes from HTML tags
    for tag in soup.recursiveChildGenerator():
        if hasattr(tag, 'attrs'):
            tag.attrs = {}

    # Get text
    text = soup.get_text()

    # Break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # Break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # Drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return text

def sec_filings_data(symbol: str, filing_type: str = "", limit: int = 1) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve a company's SEC filings and fetch the content from 'finalLink'.

    Provides access to important financial documents and regulatory filings,
    along with the content of the filings.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param filing_type: SEC filing type (e.g., '10-K', '10-Q', '8-K'). Default is all types.
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :return: List of dicts with SEC filings data, including the content from 'finalLink',
             or None if request fails.
    :example: sec_filings_data('AAPL', filing_type='10-K', limit=2)
    Note: this function returns unredacted full text of the filings and 
    may not be suitable for LLM processing in the absense of very long 
    context windows. e.g. a single 10-K filing can be 50k+ tokens.
    """
    # First, get the SEC filings data using the existing function
    filings = sec_filings(symbol, filing_type, limit)
    
    if filings is None:
        return None

    # Set up headers for SEC requests
    headers = {
        'User-Agent': SEC_USER_AGENT
    }

    # Process each filing to fetch and add the content
    for filing in filings:
        final_link = filing.get('finalLink')
        if final_link:
            try:
                response = requests.get(final_link, headers=headers)
                response.raise_for_status()
                
                # Parse the HTML content
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Clean and extract the text content
                content = clean_html_content(soup)
                
                # Add the content to the filing dictionary
                filing['content'] = content
            except requests.RequestException as e:
                logging.error(f"Error fetching content from {final_link}: {str(e)}")
                filing['content'] = None
        else:
            filing['content'] = None

    return filings

def press_releases(
    symbol: str = None,
    limit: int = DEFAULT_LIMIT,
    page: int = 0
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve the latest press releases, optionally filtered by company.

    Provides detailed information about company announcements, including
    release date, title, and content. Useful for staying updated on important
    developments and news from organizations.

    :param symbol: Company ticker (e.g., 'AAPL'). If None, returns releases
                   for all companies.
    :param limit: Number of records to retrieve. Default is 10.
    :param page: Page number for pagination. Default is 0.
    :return: List of dicts with press releases data or None if request fails.
    :example: press_releases(symbol='AAPL', limit=10, page=0)
              press_releases(limit=20, page=1)
    """
    path = f"press-releases/{symbol}" if symbol else "press-releases"
    query_vars = {"apikey": API_KEY, "limit": limit, "page": page}
    return __return_json_v3(path=path, query_vars=query_vars)

def stock_peers(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve a group of companies similar to the given stock.

    Provides peers trading on the same exchange, in the same sector,
    with similar market capitalization. Useful for competitor analysis
    and identifying well-performing companies in the same industry.

    :param symbol: Company ticker (e.g., 'AAPL')
    :return: List of dicts with stock peers data or None if request fails
    :example: stock_peers('AAPL')
    """
    path = f"stock_peers"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def analyst_estimates(symbol: str, period: str = "annual", limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve analyst estimates for a company's future earnings and revenue.

    Provides forecasts to help identify potential investment opportunities.
    Note that analyst estimates are not always accurate.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param period: Reporting period ('annual' or 'quarter'). Default is 'annual'.
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :return: List of dicts with analyst estimates data, including estimated
             revenue, EBITDA, EBIT, net income, EPS, and more.
    :example: analyst_estimates('AAPL', period='quarter', limit=5)
    """
    path = f"/analyst-estimates/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "symbol": symbol,
        "period": __validate_period(value=period),
        "limit": limit,
    }
    return __return_json_v3(path=path, query_vars=query_vars)

def sales_revenue_by_segments(
    symbol: str,
    structure: str = "flat",
    period: str = "annual"
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve revenue breakdown by product category for a company.

    Useful for identifying most profitable products, tracking performance,
    and making informed investment decisions.

    :param symbol: Company ticker (e.g., 'AAPL')
    :param structure: Data structure ('flat' or 'segment'). Default is 'flat'
    :param period: Reporting period ('annual' or 'quarter'). Default is 'annual'
    :return: List of dicts with revenue segmentation data or None if request fails
    :example: sales_revenue_by_segments('AAPL', structure='segment', period='quarter')
    """
    path = "revenue-product-segmentation"
    query_vars = {
        "apikey": API_KEY,
        "symbol": symbol,
        "structure": structure,
        "period": period
    }
    return __return_json_v4(path=path, query_vars=query_vars)

def revenue_geographic_segmentation(
    symbol: str,
    structure: str = "flat",
    period: str = "annual"
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve revenue breakdown by geographic region for a company.

    Useful for identifying profitable regions, tracking performance over time,
    and making informed investment decisions.

    :param symbol: Company ticker (e.g., 'AAPL')
    :param structure: Data structure ('flat' or 'segment'). Default is 'flat'
    :param period: Reporting period ('annual' or 'quarter'). Default is 'annual'
    :return: List of dicts with revenue by geographic segments or None if request fails
    :example: revenue_geographic_segmentation('AAPL', structure='segment', period='quarter')
    """
    path = "revenue-geographic-segmentation"
    query_vars = {
        "apikey": API_KEY,
        "symbol": symbol,
        "structure": structure,
        "period": period
    }
    return __return_json_v4(path=path, query_vars=query_vars)

def esg_score(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve Environmental, Social, and Governance (ESG) ratings for a company.

    Provides insights into a company's sustainability and social responsibility performance.
    Useful for making informed investment decisions based on ESG factors.
    Data is sourced from corporate sustainability reports, ESG research firms, and government agencies.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: List of dicts with ESG ratings data or None if request fails.
    :example: esg_score('AAPL')
    """
    path = f"esg-environmental-social-governance-data"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def stock_grade(symbol: str, limit: int = 50) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve stock grades given by hedge funds, investment firms, and analysts.

    Provides ratings and insights on a company's financial performance,
    business model, and competitive landscape. Useful for understanding
    professional investors' views and identifying investment opportunities.

    :param symbol: Company ticker (e.g., 'AAPL')
    :param limit: Number of results to return (default: 50)
    :return: List of dicts with stock grade data or None if request fails
    :example: stock_grade('AAPL', limit=10)
    """
    path = f"grade/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    return __return_json_v3(path=path, query_vars=query_vars)

def financial_score(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve the financial score for a company.

    Provides an assessment of a company's financial health and performance.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: List of dicts with financial score data or None if request fails.
    :example: financial_score('AAPL')
    """
    path = "score"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def owner_earnings(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve owner earnings data for a company.

    Provides insights into a company's earnings available for common shareholders.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: List of dicts with owner earnings data or None if request fails.
    :example: owner_earnings('AAPL')
    """
    path = "owner_earnings"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def upgrades_downgrades(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve a comprehensive list of stock upgrades and downgrades for a company.

    Provides insights into analysts' changing expectations for a stock's performance.
    Updated daily to offer the most current analyst ratings.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: List of dicts with upgrade/downgrade data, including rating changes,
             analyst firms, and dates, or None if request fails.
    :example: upgrades_downgrades('AAPL')
    """
    path = "upgrades-downgrades"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def upgrades_downgrades_rss_feed(page: int = 0) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve daily-updated RSS feed of stock upgrades and downgrades from various analysts.

    Provides the latest analyst ratings to help investors stay informed about
    changing market sentiments and potential investment opportunities.

    :param page: Page number for pagination. Default is 0.
    :return: List of dicts with latest stock upgrades and downgrades data,
             including rating changes, analyst firms, and dates.
    :example: upgrades_downgrades_rss_feed(page=1)
    """
    path = "upgrades-downgrades-rss-feed"
    query_vars = {"apikey": API_KEY, "page": page}
    return __return_json_v4(path=path, query_vars=query_vars)

def upgrades_downgrades_consensus(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve the consensus rating for a company's stock.

    Provides an average rating from different analysts, offering a general
    idea of analysts' opinions about a company's stock. This can be used
    to make more informed investment decisions.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: List of dicts with consensus rating data or None if request fails.
             Data includes overall rating and individual analyst ratings.
    :example: upgrades_downgrades_consensus('AAPL')
    """
    path = "upgrades-downgrades-consensus"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def upgrades_downgrades_by_company(company: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve stock upgrades and downgrades issued by a specific analyst company.

    Provides a comprehensive list of rating changes for various stocks,
    including the rating change, analyst firm, and date. This data can be
    used to track analyst sentiment and identify potential investment
    opportunities or risks.

    :param company: Analyst company name (e.g., 'Barclays').
    :return: List of dicts with stock upgrades and downgrades data, including
             company symbol, rating change, analyst firm, and date.
    :example: upgrades_downgrades_by_company('Barclays')
    """
    path = "upgrades-downgrades-grading-company"
    query_vars = {"apikey": API_KEY, "company": company}
    return __return_json_v4(path=path, query_vars=query_vars)

def mergers_acquisitions_rss_feed(page: int = 0) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve the latest M&A news RSS feed.

    Provides insights into mergers, acquisitions, and other corporate transactions.

    :param page: Page number for pagination. Default is 0.
    :return: List of dicts with latest M&A news RSS feed data or None if request fails.
    :example: mergers_acquisitions_rss_feed(page=1)
    """
    path = "mergers-acquisitions-rss-feed"
    query_vars = {"apikey": API_KEY, "page": page}
    return __return_json_v4(path=path, query_vars=query_vars)

def search_mergers_acquisitions(name: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Search for M&A deals based on company name.

    Provides insights into mergers, acquisitions, and other corporate transactions
    for a specific company.

    :param name: Company name (e.g., 'Apple').
    :return: List of dicts with M&A deal data for the company or None if request fails.
    :example: search_mergers_acquisitions('Apple')
    """
    path = "mergers-acquisitions/search"
    query_vars = {"apikey": API_KEY, "name": name}
    return __return_json_v4(path=path, query_vars=query_vars)

def executive_compensation(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve executive compensation data for a company.

    Provides insights into the compensation of key executives and their impact on shareholder value.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: List of dicts with executive compensation data or None if request fails.
    :example: executive_compensation('AAPL')
    """
    path = "governance/executive_compensation"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def compensation_benchmark(year: int) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve executive compensation benchmark data for a specific year.

    Provides insights into the compensation trends and benchmarks for key executives in various industries.

    :param year: Year for compensation benchmark data (e.g., 2023).
    :return: List of dicts with compensation benchmark data or None if request fails.
    :example: compensation_benchmark(2023)
    """
    path = "executive-compensation-benchmark"
    query_vars = {"apikey": API_KEY, "year": year}
    return __return_json_v4(path=path, query_vars=query_vars)

def company_notes(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve company notes for a specific company.

    Provides additional insights and notes about a company's performance and operations.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: List of dicts with company notes data or None if request fails.
    :example: company_notes('AAPL')
    """
    path = "company-notes"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def historical_employee_count(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve historical employee count data for a company.

    Tracks workforce growth or decline over time, providing insights into
    company expansion, efficiency, and industry comparisons. Useful for
    identifying trends in company growth and operational efficiency.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: List of dicts with historical employee count data or None if request fails.
    :example: historical_employee_count('AAPL')
    """
    path = "historical/employee_count"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def employee_count(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve the current number of employees for a company.

    Provides insights into a company's workforce size and potential growth.
    Useful for comparing company sizes, assessing growth potential, and
    analyzing workforce trends.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: List of dicts with current employee count data or None if request fails.
    :example: employee_count('AAPL')
    """
    path = "employee_count"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def company_core_information(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve core information for a company.

    Provides a comprehensive overview of a company's basic information.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: List of dicts with company core information data or None if request fails.
    :example: company_core_information('AAPL')
    """
    path = "company-core-information"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)

def all_countries() -> typing.Optional[typing.List[str]]:
    """
    Retrieve a list of all available countries.

    Useful for exploring and analyzing data from various countries.

    :return: List of country names or None if request fails.
    :example: all_countries()
    """
    path = "get-all-countries"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def analyst_recommendation(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve analyst recommendations for buying, selling, or holding a company's stock.

    Provides insights to help make informed investment decisions. Note that
    recommendations are not always accurate; investors should do their own research.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: List of dicts with analyst recommendations data, including
             analyst firm, rating, price target, and action (buy/sell/hold).
    :example: analyst_recommendation('AAPL')
    """
    path = f"analyst-stock-recommendations/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def is_market_open(exchange: str = "NASDAQ") -> typing.Optional[typing.Dict]:
    """
    Check if a specific exchange is currently open or closed.

    Useful for determining market hours and availability of data.

    :param exchange: Exchange name (e.g., 'NASDAQ'). Default is 'NASDAQ'.
    :return: Dictionary with market open/close status or None if request fails.
    :example: is_market_open('NYSE')
    """
    path = "is-the-market-open"
    query_vars = {"apikey": API_KEY, "exchange": exchange}
    return __return_json_v3(path=path, query_vars=query_vars)

def available_sectors() -> typing.Optional[typing.List[str]]:
    """
    Retrieve a list of available sectors.

    Useful for exploring and analyzing data across various sectors.

    :return: List of sector names or None if request fails.
    :example: available_sectors()
    """
    path = "sectors-list"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def available_industries() -> typing.Optional[typing.List[str]]:
    """
    Retrieve a list of available industries.

    Useful for exploring and analyzing data across various industries.

    :return: List of industry names or None if request fails.
    :example: available_industries()
    """
    path = "industries-list"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def available_exchanges() -> typing.Optional[typing.List[str]]:
    """
    Retrieve a list of available exchanges.

    Useful for exploring and analyzing data from various exchanges.

    :return: List of exchange names or None if request fails.
    :example: available_exchanges()
    """
    path = "exchanges-list"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)

def company_outlook(symbol: str) -> typing.Optional[typing.Dict]:
    """
    Retrieve the company outlook for a specific company.

    Provides insights into a company's future outlook and expectations.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: Dictionary with company outlook data or None if request fails.
    :example: company_outlook('AAPL')
    """
    path = "company-outlook"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)