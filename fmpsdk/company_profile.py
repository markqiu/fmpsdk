import logging
import typing
import os

from .settings import DEFAULT_LIMIT
from .url_methods import (
    __return_json_v3,
    __return_json_v4,
    __validate_industry,
    __validate_period,
    __validate_sector,
)
from .data_compression import format_output, apply_precision

API_KEY = os.getenv('FMP_API_KEY')


def company_profile(
    symbol: str,
    output: str = 'markdown'
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve a comprehensive overview of a company.

    Provides key information such as price, beta, market capitalization,
    description, headquarters, industry, sector, CEO, website, and more.
    Useful for identifying investment opportunities, tracking performance,
    and conducting competitive research.

    :param symbol: Ticker symbol of the company (e.g., 'AAPL').
    :param output: Output format ('tsv', 'json', or 'markdown'). Defaults to 'markdown'.
    :return: Company profile data in the specified format.
    :example: company_profile('AAPL', output='markdown')
    """
    path = f"profile/{symbol}"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return format_output(result, output)


def key_executives(
    symbol: str,
    output: str = 'markdown'
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve standardized data for key executives from SEC filings.

    Useful for analyzing corporate governance, executive incentives, and 
    comparing compensation across companies.

    :param symbol: Ticker symbol of the company (e.g., 'AAPL').
    :param output: Output format ('tsv', 'json', or 'markdown'). Defaults to 'markdown'.
    :return: Key executives data in the specified format.
    :example: key_executives('AAPL', output='markdown')
    """
    path = f"key-executives/{symbol}"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return format_output(result, output)


def company_core_information(
    symbol: str,
    output: str = 'markdown'
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve core information for a company.

    Provides a comprehensive overview of a company's basic information.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param output: Output format ('tsv', 'json', or 'markdown'). Defaults to 'markdown'.
    :return: Company core information data in the specified format.
    :example: company_core_information('AAPL', output='markdown')
    """
    path = "company-core-information"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    result = __return_json_v4(path=path, query_vars=query_vars)
    return format_output(result, output)


def enterprise_values(
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    output: str = 'markdown'
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve enterprise value data for a company.

    Provides the total value of a company, including equity and debt.
    Useful for assessing overall company value and comparing with peers.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param period: Reporting period ('annual' or 'quarter'). Default is 'annual'.
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :param output: Output format ('tsv', 'json', or 'markdown'). Defaults to 'markdown'.
    :return: Enterprise value data in the specified format.
    :example: enterprise_values('AAPL', period='quarter', limit=5, output='markdown')
    """
    path = f"enterprise-values/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "period": __validate_period(value=period),
        "limit": limit,
    }
    result = __return_json_v3(path=path, query_vars=query_vars)
    return format_output(result, output)


def key_metrics_ttm(
    symbol: str,
    limit: int = DEFAULT_LIMIT,
    output: str = 'markdown',
    precision: typing.Optional[int] = 5
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve trailing twelve months (TTM) key metrics for a company.

    Provides essential financial metrics for recent performance analysis.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :param output: Output format ('tsv', 'json', or 'markdown'). Defaults to 'markdown'.
    :param precision: Decimal places for rounding. None for full precision. Default is 5.
    :return: TTM key metrics data in the specified format.
    :example: key_metrics_ttm('AAPL', limit=5, output='markdown', precision=3)
    """
    path = f"key-metrics-ttm/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit}
    result = __return_json_v3(path=path, query_vars=query_vars)
    if result:
        result = apply_precision(result, precision)
    return format_output(result, output)


def key_metrics(
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    output: str = 'markdown',
    precision: typing.Optional[int] = 5
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve key financial metrics for a company's performance assessment.

    Provides crucial KPIs including revenue, net income, EPS, and P/E ratio.
    Useful for financial analysis, competitor comparisons, and goal tracking.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param period: Reporting period ('annual' or 'quarter'). Default is 'annual'.
    :param limit: Number of records to retrieve. Default is DEFAULT_LIMIT.
    :param output: Output format ('tsv', 'json', or 'markdown'). Defaults to 'markdown'.
    :param precision: Decimal places for rounding. None for full precision. Default is 5.
    :return: Key financial metrics in the specified format.
    :example: key_metrics('AAPL', period='quarter', limit=5, output='markdown', precision=3)
    """
    path = f"key-metrics/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "period": __validate_period(value=period),
        "limit": limit,
    }
    result = __return_json_v3(path=path, query_vars=query_vars)
    if result:
        result = apply_precision(result, precision)
    return format_output(result, output)


def company_outlook(
    symbol: str,
    output: str = 'markdown'
) -> typing.Union[typing.Dict, str]:
    """
    Retrieve the company outlook for a specific company.

    Provides insights into a company's future outlook and expectations.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param output: Output format ('tsv', 'json', or 'markdown'). Defaults to 'markdown'.
    :return: Company outlook data in the specified format.
    :example: company_outlook('AAPL', output='markdown')
    """
    path = "company-outlook"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    result = __return_json_v4(path=path, query_vars=query_vars)
    return format_output([result], output) if result else None