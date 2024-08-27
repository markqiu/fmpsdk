import typing
import os
from .settings import DEFAULT_LIMIT
from .url_methods import __return_json_v3, __validate_period
from .data_compression import compress_json_to_tuples

API_KEY = os.getenv('FMP_API_KEY')


def income_statement_growth(
    symbol: str,
    limit: int = DEFAULT_LIMIT,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Retrieve income statement growth metrics for a company.

    Provides insights into a company's revenue and profit growth trends.
    Useful for assessing financial performance and identifying growth patterns.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :param condensed: If True, return compact tuple format. Defaults to True.
    :return: Income statement growth data or None if request fails.
    :example: income_statement_growth('AAPL', limit=5)
    """
    path = f"income-statement-growth/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
    }
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)


def balance_sheet_statement_growth(
    symbol: str,
    limit: int = DEFAULT_LIMIT,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Retrieve balance sheet statement growth metrics for a company.

    Provides insights into a company's assets, liabilities, and equity growth.
    Useful for assessing financial health and long-term stability.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :param condensed: If True, return compact tuple format. Defaults to True.
    :return: Balance sheet growth data or None if request fails.
    :example: balance_sheet_statement_growth('AAPL', limit=5)
    """
    path = f"balance-sheet-statement-growth/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
    }
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)


def cash_flow_statement_growth(
    symbol: str,
    limit: int = DEFAULT_LIMIT,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Retrieve cash flow statement growth metrics for a company.

    Provides insights into a company's cash inflows and outflows growth.
    Useful for assessing liquidity and financial flexibility.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :param condensed: If True, return compact tuple format. Defaults to True.
    :return: Cash flow statement growth data or None if request fails.
    :example: cash_flow_statement_growth('AAPL', limit=5)
    """
    path = f"cash-flow-statement-growth/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
    }
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)


def financial_ratios_ttm(
    symbol: str,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Retrieve trailing twelve months (TTM) financial ratios for a company.

    Provides insights into a company's current financial performance and efficiency.
    Useful for comparing with industry averages and identifying areas for improvement.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param condensed: If True, return compact tuple format. Defaults to True.
    :return: TTM financial ratios data or None if request fails.
    :example: financial_ratios_ttm('AAPL')
    """
    path = f"ratios-ttm/{symbol}"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)


def financial_ratios(
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Retrieve financial ratios for a company.

    Provides insights into a company's financial performance and efficiency.
    Useful for comparing with industry averages and identifying areas for improvement.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param period: Reporting period ('annual' or 'quarter'). Default is 'annual'.
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :param condensed: If True, return compact tuple format. Defaults to True.
    :return: Financial ratios data or None if request fails.
    :example: financial_ratios('AAPL', period='quarter', limit=5)
    """
    path = f"ratios/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "period": __validate_period(value=period),
        "limit": limit,
    }
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)


def financial_growth(
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    condensed: bool = True
) -> typing.Union[typing.List[typing.Dict], typing.Tuple[typing.Tuple[str, ...], ...]]:
    """
    Retrieve financial growth metrics for a company.

    Provides insights into a company's overall financial performance improvement.
    Useful for assessing growth trends, comparing performance over time, and
    identifying potential investment opportunities.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param period: Reporting period ('annual' or 'quarter'). Default is 'annual'.
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :param condensed: If True, return compact tuple format. Defaults to True.
    :return: Financial growth data or None if request fails.
    :example: financial_growth('AAPL', period='quarter', limit=5)
    """
    path = f"financial-growth/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
        "period": __validate_period(value=period),
    }
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tuples(result, condensed)