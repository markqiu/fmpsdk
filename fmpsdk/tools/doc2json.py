import json
from typing import Any, Dict

from openai import OpenAI
from openai.types.chat.chat_completion import Choice
from rich import print

from fmpsdk.config import settings


# search 工具的具体实现，这里我们只需要返回参数即可
def search_impl(arguments: Dict[str, Any]) -> Any:
    """
    在使用 Moonshot AI 提供的 search 工具的场合，只需要原封不动返回 arguments 即可，
    不需要额外的处理逻辑。

    但如果你想使用其他模型，并保留联网搜索的功能，那你只需要修改这里的实现（例如调用搜索
    和获取网页内容等），函数签名不变，依然是 work 的。

    这最大程度保证了兼容性，允许你在不同的模型间切换，并且不需要对代码有破坏性的修改。
    """
    return arguments


client = OpenAI(
    api_key=settings.openai.api_key,  # 在这里将 MOONSHOT_API_KEY 替换为你从 Kimi 开放平台申请的 API Key
    base_url=settings.openai.base_url,
)


def chat(messages) -> Choice:
    completion = client.chat.completions.create(
        model="moonshot-v1-128k",
        messages=messages,
        temperature=0.3,
        tools=[
            {
                "type": "builtin_function",  # <-- 使用 builtin_function 声明 $web_search 函数，请在每次请求都完整地带上 tools 声明
                "function": {
                    "name": "$web_search",
                },
            }
        ],
        response_format={"type": "json_object"},
    )
    return completion.choices[0]


messages = [
    {"role": "system", "content": "你是 Kimi。"},
]

messages.append(
    {
        "role": "user",
        "content": """
            读取https://site.financialmodelingprep.com/developer/docs的内容，把接口调用总结一个json表格，包含这些关键字：接口类别,接口名称，用途，地址，参数. 返回格式采用 json，每次输出一个类别。
            其中：
            接口类别统计第一级的分类比如General Search API和Ticker Search API都属于Company Search；
            地址那一列列出 endpoint 的信息，比如General Search API地址填写https://financialmodelingprep.com/api/v3/search ，Ticker Search API地址填写https://financialmodelingprep.com/api/v3/search-ticker。
            参数那一列要填上Parameter表格转换成json值，比如General Search API的参数是，：{"Query Parameter": ["query*", "limit", "exchange"], "Type": ["string", "number", "string"], "Example":["AA", "10", "NYSE"]
            json格式样例：
{
"Company Search": {
  "General Search API":
    {
      "用途": "Search for companies",
      "地址": "https://financialmodelingprep.com/api/v3/search",
      "参数": {
        "Query Parameter": ["query*", "limit", "exchange"],
        "Type": ["string", "number", "string"],
        "Example": ["AA", "10", "NYSE"]
      }
    },
  "Ticker Search API":
    {
      "用途": "Search for tickers",
      "地址": "https://financialmodelingprep.com/api/v3/search-ticker",
      "参数": {
        "Query Parameter": ["query*", "limit", "exchange"],
        "Type": ["string", "number", "string"],
        "Example": ["AAPL", "10", "NASDAQ"]
      }
    },
  "General Search API":
    {
        '用途': 'Search for companies',
        '地址': 'https://financialmodelingprep.com/api/v3/search',
        '参数': {
            'Query Parameter': ['query*', 'limit', 'exchange'],
            'Type': ['string', 'number', 'string'],
            'Example': ['AA', '10', 'NYSE']
        }
    },
 }
}
        """,
    }
)


finish_reason = None
while finish_reason is None or finish_reason == "tool_calls":
    choice = chat(messages)
    finish_reason = choice.finish_reason
    if finish_reason == "tool_calls":  # <-- 判断当前返回内容是否包含 tool_calls
        messages.append(
            choice.message
        )  # <-- 我们将 Kimi 大模型返回给我们的 assistant 消息也添加到上下文中，以便于下次请求时 Kimi 大模型能理解我们的诉求
        for tool_call in (
            choice.message.tool_calls
        ):  # <-- tool_calls 可能是多个，因此我们使用循环逐个执行
            tool_call_name = tool_call.function.name
            tool_call_arguments = json.loads(
                tool_call.function.arguments
            )  # <-- arguments 是序列化后的 JSON Object，我们需要使用 json.loads 反序列化一下
            if tool_call_name == "$web_search":
                tool_result = search_impl(tool_call_arguments)
            else:
                tool_result = f"Error: unable to find tool by name '{tool_call_name}'"

            # 使用函数执行结果构造一个 role=tool 的 message，以此来向模型展示工具调用的结果；
            # 注意，我们需要在 message 中提供 tool_call_id 和 name 字段，以便 Kimi 大模型
            # 能正确匹配到对应的 tool_call。
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": tool_call_name,
                    "content": json.dumps(tool_result),
                    # <-- 我们约定使用字符串格式向 Kimi 大模型提交工具调用结果，因此在这里使用 json.dumps 将执行结果序列化成字符串
                }
            )

print(choice.message.content)  # <-- 在这里，我们才将模型生成的回复返回给用户
messages.append({"role": "user", "content": "还不完整，继续输出。"})
choice = chat(messages)
print(choice.message.content)
# tables = json.loads(answer)
# rich.print(tables)
