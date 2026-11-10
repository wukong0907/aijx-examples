"""AIJX GPT-5 Responses API 示例。

运行前：
    export AIJX_API_KEY="sk-xxxxxxxx"
    pip install openai
"""
import os

from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AIJX_API_KEY"],
    base_url="https://www.junxinlianke.cn/v1",
)

resp = client.responses.create(
    model="gpt-5",  # 或 gpt-5-mini 等 Responses API 模型
    input="用一句话解释什么是函数式编程。",
)

print(resp.output_text)
