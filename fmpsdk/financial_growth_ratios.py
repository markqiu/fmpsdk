import typing
import os
from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3, __validate_period

API_KEY = os.getenv('FMP_API_KEY')

def income_statement_growth(symbol: str, limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve income statement growth metrics for a company.

    Provides insights into a company's revenue and profit growth trends.
    Useful for assessing financial performance and identifying growth patterns.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :return: List of dicts with income statement growth data or None if request fails.
    :example: income_statement_growth('AAPL', limit=5)
    """
    path = f"income-statement-growth/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
    }
    return __return_json_v3(path=path, query_vars=query_vars)


def balance_sheet_statement_growth(symbol: str, limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve balance sheet statement growth metrics for a company.

    Provides insights into a company's assets, liabilities, and equity growth.
    Useful for assessing financial health and long-term stability.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :return: List of dicts with balance sheet growth data or None if request fails.
    :example: balance_sheet_statement_growth('AAPL', limit=5)
    """
    path = f"balance-sheet-statement-growth/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
    }
    return __return_json_v3(path=path, query_vars=query_vars)


def cash_flow_statement_growth(symbol: str, limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve cash flow statement growth metrics for a company.

    Provides insights into a company's cash inflows and outflows growth.
    Useful for assessing liquidity and financial flexibility.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :return: List of dicts with cash flow statement growth data or None if request fails.
    :example: cash_flow_statement_growth('AAPL', limit=5)
    """
    path = f"cash-flow-statement-growth/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
    }
    return __return_json_v3(path=path, query_vars=query_vars)


def financial_ratios_ttm(symbol: str) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve trailing twelve months (TTM) financial ratios for a company.

    Provides insights into a company's current financial performance and efficiency.
    Useful for comparing with industry averages and identifying areas for improvement.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: List of dicts with TTM financial ratios data or None if request fails.
    :example: financial_ratios_ttm('AAPL')
    """
    path = f"ratios-ttm/{symbol}"
    query_vars = {"apikey": API_KEY}
    return __return_json_v3(path=path, query_vars=query_vars)


def financial_ratios(
    symbol: str, period: str = "annual", limit: int = DEFAULT_LIMIT
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve financial ratios for a company.

    Provides insights into a company's financial performance and efficiency.
    Useful for comparing with industry averages and identifying areas for improvement.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param period: Reporting period ('annual' or 'quarter'). Default is 'annual'.
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :return: List of dicts with financial ratios data or None if request fails.
    :example: financial_ratios('AAPL', period='quarter', limit=5)
    """
    path = f"ratios/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "period": __validate_period(value=period),
        "limit": limit,
    }
    return __return_json_v3(path=path, query_vars=query_vars)


def financial_growth(symbol: str, period: str = "annual", limit: int = DEFAULT_LIMIT) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve financial growth metrics for a company.

    Provides insights into a company's overall financial performance improvement.
    Useful for assessing growth trends, comparing performance over time, and
    identifying potential investment opportunities.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param period: Reporting period ('annual' or 'quarter'). Default is 'annual'.
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :return: List of dicts with financial growth data or None if request fails.
    :example: financial_growth('AAPL', period='quarter', limit=5)
    """
    path = f"financial-growth/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
        "period": __validate_period(value=period),
    }
    return __return_json_v3(path=path, query_vars=query_vars)