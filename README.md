# FMP SDK

The idea behind this project is to provide a 'one-stop-shop' to the API endpoints provided by
[Financial Model Prep](http://financialmodelingprep.com) website.

**Note: fmpsdk should be synced with FMP's API changelog as of 20210220.  Changes thereafter are not yet included.**

## How to Use

1. Install the package: `pip install fmpsdk`
1. Create a .env file and put your apikey in it.  Inside .env: `apikey='blah'`
1. Use `fmpsdk.<some function>(apikey=apikey, <possibly more variables>)` to query the API for that "some function".
1. The return from that function call is almost always a List of Dictionaries.  It is up to you to parse it.

## Example code

Here is a "quick start" script example.  A larger, more detailed example is in the file `fmpsdk-example.py`.

```python

#!/usr/bin/env python3

import os
from dotenv import load_dotenv
import typing
import fmpsdk

# Actual API key is stored in a .env file.  Not good to store API key directly in script.

# Company Valuation Methods
symbol: str = "AAPL"
print(f"Company Profile: {fmpsdk.company_profile(symbol=symbol)}")
```

## API List
好的，我将总结全部API接口的类别、名称、用途、地址和参数信息。以下是完整的表格：

| 接口类别 | 接口名称 | 用途 | 地址 | 参数 |
| --- | --- | --- | --- | --- |
| Company Search | General Search API | 搜索超过70,000个符号名称或公司名称 | https://financialmodelingprep.com/api/v3/search | {"Query Parameter": ["query*", "limit", "exchange"], "Type": ["string", "number", "string"], "Example": ["AA", "10", "NYSE"]} |
| Company Search | Ticker Search API | 通过公司名称或股票代码搜索股票代码和交易所 | https://financialmodelingprep.com/api/v3/search-ticker | {"Query Parameter": ["query*"], "Type": ["string"], "Example": ["AAPL"]} |
| Company Search | Name Search API | 通过公司名称搜索股票代码和交易所信息 | https://financialmodelingprep.com/api/v3/search-name | {"Query Parameter": ["query*"], "Type": ["string"], "Example": ["Apple Inc."]} |
| Company Search | CIK Name Search API | 通过公司名称发现SEC注册实体的CIK号码 | https://financialmodelingprep.com/api/v3/search-cik-name | {"Query Parameter": ["query*"], "Type": ["string"], "Example": ["Apple Inc."]} |
| Company Search | CIK Search API | 使用CIK号码快速找到SEC注册实体关联的公司名称 | https://financialmodelingprep.com/api/v3/search-cik | {"Path Parameter": ["cik*"], "Type": ["string"], "Example": ["0000320187"]} |
| Company Search | Cusip Search API | 通过CUSIP号码访问有关金融工具和证券的信息 | https://financialmodelingprep.com/api/v3/search-cusip | {"Path Parameter": ["cusip*"], "Type": ["string"], "Example": ["037833100"]} |
| Company Search | ISIN Search API | 通过ISIN代码找到有关金融工具和证券的信息 | https://financialmodelingprep.com/api/v3/search-isin | {"Path Parameter": ["isin*"], "Type": ["string"], "Example": ["US0378331005"]} |
| Stock List | Symbol List API | 查找交易和非交易股票的符号 | /stock/list |  |
| Stock List | Exchange Traded Fund Search API | 查找任何ETF的符号 | /etf/list |  |
| Stock List | Statement Symbols List API | 查找所有公司财务报表可用的符号 | /stock/financials |  |
| Stock List | Tradable Search API | 查找所有活跃交易股票 | /stock/trading |  |
| Stock List | Commitment of traders report API | 获取交易者承诺报告 | /futures/cot |  |
| Stock List | CIK List API | 获取SEC注册实体的CIK号码数据库 | /stock/cik |  |
| Stock List | Euronext Symbols API | 查找在Euronext交易所交易的所有股票符号 | /stock/euronext |  |
| Stock List | Symbol Changes API | 跟踪由于合并、收购、股票分割和名称更改导致的股票符号更改 | /stock/symbol-changes |  |
| Stock List | Exchange Symbols API | 包括FMP涵盖的所有选定交易所的股票符号列表 | /stock/exchange | exchange: Exchange symbol* |
| Stock List | Available Indexes API | 提供所有可用指数的列表 | /index/list |  |
| Company Information | Company Profile API | 获取公司的全面概述 | /company/profile | symbol* |
| Company Information | Executive Compensation API | 了解公司如何补偿其高管 | /company/compensation | symbol* |
| Company Information | Compensation Benchmark API | 将公司的高管薪酬与同行业其他公司进行比较 | /company/comp-benchmark | symbol* |
| Company Information | Company Notes API | 通过公司在财务报表中报告的注释来了解公司的财务状况、运营和风险 | /company/notes | symbol* |
| Company Information | Historical Employee API | 追踪公司员工人数随时间的变化 | /company/employees-historical | symbol* |
| Company Information | Employee Count API | 获取公司当前员工人数 | /company/employees | symbol* |
| Company Information | Screener (Stock) API | 根据各种标准搜索股票 | /stock/screener |  |
| Company Information | Stock Grade API | 获取由对冲基金、投资公司和分析师给出的公司评级 | /stock/grade | symbol* |
| Company Information | Executives API | 获取公司高管的详细信息 | /company/executives | symbol* |
| Company Information | Company Core Information Summary API | 验证公司身份或查找有关公司的其他信息 | /company/core-information | symbol* |
| Company Information | Market Cap API | 提供公司的当前市值 | /company/market-cap | symbol* |
| Company Information | Historical Market Cap API | 提供公司的历史市值数据 | /company/historical-market-cap | symbol*, from, to |
| Company Information | All Countries API | 提供所有交易股票的国家列表 | /stock/countries |  |
| Company Information | Analyst Estimates API | 提供分析师对公司未来收益和收入预测 | /company/estimates | symbol* |
| Company Information | Analyst Recommendation API | 提供分析师对公司股票的买卖或持有建议 | /company/recommendation | symbol* |
| Company Information | Company Logo API | 提供公司标志的图像 | /company/logo | symbol* |
| Company Information | Company Outlook API | 提供公司的概况，包括其概况信息、最新的内部交易和财务报表 | /company/outlook | symbol* |
| Company Information | Stock Peers API | 提供在同一交易所交易、处于相同行业并具有相似市值的公司组 | /stock/peers | symbol* |
| Company Information | Holidays and Trading Hours API | 提供美国市场和EURONEXT等的开放或关闭信息 | /market/open |  |
| Company Information | All Exchanges Trading Hours API | 提供美国市场和所有其他交易所的开放或关闭信息 | /market/open/all |  |
| Company Information | Delisted Companies API | 提供从美国交易所退市的公司列表 | /stock/delisted |  |
| Company Information | Company Share Float API | 提供给定公司的公开交易股份总数 | /company/share-float | symbol* |
| Company Information | Historical Share Float API | 提供给定公司公开交易股份数量的历史数据 | /company/historical-share-float | symbol*, from, to |
| Company Information | All Shares Float API | 提供可供交易的股份数量，包括受限股份单元(RSUs) | /stock/float |  |
| Company Information | All Available Sectors API | 提供FMP数据库中所有可用行业列表 | /stock/sectors |  |
| Company Information | All Available Industries API | 提供FMP数据库中所有可用行业的列表 | /stock/industries |  |
| Company Information | All Available Exchanges API | 提供FMP数据库中所有可用交易所的列表 | /stock/exchanges |  |
| Quote | Full Quote API | 获取股票的最新出价和要价价格，以及成交量和最后交易价格 | /quote/endpoint | symbol* |
| Quote | Quote Order API | 提供股票报价的简化视图，包括当前价格、成交量和最后交易价格 | /quote-order | symbol* |
| Quote | Simple Quote API | 获取股票的简单报价，包括价格、变动和成交量 | /simple-quote | symbol* |
| Quote | OTC Quote API | 获取场外交易（OTC）股票的最新出价和要价价格，以及成交量和最后交易价格 | /otc-quote | symbol* |
| Quote | Exchange Prices API | 提供特定交易所所有股票的实时价格 | /exchange-prices | symbol* |
| Quote | Stock Price Change API | 获取一段时间内股票价格的变动 | /price-change | symbol*, from, to |
| Quote | Aftermarket Trade API | 获取在盘后交易中发生的交易信息 | /aftermarket-trade | symbol* |
| Quote | Aftermarket Quote API | 获取股票在盘后的最新出价和要价价格 | /aftermarket-quote | symbol* |
| Quote | Batch Quote API | 一次性获取多只股票的报价 | /batch-quote | symbols* |
| Quote | Batch Trade API | 一次性获取多只股票的交易信息 | /batch-trade | symbols* |
| Quote | Last Forex API | 获取货币对的最新价格 | /last-forex | symbol* |
| Quote | Last Crypto API | 获取加密货币的最新价格 | /last-crypto | symbol* |
| Quote | Live Full Price w/ Orders API | 获取股票的最新出价、要价、成交量和最后交易价格 | /live-full-price-orders | symbol* |
| Quote | All Live Full Price w/ Orders API | 获取所有股票的实时全价列表 | /all-live-full-price-orders |  |
| Quote | Forex Prices API | 获取货币对的最新出价和要价价格 | /forex-prices | symbol* |
| Quote | All Forex Prices API | 获取所有外汇（FX）价格列表 | /all-forex-prices |  |
| Financial Statements | Income Statements API | 提供公司实时损益表数据 | /financials/income-statement | symbol*, limit |
| Financial Statements | Balance Sheet Statements API | 提供公司的资产负债表 | /financials/balance-sheet | symbol*, limit |
| Financial Statements | Cashflow Statements API | 提供公司的现金流量表 | /financials/cash-flow | symbol*, limit |
| Financial Statements | Income Statements As Reported API | 获取公司报告的未经调整的损益表 | /financials/income-statement-as-reported | symbol*, limit |
| Financial Statements | Balance Sheet Statements As Reported API | 获取公司报告的未经调整的资产负债表 | /financials/balance-sheet-as-reported | symbol*, limit |
| Financial Statements | Cashflow Statements As Reported API | 获取公司报告的未经调整的现金流量表 | /financials/cash-flow-as-reported | symbol*, limit |
| Financial Statements | Full Financial Statements As Reported API | 获取公司报告的所有三种财务报表（损益表、资产负债表和现金流量表） | /financials/full-statements-as-reported | symbol*, limit |
| Financial Statements | List of dates and Links API | 提供公司财务报表可用的所有日期列表 | /financials/dates | symbol* |
| Financial Statements | Annual Reports on Form 10-K API | 提供公司的年度报告10-K | /financials/form-10k | symbol*, limit |
| Statement Analysis | Key Metrics API | 获取公司的关键财务指标 | /financials/key-metrics | symbol* |
| Statement Analysis | Key Metrics TTM API | 获取公司过去十二个月的关键财务指标 | /financials/key-metrics-ttm | symbol* |
| Statement Analysis | Ratios API | 获取公司的财务比率 | /financials/ratios | symbol* |
| Statement Analysis | Ratios TTM API | 获取公司过去十二个月的财务比率 | /financials/ratios-ttm | symbol* |
| Statement Analysis | Cashflow Growth API | 获取公司的现金流增长率 | /financials/cash-flow-growth | symbol* |
| Statement Analysis | Income Growth API | 获取公司的收入增长率 | /financials/income-growth | symbol* |
| Statement Analysis | Balance Sheet Growth API | 获取公司资产负债表增长率 | /financials/balance-sheet-growth | symbol* |
| Statement Analysis | Financial Growth API | 获取公司整体财务表现的增长率 | /financials/financial-growth | symbol* |
| Statement Analysis | Financial Score API | 获取公司的财务评分 | /financials/score | symbol* |
| Statement Analysis | Owner Earnings API | 获取公司所有者收益 | /financials/owner-earnings | symbol* |
| Statement Analysis | Enterprise Values API | 获取公司的企业价值 | /financials/enterprise-values | symbol* |
| Valuation | Discounted Cashflow API | 获取公司的折现现金流估值 | /valuation/discounted-cash-flow | symbol* |
| Valuation | Advanced DCF API | 使用高级功能计算公司的DCF估值 | /valuation/advanced-DCF | symbol* |
| Valuation | Levered DCF API | 考虑公司债务水平的DCF估值 | /valuation/levered-DCF | symbol* |
| Valuation | Company Rating API | 基于财务报表、DCF分析、财务比率和内在价值提供公司评级 | /valuation/rating | symbol* |
| Valuation | Historical Rating API | 提供公司的历史评级 | /valuation/historical-rating | symbol*, from, to |
| Price Target | Price Targets API | 获取公司的股价目标 | /price-target | symbol* |
| Price Target | Price Target Summary API | 获取不同分析师对公司股价目标的汇总 | /price-target/summary | symbol* |
| Price Target | Price Target By Name API | 获取特定分析师对公司的股价目标 | /price-target/byname | symbol*, analyst_name* |
| Price Target | Price Target By Company API | 获取特定行业或领域内所有公司的股价目标 | /price-target/bycompany | industry* |
| Price Target | Price Target Consensus API | 获取所有分析师对公司股价目标的共识 | /price-target/consensus | symbol* |
| Price Target | Price Target RSS Feed API | 获取公司股价目标更新的RSS源 | /price-target/rss | symbol* |
| Upgrades & Downgrades | Upgrades & Downgrades API | 获取不同分析师对股票的升级和降级列表 | /upgrades-downgrades |  |
| Upgrades & Downgrades | Upgrades & Downgrades RSS Feed API | 订阅不同分析师对股票的升级和降级的RSS源 | /upgrades-downgrades/rss |  |
| Upgrades & Downgrades | Upgrades & Downgrades Consensus API | 获取公司股票的共识评级 | /upgrades-downgrades/consensus | symbol* |
| Upgrades & Downgrades | Upgrades & Downgrades By Company API | 获取特定公司所有股票的升级和降级列表 | /upgrades-downgrades/bycompany | symbol* |
| News | FMP Articles API | 获取Financial Modeling Prep的最新文章列表 | /news/fmp-articles |  |
| News | General News API | 获取各种来源的最新一般新闻文章列表 | /news/general |  |
| News | Stock News API | 获取各种来源的最新股票新闻文章列表 | /news/stock | symbol* |
| News | Stock News Sentiments RSS Feed API | 获取包含情感分析的最新股票新闻文章的RSS源 | /news/stock-sentiments-rss | symbol* |
| News | Forex News API | 获取各种来源的最新外汇新闻文章列表 | /news/forex |  |
| News | Crypto News API | 获取各种来源的最新加密货币新闻文章列表 | /news/crypto | symbol* |
| News | Press Releases API | 获取各种公司的新闻稿 | /news/press-releases |  |
| News | Press Releases By Symbol API | 获取特定公司的新闻稿 | /news/press-releases/{symbol} | symbol* |
| News | Historical Social Sentiment API | 提供给定股票或公司名称的历史社交情绪数据 | /sentiment/historical | symbol* |
| News | Trending Social Sentiment API | 提供给定股票或公司名称的趋势社交情绪数据 | /sentiment/trending | symbol* |
| News | Social Sentiment Changes API | 提供给定股票或公司名称的社交情绪变化数据 | /sentiment/changes | symbol* |
| Earnings Transcripts | Earnings Transcript API | 获取特定公司收益电话会议的文字记录 | /earnings-transcripts | symbol* |
| Earnings Transcripts | Transcript Dates API | 获取特定公司所有收益电话会议日期的列表 | /earnings-transcripts/dates | symbol* |
| Earnings Transcripts | Batch Earning Call Transcript API | 批量获取多个公司收益电话会议的文字记录 | /earnings-transcripts/batch | symbols* |
| Securities and Exchange Commission (S.E.C) | RSS Feed API | 实时获取SEC文件的源 | /sec-filings/rss |  |
| Securities and Exchange Commission (S.E.C) | RSS Feed V3 API | 实时获取SEC文件的最新RSS源（版本3） | /sec-filings/rss/v3 |  |
| Securities and Exchange Commission (S.E.C) | RSS Feed All API | 实时获取所有SEC文件的最新RSS源 | /sec-filings/rss/all |  |
| Securities and Exchange Commission (S.E.C) | RSS Feed 8-K API | 实时获取8-K SEC文件的RSS源 | /sec-filings/rss/8-k |  |
| Securities and Exchange Commission (S.E.C) | SEC Filings API | 获取SEC文件的直接链接 | /sec-filings | symbol*, filing_type* |
| Securities and Exchange Commission (S.E.C) | Individual Industry Classification API | 根据SIC系统识别特定公司的行业 | /industry-classification/individual | symbol* |
| Securities and Exchange Commission (S.E.C) | All Industry Classification API | 获取SIC系统下所有行业的概览 | /industry-classification/all |  |
| Securities and Exchange Commission (S.E.C) | Industry Classification Codes API | 了解SIC系统并识别特定行业的SIC代码 | /industry-classification/codes |  |
| Earnings | Earnings Calendar API | 获取公开交易公司即将到来的和过去的收益公告列表 | /earnings/calendar |  |
| Earnings | Earnings Historical & Upcoming API | 获取特定公司的历史和即将到来的收益公告 | /earnings/historical-upcoming | symbol* |
| Earnings | Earnings Confirmed API | 获取已经确认的收益公告列表 | /earnings/confirmed |  |
| Earnings | Earnings Surprises API | 获取收益公告的正面或负面惊喜列表 | /earnings/surprises |  |
| Dividends | Dividends Calendar API | 获取即将到来的公开交易公司的股息支付列表 | /dividends/calendar |  |
| Dividends | Dividends Historical API | 获取公开交易公司的历史股息支付列表 | /dividends/historical | symbol* |
| Splits | Splits Calendar API | 获取即将到来的公开交易公司的股票分割列表 | /splits/calendar |  |
| Splits | Splits Historical API | 获取公开交易公司的历史股票分割列表 | /splits/historical | symbol* |
| IPO Calendar | IPO Confirmed API | 获取已确认且即将进行的IPO列表 | /ipo/confirmed |  |
| IPO Calendar | IPO Prospectus API | 获取给定公司的IPO招股书链接 | /ipo/prospectus | symbol* |
| IPO Calendar | IPO Calender By Symbol API | 获取特定公司已确认且即将进行的IPO列表 | /ipo/calendar-by-symbol | symbol* |
| Mergers & Acquisitions | M&A RSS Feed API | 实时获取并购新闻和公告的RSS源 | /m-and-a/rss |  |
| Mergers & Acquisitions | Search M&A API | 允许用户根据各种标准搜索并购交易 | /m-and-a/search |  |
| Stock Historical Price | Intraday Chart API | 提供给定公司的日内图表 | /historical-chart/intraday | symbol*, time_interval* |
| Stock Historical Price | Daily Chart EOD API | 提供给定公司的每日股票数据 | /historical-chart/daily | symbol*, from, to |
| Technical Indicators | Simple Moving Average API | 提供给定期间的简单移动平均线 | /technical-indicators/sma | symbol*, interval, time_period |
| Technical Indicators | Exponential Moving Average API | 提供给定期间的指数移动平均线 | /technical-indicators/ema | symbol*, interval, time_period |
| Technical Indicators | Weighted Moving Average API | 提供给定期间的加权移动平均线 | /technical-indicators/wma | symbol*, interval, time_period |
| Technical Indicators | Double EMA API | 提供给定期间的双指数移动平均线 | /technical-indicators/dema | symbol*, interval, time_period |
| Technical Indicators | Triple EMA API | 提供给定期间的三重指数移动平均线 | /technical-indicators/tema | symbol*, interval, time_period |
| Technical Indicators | Williams API | 提供给定期间的威廉指标 | /technical-indicators/williams | symbol*, interval, time_period |
| Technical Indicators | Relative Strength Index API | 提供给定期间的相对强弱指数 | /technical-indicators/rsi | symbol*, interval, time_period |
| Technical Indicators | Average Directional Index API | 提供给定期间的平均方向性指数 | /technical-indicators/adx | symbol*, interval, time_period |
| Technical Indicators | Standard Deviation API | 提供给定期间的收盘价标准差 | /technical-indicators/stddev | symbol*, interval, time_period |
| ETF Holdings | ETF Holding dates API | 提供ETF持仓更新的日期列表 | /etf/holding-dates | symbol* |
| ETF Holdings | ETF Holdings API | 提供特定ETF的所有机构投资者列表 | /etf/holdings | symbol*, date* |
| ETF Holdings | ETF Holder API | 返回特定ETF持有的所有股票 | /etf/holder | symbol*, date* |
| ETF Holdings | ETF Information API | 提供ETF的基本信息 | /etf/info | symbol* |
| ETF Holdings | ETF Sector Weighting API | 提供ETF资产在各个行业的投资比例 | /etf/sector-weighting | symbol* |
| ETF Holdings | ETF Country Weighting API | 提供ETF资产在各国的投资比例 | /etf/country-weighting | symbol* |
| ETF Holdings | ETF Stock Exposure API | 返回ETF持仓的所有股票的市值、持股数量或权重百分比 | /etf/stock-exposure | symbol*, date* |
| Mutual Funds Holdings | Mutual Fund dates API | 提供共同基金持仓更新的日期列表 | /mutual-fund/dates | symbol* |
| Mutual Funds Holdings | Mutual Funds API | 提供所有注册SEC的共同基金列表 | /mutual-fund/list |  |
| Mutual Funds Holdings | Mutual Fund by name API | 提供特定共同基金的详细信息 | /mutual-fund/name | symbol* |
| Mutual Funds Holdings | Mutual Fund Holder API | 提供特定共同基金的所有机构投资者列表 | /mutual-fund/holder | symbol* |
| ESG | ESG Search API | 根据ESG评级、表现、争议和商业参与筛选公司和基金 | /esg/search |  |
| ESG | ESG Ratings API | 获取公司和基金的ESG评级 | /esg/ratings | symbol* |
| ESG | ESG Benchmark API | 将公司和基金的ESG表现与同行比较 | /esg/benchmark | symbol* |
| Senate | Senate trading API | 追踪美国参议员的交易活动 | /senate/trading |  |
| Senate | Senate trading RSS Feed API | 实时获取参议员交易活动的RSS源 | /senate/trading-rss |  |
| Senate | House Disclosure API | 获取众议院议员的财务披露信息 | /house/disclosure |  |
| Senate | House Disclosure RSS Feed API | 实时获取众议院议员财务披露的RSS源 | /house/disclosure-rss |  |
| Market Performance | Market Index API | 提供所有主要股票市场指数列表 | /market/index |  |
| Market Performance | Sector PE Ratio API | 提供每个行业的股票市场市盈率 | /market/sector-pe-ratio |  |
| Market Performance | Industry PE Ratio API | 提供每个行业的市盈率 | /market/industry-pe-ratio |  |
| Market Performance | Sector Performance API | 提供每个行业的股票市场表现 | /market/sector-performance |  |
| Market Performance | Sector Historical API | 提供每个行业的历史股票市场表现 | /market/sector-historical |  |
| Market Performance | Market Biggest Gainers API | 提供当天涨幅最大的股票列表 | /market/gainers |  |
| Market Performance | Market Biggest Losers API | 提供当天跌幅最大的股票列表 | /market/losers |  |
| Market Performance | Market Most Active API | 提供当天交易量最大的股票列表 | /market/most-actives |  |
| Market Performance | Analysis By Symbol API | 提供给定符号的交易者承诺(COT)报告分析 | /market/cot-analysis-by-symbol | symbol* |
| Market Performance | Analysis By Dates API | 提供给定日期范围的交易者承诺(COT)报告分析 | /market/cot-analysis-by-dates | start_date*, end_date* |
| Market Performance | Report By Symbol API | 提供给定符号的完整交易者承诺(COT)报告 | /market/cot-report-by-symbol | symbol* |
| Market Performance | Report By Dates API | 提供给定日期范围的完整交易者承诺(COT)报告 | /market/cot-report-by-dates | start_date*, end_date* |
| 13F - Institutional Stock Ownership | Form 13F API | 提供管理资产超过1亿美元的机构投资者季度报告 | /institutional/13f-forms |  |
| 13F - Institutional Stock Ownership | Form 13F dates API | 提供13F报告的提交日期 | /institutional/13f-forms-dates |  |
| 13F - Institutional Stock Ownership | 13F Asset Allocation API | 提供机构投资者的资产配置 | /institutional/13f-asset-allocation | cik* |
| 13F - Institutional Stock Ownership | 13F Asset Allocation dates API | 提供13F资产配置数据更新的日期 | /institutional/13f-asset-allocation-dates |  |
| 13F - Institutional Stock Ownership | Institutional Holders List API | 提供需要提交13F报告的所有机构投资者列表 | /institutional/holders-list |  |
| 13F - Institutional Stock Ownership | Institutional Holders Search API | 通过名称、股票代码或CUSIP号搜索机构投资者 | /institutional/holders-search | query* |
| 13F - Institutional Stock Ownership | Portfolio Holdings dates API | 提供投资组合持仓数据更新的日期 | /institutional/portfolio-holdings-dates | cik* |
| 13F - Institutional Stock Ownership | Institutional Holder RSS API | 提供机构投资者数据的RSS源 | /institutional/holders-rss |  |
| 13F - Institutional Stock Ownership | Institutional Stock Ownership API | 提供个别股票的机构持股信息 | /institutional/stock-ownership | symbol* |
| 13F - Institutional Stock Ownership | Stock Ownership By Holders API | 提供个别持有人（包括机构和个人投资者）的股票持有信息 | /institutional/ownership-by-holder | cik* |
| 13F - Institutional Stock Ownership | Portfolio Holdings Summary API | 提供投资组合持仓的摘要，包括顶级持仓、行业配置和行业配置 | /institutional/portfolio-summary | cik* |
| 13F - Institutional Stock Ownership | Industry Ownership Summary API | 提供行业所有权的摘要，包括顶级行业和每个行业的机构持股 | /institutional/industry-ownership-summary |  |
| 13F - Institutional Stock Ownership | Ownership By Shares Held API | 提供按持股数量持有的股票所有权 | /institutional/ownership-by-shares-held | symbol* |
| 13F - Institutional Stock Ownership | Portfolio Composition API | 提供投资组合的构成，包括资产配置、行业配置和行业配置 | /institutional/portfolio-composition | cik* |
| 13F - Institutional Stock Ownership | Institutional Holder API | 提供有关个别机构投资者的详细信息，包括持股、联系信息和投资风格 | /institutional/holder | cik* |
| Fundraising | Crowdfunding RSS API | 实时获取众筹活动的RSS源 | /crowdfunding/rss |  |
| Fundraising | Crowdfunding Search API | 通过公司名称、活动名称或平台搜索众筹活动 | /crowdfunding/search | query* |
| Fundraising | Crowdfunding By CIK API | 获取特定公司发起的所有众筹活动列表 | /crowdfunding/by-cik | cik* |
| Fundraising | Equity Offering RSS API | 实时获取股权发行公告的RSS源 | /equity-offering/rss |  |
| Fundraising | Equity Offering Search API | 通过公司名称、发行名称或交易所搜索股权发行 | /equity-offering/search | query* |
| Fundraising | Equity Offering By CIK API | 获取特定公司宣布的所有股权发行列表 | /equity-offering/by-cik | cik* |
| Economics Data | Treasury Rates API | 提供所有到期日的实时和历史国债利率 | /economic/treasury-rates |  |
| Economics Data | Economic Indicators API | 提供各种经济指标的实时和历史经济数据 | /economic/indicators |  |
| Economics Data | Economics Calendar API | 提供即将发布的经济数据日历 | /economic/calendar |  |
| Economics Data | Market Risk Premium API | 提供给定日期的市场风险溢价 | /economic/risk-premium | date* |
| Commodities | Commodities List API | 提供全球交易所交易的所有商品列表 | /commodities/list |  |
| Commodities | Full Commodities Quote List API | 提供全球交易所交易的所有商品的报价列表 | /commodities/quotes |  |
| Commodities | Full Commodities Quote API | 提供全球交易所交易的所有商品的实时报价 | /commodities/quote | symbol* |
| Commodities | Intraday Commodities API | 提供全球交易所交易的所有商品的日内价格数据 | /commodities/intraday | symbol* |
| Commodities | Commodities Daily API | 提供全球交易所交易的所有商品的每日价格数据 | /commodities/daily | symbol* |
| Forex | Forex List API | 提供外汇市场上交易的所有货币对列表 | /forex/list |  |
| Forex | Full Forex Quote List API | 提供外汇市场上所有货币对的报价列表 | /forex/quotes |  |
| Forex | Full Forex Quote API | 提供特定货币对的完整报价 | /forex/quote | symbol* |
| Forex | Intraday Forex API | 提供特定货币对的日内价格数据 | /forex/intraday | symbol* |
| Forex | Forex Daily API | 提供外汇市场上所有货币对的每日价格数据 | /forex/daily | symbol* |
| Websocket | Company Web Socket API | 提供股票价格和报价数据的实时流 |  |  |
| Websocket | Crypto Web Socket API | 提供加密货币价格和报价数据的实时流 |  |  |
| Websocket | Forex Web Socket API | 提供外汇价格和报价数据的实时流 |  |  |
| Bulk Requests | Batch Quote API | 一次性获取多只股票的报价 | /bulk-quote/endpoint | symbols* |
| Bulk Requests | Batch Trade API | 一次性获取多只股票的交易信息 | /bulk-trade/endpoint | symbols* |
| Bulk Requests | ETF Holdings API | 一次性获取多个ETF的持仓信息 | /bulk-etf-holdings/endpoint | symbols* |
| Bulk Requests | Mutual Funds API | 一次性获取多个共同基金的信息 | /bulk-mutual-fund/endpoint | symbols* |

### 参数说明：
- `symbols*`: 必需参数，表示一个包含多个股票、ETF或共同基金符号的数组。

### 批量请求的一般步骤：
1. **构建请求**：用户需要构建一个包含所有所需数据符号的数组，并发送到相应的批量请求端点。
2. **发送请求**：通过API发送请求。
3. **处理响应**：API将返回一个包含所有请求数据的响应。

### 示例：
假设用户想要一次性获取苹果（Apple）、微软（Microsoft）和亚马逊（Amazon）的股票报价，可以使用Batch Quote API：

**请求参数**：
```json
{
  "symbols": ["AAPL", "MSFT", "AMZN"]
}
```

**发送到**：
```
https://financialmodelingprep.com/api/v3/bulk-quote
```

### 注意事项：
- 批量请求通常有符号数量的限制，用户需要参考API文档确定一次请求中最多可以包含多少个符号。
- 批量请求的响应可能包含所有请求的数据，或者在某些错误的情况下，只包含部分数据。

如果您需要更详细的信息或示例代码来实现批量请求，请告知，我将提供进一步的帮助。

Websocket接口允许用户通过建立一个持久的连接来接收实时数据更新。这些接口通常需要特定的编程逻辑来建立和维护连接，以及处理接收到的数据。

请注意，Websocket接口的地址可能需要根据实际的API文档进行获取，并且通常需要一个有效的API密钥进行身份验证。

这些Websocket接口的参数可能包括：

- `apiKey`: 用户的API密钥，用于身份验证。
- `ticker`: 用户希望订阅其价格和报价数据的股票、加密货币或外汇的符号。

例如，要订阅Apple股票（AAPL）的实时数据，用户可能需要发送一个包含以下数据的WebSocket消息：

```json
{
  "event": "subscribe",
  "data": { "ticker": ["aapl"] }
}
```

这将启动一个流，推送AAPL股票的实时报价和交易数据。

请注意，表中的参数列中的"*"表示该参数是必需的。参数的类型和示例值仅供参考，实际调用时需要根据API文档提供正确的值。

## Attribution

Special thanks to the following people who have pitched in on this project!  Open source works thanks to people who jump in and help!  These are this project's stars.  Thank you.

- [Ken Caruso](https://github.com/ipl31)
- [iforgotmypass](https://github.com/iforgotmypass)
- [Ivelin Ivanov](https://github.com/ivelin)
- [David Rodriguez](https://github.com/dwrod)
