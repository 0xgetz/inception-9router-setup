# 📝 Changelog

All notable changes to **Inception Labs × 9Router Setup** are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-08-13

### 🎉 Initial Release

#### ✨ Added
- **`setup.py`** — One-command setup script
  - Auto-fetches model list from Inception Labs API
  - Auto-generates unique Node ID (`openai-compatible-chat-<uuid8>`)
  - Injects `providerNodes` + `providerConnections` into 9Router SQLite DB
  - Registers models in `kv` table for routing
  - Environment-driven (no hardcoded credentials)
- **`test.sh`** — Comprehensive test harness
  - Tests 9Router endpoint (`/v1/models` + `/v1/chat/completions`)
  - Tests direct Inception API as fallback
  - Usage: `./test.sh <9ROUTER_KEY> [NODE_ID]`
- **`models.json`** — Model metadata reference
  - Mercury-2: 128K context, 50K max output
  - Pricing: $0.25/$0.75 per 1M tokens
  - Features: tools, json_mode, structured_outputs
- **`README.md`** — Multilingual documentation
  - 🇺🇸 English (default)
  - 🇮🇩 Bahasa Indonesia
  - 🇨🇳 中文
  - 🇯🇵 日本語
  - 🇰🇷 한국어
  - 6 professional badges
  - Model comparison table
  - Architecture diagram
- **`LICENSE`** — MIT License (© 0xgetz 2026)

#### 🔧 Technical Details
- **Provider type:** `openai-compatible` (matches 9Router pattern)
- **API base:** `https://api.inceptionlabs.ai/v1`
- **Model:** `mercury-2` (diffusion LLM, 5-10× faster than GPT-4o Mini)
- **Auth:** Bearer token (`sk_...`)
- **No dashboard restart required** — DB write only

#### 📋 Repository Config
- **Visibility:** Public
- **Topics:** `9router`, `inception-labs`, `mercury-2`, `dllm`, `ai-inference`, `llm-proxy`, `openai-compatible`, `auto-setup`, `diffusion-llm`, `sqlite`, `python`, `api`

---

## 🔮 Roadmap

### [1.1.0] - Planned
- [ ] Support for **mercury-coder** (code-specialized variant)
- [ ] Multi-provider batch setup (loop through config)
- [ ] Interactive mode with model picker
- [ ] Dry-run flag (`--dry-run`)
- [ ] Webhook notification on model errors

### [1.2.0] - Future
- [ ] Docker Compose setup (9Router + this tool)
- [ ] Support for streaming responses (`stream=true`)
- [ ] Cost calculator (tokens → USD)
- [ ] Health check endpoint integration

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feat/amazing-feature`)
3. Commit changes (`git commit -m "feat: add amazing feature"`)
4. Push to branch (`git push origin feat/amazing-feature`)
5. Open a Pull Request

---

## 📜 License

MIT © 0xgetz 2026

---

<div align="center">

**[⬆ Back to Top](#-changelog)**

</div>
