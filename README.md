# Inception Labs → 9router Auto-Setup

Auto-colok Inception Labs **Mercury-2** (diffusion LLM, 5-10x faster than GPT-4o mini) ke 9router DB. Tanpa kill dashboard.

## Quick Start

```bash
# 1. Dapat API key dari Inception Labs
#    Daftar di https://inceptionlabs.ai → dashboard → API Keys → copy sk_...

# 2. Run setup script
INCEPTION_API_KEY="sk_xxxxx" python3 setup.py
```

## Model

| Model | Type | Speed | Context |
|-------|------|-------|---------|
| `mercury-2` | dLLM (diffusion) | 5-10x faster than GPT-4o mini | 128k |

## Cara Panggil (via 9router)

```bash
curl http://localhost:20128/v1/chat/completions \
  -H "Authorization: Bearer <9ROUTER_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai-compatible-chat-<NODE_ID>/mercury-2",
    "messages": [{"role": "user", "content": "hello"}],
    "max_tokens": 500
  }'
```

> **Note:** Mercury-2 adalah diffusion LLM. Butuh `max_tokens` minimal ~200+ untuk hasil yang baik (token digunakan untuk reasoning + diffusion process).

## File

- `setup.py` — auto inject providerNode + providerConnection ke 9router DB
- `test.sh` — test endpoint via 9router
- `models.json` — model list dari Inception Labs API

## Prasyarat

- 9router jalan di port 20128
- Python 3.11+
- 9router DB di `/root/.9router/db/data.sqlite`

## License

MIT © 0xgetz 2026
