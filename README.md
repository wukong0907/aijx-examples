# AIJX 开放平台 · 接入示例

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![OpenAI Compatible](https://img.shields.io/badge/API-OpenAI%20Compatible-10a37f.svg)](https://www.junxinlianke.cn)
[![Models](https://img.shields.io/badge/models-70%2B-8b5cf6.svg)](https://www.junxinlianke.cn)

钧信联科 **AIJX 开放平台**：一个 Key，调用 Claude / GPT / Gemini / DeepSeek / 通义千问 / Kimi / GLM 等 **70+ 国内外主流大模型**。
接口 **OpenAI 兼容**，你现有的 SDK 代码只需改 `base_url` 和 `api_key` 两个参数即可无缝切换。

## 为什么用它

对接多家模型厂商，通常要经历这套流程：逐家注册 → 逐个实名 → 分别充值 → 各自维护 SDK 和错误码 → 每家账单分开看。
模型换代时还要重来一遍。

AIJX 把它们收敛成一层：

| 痛点 | 直接对接各家 | 用 AIJX |
|---|---|---|
| 接入成本 | 每家一套 Key、一套文档 | 一个 Key，一套 OpenAI 兼容协议 |
| 充值 | 分平台、分币种 | 国内模型 / 海外模型两个账本，各自充值 |
| 切换模型 | 改代码、换 SDK | 只改 `model` 字段 |
| 账单 | 分散在多个后台 | 用量明细统一可查 |

按量计费，**用多少扣多少**，不预存不绑定。

## 免费试用

注册即送 **¥3 体验额度**（30 天有效），够跑通下面所有示例并试几个真实模型。

1. 打开 https://www.junxinlianke.cn 注册
2. 进入控制台「API Keys」创建密钥，得到 `sk-xxxxxxxx`
3. 跑下面的示例

## 快速开始

```bash
pip install openai
export AIJX_API_KEY="sk-xxxxxxxx"
```

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

## 支持的能力

| 能力 | 接口 | 示例 |
|---|---|---|
| 文本对话 | `POST /v1/chat/completions` | [`examples/chat.py`](examples/chat.py) |
| 流式对话 | `POST /v1/chat/completions` (stream) | [`examples/chat_stream.py`](examples/chat_stream.py) |
| Responses API | `POST /v1/responses` | [`examples/responses.py`](examples/responses.py) |
| 文生图 | `POST /v1/images/generations` | [`examples/image.py`](examples/image.py) |
| 文生视频 | `POST /v1/videos/generations` | [`examples/video.py`](examples/video.py) |
| 语音合成 | `POST /v1/audio/speech` | [`examples/audio.py`](examples/audio.py) |
| 向量嵌入 | `POST /v1/embeddings` | [`examples/embeddings.py`](examples/embeddings.py) |
| 重排序 | `POST /v1/rerank` | [`examples/rerank.py`](examples/rerank.py) |
| 余额查询 | `GET /v1/dashboard/billing/credit_grants` | [`examples/balance.py`](examples/balance.py) |

> 说明：`/v1/videos/generations` 与 `/v1/rerank` 没有对应的 OpenAI SDK 资源，示例里用标准 HTTP 调用，不需要额外依赖。

## 目录结构

```
examples/
├── chat.py            # 文本对话
├── chat_stream.py     # 流式对话（SSE）
├── responses.py       # Responses API
├── image.py           # 文生图
├── video.py           # 文生视频（HTTP）
├── audio.py           # 语音合成
├── embeddings.py      # 向量嵌入
├── rerank.py          # 重排序（HTTP）
└── balance.py         # 余额查询（HTTP）
```

## 常见问题

- **模型名从哪看？** 控制台「模型广场」有完整清单和实时价格。
- **国内 / 海外模型区别？** 国内模型（DeepSeek / 千问 / GLM / Kimi / 豆包）走国内账本，海外模型（Claude / GPT / Gemini / Grok）走海外账本，各自充值即可。
- **费用怎么算？** 按量扣费，实时用量明细见控制台「用量」。
- **能直接替换现有 OpenAI 代码吗？** 能。改 `base_url` 与 `api_key` 即可，`model` 换成平台上的模型名。

## 相关链接

- 官网：https://www.junxinlianke.cn
- 控制台：https://www.junxinlianke.cn/console

---

示例代码可自由取用（MIT）。发现示例有问题或想要某个语言的版本，欢迎开 Issue。
