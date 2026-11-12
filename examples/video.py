"""AIJX 文生视频示例。

说明：OpenAI Python SDK 目前没有 videos 资源，因此这里直接用 HTTP 调用
（与 rerank.py 一致），不需要额外依赖。

运行前：
    export AIJX_API_KEY="sk-xxxxxxxx"

注意：视频生成通常是长耗时任务，多数模型返回任务 id，需要再轮询查询结果；
      具体字段请以控制台「模型广场」中该模型的接口说明为准。
"""
import json
import os
import urllib.request

API_KEY = os.environ["AIJX_API_KEY"]
BASE = "https://www.junxinlianke.cn/v1"

body = {
    "model": "wan2.6",  # 换成任意已上架的视频生成模型
    "prompt": "一只柴犬在樱花树下奔跑，镜头跟随，柔和的光线",
}

req = urllib.request.Request(
    BASE + "/videos/generations",
    data=json.dumps(body).encode(),
    headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
)

resp = json.loads(urllib.request.urlopen(req, timeout=120).read())
print(json.dumps(resp, ensure_ascii=False, indent=2))
