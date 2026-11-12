"""AIJX 语音合成示例。

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

resp = client.audio.speech.create(
    model="tts-1",  # 或其它语音合成模型
    voice="alloy",
    input="欢迎使用 AIJX 开放平台。",
)

resp.stream_to_file("output.mp3")
print("已保存 output.mp3")
