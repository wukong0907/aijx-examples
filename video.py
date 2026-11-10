"""AIJX 文生视频示例。

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

resp = client.videos.generate(
    model="wan2.6",  # 或其它视频生成模型
    prompt="一只柴犬在樱花树下奔跑，镜头跟随，柔和的光线",
)

print(resp)
