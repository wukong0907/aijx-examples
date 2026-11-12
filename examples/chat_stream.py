"""AIJX 流式对话示例（SSE）。

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

stream = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[{"role": "user", "content": "写一首关于秋天的五言绝句。"}],
    stream=True,
)

for chunk in stream:
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)

print()
