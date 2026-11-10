# AIJX 开放平台 · 接入示例仓库

> 钧信联科 AIJX 开放平台：一个 Key，调用 Claude / GPT / Gemini / DeepSeek / 通义千问 等国内外主流大模型，OpenAI 兼容接口，无需逐家注册对接。

## 快速开始

```bash
# 1. 控制台创建 API Key
#    https://www.junxinlianke.cn/console/keys
#    得到形如 sk-xxxxxxxx 的密钥

# 2. 设置环境变量
export AIJX_API_KEY="sk-xxxxxxxx"
export AIJX_BASE_URL="https://www.junxinlianke.cn/v1"
```

## 一分钟跑通（Python）

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-xxxxxxxx",
    base_url="https://www.junxinlianke.cn/v1",
)

resp = client.chat.completions.create(
    model="deepseek-v4-pro",          # 换成任意已上架模型
    messages=[{"role": "user", "content": "用一句话介绍你自己"}],
)
print(resp.choices[0].message.content)
```

因为接口是 **OpenAI 兼容**，你现有的 OpenAI SDK 代码只需改 `base_url` 和 `api_key` 两个参数即可无缝切换。

## 支持的能力

| 能力 | 接口 | 示例 |
|---|---|---|
| 文本对话 | `POST /v1/chat/completions` | `examples/chat.py` |
| 流式对话 | `POST /v1/chat/completions` (stream) | `examples/chat_stream.py` |
| GPT-5 Responses | `POST /v1/responses` | `examples/responses.py` |
| 文生图 | `POST /v1/images/generations` | `examples/image.py` |
| 文生视频 | `POST /v1/videos/generations` | `examples/video.py` |
| 语音合成 | `POST /v1/audio/speech` | `examples/audio.py` |
| 向量嵌入 | `POST /v1/embeddings` | `examples/embeddings.py` |
| 重排序 | `POST /v1/rerank` | `examples/rerank.py` |
| 余额查询 | `GET /v1/dashboard/billing/credit_grants` | `examples/balance.py` |

## 目录结构

```
examples/
├── chat.py            # 文本对话
├── chat_stream.py     # 流式对话
├── responses.py       # GPT-5 Responses API
├── image.py           # 文生图
├── video.py           # 文生视频
├── audio.py           # 语音合成
├── embeddings.py      # 向量嵌入
├── rerank.py          # 重排序
└── balance.py         # 余额查询
```

## 常见问题

- **模型名从哪看？** 控制台「模型广场」查看完整清单与实时价格。
- **国内/海外模型区别？** 国内模型（DeepSeek/千问/GLM/Kimi/豆包）走国内账本，海外模型（Claude/GPT/Gemini/Grok）走海外账本，各自充值即可。
- **费用怎么算？** 按量扣费，实时用量明细见控制台「用量」。

## 平台入口

- 官网：https://www.junxinlianke.cn
- 控制台：https://www.junxinlianke.cn/console
