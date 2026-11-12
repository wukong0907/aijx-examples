"""AIJX 重排序（Rerank）示例。

运行前：
    export AIJX_API_KEY="sk-xxxxxxxx"
    pip install openai
"""
import os
import urllib.request
import json

API_KEY = os.environ["AIJX_API_KEY"]
BASE = "https://www.junxinlianke.cn/v1"

body = {
    "model": "bge-reranker-v2-m3",  # 或其它重排序模型
    "query": "什么是向量数据库？",
    "documents": [
        "向量数据库用于存储和检索高维向量。",
        "今天天气很好。",
        "重排序模型根据相关性对候选文档排序。",
    ],
}

req = urllib.request.Request(
    BASE + "/rerank",
    data=json.dumps(body).encode(),
    headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
)
resp = json.loads(urllib.request.urlopen(req).read())
print(json.dumps(resp, ensure_ascii=False, indent=2))
