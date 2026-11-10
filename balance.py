"""AIJX 余额查询示例。

运行前：
    export AIJX_API_KEY="sk-xxxxxxxx"
"""
import os
import urllib.request
import json

API_KEY = os.environ["AIJX_API_KEY"]
BASE = "https://www.junxinlianke.cn/v1"

req = urllib.request.Request(
    BASE + "/dashboard/billing/credit_grants",
    headers={"Authorization": f"Bearer {API_KEY}"},
)
resp = json.loads(urllib.request.urlopen(req).read())
print(json.dumps(resp, ensure_ascii=False, indent=2))
