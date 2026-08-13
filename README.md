<div align="center">

# 🚀 Inception Labs × 9Router

### Auto-Setup Mercury-2 dLLM to 9Router

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![9Router](https://img.shields.io/badge/9Router-Compatible-purple.svg)](https://github.com/0xgetz/inception-9router-setup)
[![Private Repo](https://img.shields.io/badge/Access-Private-red.svg)](https://github.com/0xgetz/inception-9router-setup)
[![Mercury-2](https://img.shields.io/badge/Model-Mercury--2-orange.svg)](https://inceptionlabs.ai)
[![dLLM](https://img.shields.io/badge/Type-dLLM-green.svg)]()

**One command. Zero config. Instant AI inference.**

Mercury-2 is the world's first **diffusion Large Language Model (dLLM)** — 5-10× faster than GPT-4o Mini and Claude 3.5 Haiku, while matching their quality. Ranked **#1 in speed** on Copilot Arena.

</div>

---

## 🌐 README Languages

| Language | Link |
|----------|------|
| 🇺🇸 English | [Below](#-quick-start) |
| 🇮🇩 Bahasa Indonesia | [Bahasa](#-quick-start-id) |
| 🇨🇳 中文 | [中文](#-quick-start-zh) |
| 🇯🇵 日本語 | [日本語](#-quick-start-ja) |
| 🇰🇷 한국어 | [한국어](#-quick-start-ko) |

---

## ⚡ Quick Start

```bash
# 1. Get API key from Inception Labs
#    Sign up at https://inceptionlabs.ai → Dashboard → API Keys → Copy sk_...

# 2. Clone & run
git clone https://github.com/0xgetz/inception-9router-setup.git
cd inception-9router-setup
INCEPTION_API_KEY="sk_xxxxx" python3 setup.py
```

**That's it.** Provider node + connection + model registry auto-injected into 9Router DB. No dashboard restart needed.

---

## 🤖 Model

| Model | Type | Speed | Context | Max Output | Price (per 1M tokens) |
|-------|------|-------|---------|------------|----------------------|
| `mercury-2` | dLLM (Diffusion) | 5-10× faster than GPT-4o Mini | 128K | 50K | $0.25 input / $0.75 output |

> ⚠️ **Note:** Mercury-2 is a diffusion LLM — it uses a diffusion process for token generation. Set `max_tokens ≥ 200` for best results. Lower values may return empty content.

---

## 📡 Calling via 9Router

```bash
curl http://localhost:20128/v1/chat/completions \
  -H "Authorization: Bearer <9ROUTER_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "<NODE_ID>/mercury-2",
    "messages": [{"role": "user", "content": "Hello world"}],
    "max_tokens": 500
  }'
```

> Replace `<NODE_ID>` with the output from `setup.py` (e.g. `openai-compatible-chat-f1e0d427`)

---

## 🧪 Testing

```bash
# Test via 9Router
./test.sh <9ROUTER_KEY> <NODE_ID>

# Test direct Inception API
INCEPTION_API_KEY="sk_..." ./test.sh dummy
```

---

## 📁 File Structure

```
inception-9router-setup/
├── setup.py        ← Auto-inject provider to 9Router DB
├── test.sh         ← Test endpoint (9Router + direct)
├── models.json     ← Model list from Inception API
├── README.md       ← This file
└── LICENSE         ← MIT
```

---

## 🔧 Requirements

| Requirement | Version |
|-------------|---------|
| Python | 3.11+ |
| 9Router | Running on port 20128 |
| 9Router DB | `/root/.9router/db/data.sqlite` |

---

## 🔄 How It Works

```
┌─────────────┐     ┌──────────────┐     ┌───────────────────┐
│  setup.py    │────▶│  9Router DB  │────▶│  9Router Gateway  │
│  (inject)   │     │  (SQLite)    │     │  (auto-reload)    │
└─────────────┘     └──────────────┘     └───────────────────┘
       │                    │                      │
       ▼                    ▼                      ▼
  providerNode      providerConnection         /v1/models
  + kv registry     + apiKey                  /v1/chat/completions
```

1. **Fetches** model list from `https://api.inceptionlabs.ai/v1/models`
2. **Generates** unique Node ID (`openai-compatible-chat-<uuid8>`)
3. **Injects** `providerNodes` + `providerConnections` into 9Router SQLite DB
4. **Registers** models in `kv` table for routing
5. **Ready** — call via 9Router endpoint

---

<div align="center">

### Made with ❤️ by [0xgetz](https://github.com/0xgetz)

</div>

---
---

## ⚡ Quick Start (ID) <a name="quick-start-id"></a>

**Bahasa Indonesia**

```bash
# 1. Dapat API key dari Inception Labs
#    Daftar di https://inceptionlabs.ai → Dashboard → API Keys → Copy sk_...

# 2. Clone & jalankan
git clone https://github.com/0xgetz/inception-9router-setup.git
cd inception-9router-setup
INCEPTION_API_KEY="sk_xxxxx" python3 setup.py
```

**Selesai.** Provider node + koneksi + registry model otomatis di-inject ke 9Router DB. Tanpa restart dashboard.

### Memanggil via 9Router

```bash
curl http://localhost:20128/v1/chat/completions \
  -H "Authorization: Bearer <9ROUTER_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "<NODE_ID>/mercury-2",
    "messages": [{"role": "user", "content": "Halo dunia"}],
    "max_tokens": 500
  }'
```

> ⚠️ **Catatan:** Mercury-2 adalah diffusion LLM — gunakan `max_tokens ≥ 200` untuk hasil optimal.

---

## ⚡ Quick Start (ZH) <a name="quick-start-zh"></a>

**中文**

```bash
# 1. 从 Inception Labs 获取 API 密钥
#    注册 https://inceptionlabs.ai → 控制台 → API Keys → 复制 sk_...

# 2. 克隆并运行
git clone https://github.com/0xgetz/inception-9router-setup.git
cd inception-9router-setup
INCEPTION_API_KEY="sk_xxxxx" python3 setup.py
```

**完成。** Provider 节点 + 连接 + 模型注册表自动注入 9Router 数据库。无需重启仪表盘。

### 通过 9Router 调用

```bash
curl http://localhost:20128/v1/chat/completions \
  -H "Authorization: Bearer <9ROUTER_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "<NODE_ID>/mercury-2",
    "messages": [{"role": "user", "content": "你好世界"}],
    "max_tokens": 500
  }'
```

> ⚠️ **注意：** Mercury-2 是扩散语言模型 — 设置 `max_tokens ≥ 200` 以获得最佳结果。

---

## ⚡ Quick Start (JA) <a name="quick-start-ja"></a>

**日本語**

```bash
# 1. Inception Labs から API キーを取得
#    https://inceptionlabs.ai → ダッシュボード → API Keys → sk_... をコピー

# 2. クローンして実行
git clone https://github.com/0xgetz/inception-9router-setup.git
cd inception-9router-setup
INCEPTION_API_KEY="sk_xxxxx" python3 setup.py
```

**完了。** Provider ノード + 接続 + モデルレジストリが 9Router DB に自動挿入されます。ダッシュボードの再起動は不要です。

### 9Router 経由で呼び出し

```bash
curl http://localhost:20128/v1/chat/completions \
  -H "Authorization: Bearer <9ROUTER_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "<NODE_ID>/mercury-2",
    "messages": [{"role": "user", "content": "こんにちは世界"}],
    "max_tokens": 500
  }'
```

> ⚠️ **注意：** Mercury-2 は拡散言語モデルです。最適な結果を得るには `max_tokens ≥ 200` を設定してください。

---

## ⚡ Quick Start (KO) <a name="quick-start-ko"></a>

**한국어**

```bash
# 1. Inception Labs에서 API 키 가져오기
#    https://inceptionlabs.ai → 대시보드 → API Keys → sk_... 복사

# 2. 클론 후 실행
git clone https://github.com/0xgetz/inception-9router-setup.git
cd inception-9router-setup
INCEPTION_API_KEY="sk_xxxxx" python3 setup.py
```

**완료.** Provider 노드 + 연결 + 모델 레지스트리가 9Router DB에 자동 주입됩니다. 대시보드 재시작 불필요.

### 9Router를 통해 호출

```bash
curl http://localhost:20128/v1/chat/completions \
  -H "Authorization: Bearer <9ROUTER_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "<NODE_ID>/mercury-2",
    "messages": [{"role": "user", "content": "안녕하세요"}],
    "max_tokens": 500
  }'
```

> ⚠️ **참고:** Mercury-2는 확산 언어 모델입니다. 최적의 결과를 위해 `max_tokens ≥ 200`을 설정하세요.
