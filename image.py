"""AIJX 文生图示例。

运行前：
    export AIJX_API_KEY="sk-xxxxxxxx"
    pip install openai requests
"""
import os

from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AIJX_API_KEY"],
    base_url="https://www.junxinlianke.cn/v1",
)

resp = client.images.generate(
    model="gpt-image-2.5-flare",  # 或其它文生图模型
    prompt="一只坐在窗边看雨的橘猫，温暖的光线，电影感",
    n=1,
    size="1024x1024",
)

# 返回的 url 为 base64 数据或图片地址，视模型而定
image = resp.data[0]
if image.url:
    print("图片地址:", image.url[:200], "...")
elif image.b64_json:
    import base64

    with open("output.png", "wb") as f:
        f.write(base64.b64decode(image.b64_json))
    print("已保存 output.png")
