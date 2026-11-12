"""AIJX 文本对话示例（OpenAI 兼容）。

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

# model 换成任意已上架模型：deepseek-v4-pro / qwen3.7-max / claude-haiku-5-5 / gpt-4o ...
resp = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "你是一名简洁、专业的技术助手。"},
        {"role": "user", "content": "用一句话介绍你自己。"},
    ],
    temperature=0.7,
    max_tokens=512,
)

print(resp.choices[0].message.content)
print("\n--- 用量 ---")
print(f"prompt_tokens:   {resp.usage.prompt_tokens}")
print(f"completion_tokens: {resp.usage.completion_tokens}")
