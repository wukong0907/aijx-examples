"""AIJX 向量嵌入示例。

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

resp = client.embeddings.create(
    model="text-embedding-3-small",  # 或其它嵌入模型
    input=["苹果是一种水果", "香蕉也是一种水果"],
)

for i, item in enumerate(resp.data):
    print(f"文本 {i} 向量维度: {len(item.embedding)}")
