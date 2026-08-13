# 📝 Changelog

All notable changes to **Inception Labs × 9Router Setup** are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

> **Official reference:** [Inception Labs — Get Started](https://docs.inceptionlabs.ai/get-started/get-started)

---

## [1.0.0] - 2026-08-13

### 🎉 Initial Release

#### ✨ Added
- **`setup.py`** — One-command setup script
  - Auto-fetches model list from Inception Labs API (`/v1/models`)
  - Auto-generates unique Node ID (`openai-compatible-chat-<uuid8>`)
  - Injects `providerNodes` + `providerConnections` into 9Router SQLite DB
  - Registers models in `kv` table for routing
  - Environment-driven (no hardcoded credentials)
- **`test.sh`** — Comprehensive test harness
  - Tests 9Router endpoint (`/v1/models` + `/v1/chat/completions`)
  - Tests direct Inception API as fallback
  - Usage: `./test.sh <9ROUTER_KEY> [NODE_ID]`
- **`models.json`** — Model metadata reference
- **`README.md`** — Multilingual documentation (EN, ID, ZH, JA, KO)
- **`LICENSE`** — MIT License (© 0xgetz 2026)

#### 📚 Aligned with Official Inception Docs
Based on [Get Started](https://docs.inceptionlabs.ai/get-started/get-started):

- **Base URL:** `https://api.inceptionlabs.ai/v1` (all requests)
- **Auth Header:** `Authorization: Bearer $INCEPTION_API_KEY`
- **SDK:** `pip install inceptionai` / `npm install inceptionai`
- **Free Tier:** Every new account gets **100M free tokens** — no payment required
- **Recommended Defaults** (per docs):
  - `model`: `mercury-2`
  - `temperature`: `0.75`
  - `reasoning_effort`: `medium`
  - `max_tokens`: `8192`
- **Reasoning Levels:** `instant` (ultra-low latency) → `low` → `medium` → `high` (extended thinking)
- **Third-Party Compatible:** AISuite, LiteLLM, LangChain, OpenAI Client, VercelAI

#### 🔧 Technical Details
- **Provider type:** `openai-compatible` (matches 9Router pattern)
- **Model:** `mercury-2` (diffusion LLM, 5-10× faster than GPT-4o Mini)
- **Context:** 128K | **Max output:** 50K
- **Pricing:** $0.25 input / $0.75 output per 1M tokens
- **No dashboard restart required** — DB write only

#### 📋 Repository Config
- **Visibility:** Public
- **Topics:** `9router`, `inception-labs`, `mercury-2`, `dllm`, `ai-inference`, `llm-proxy`, `openai-compatible`, `auto-setup`, `diffusion-llm`, `sqlite`, `python`, `api`

---

## 🔮 Roadmap

### [1.1.0] - Planned
- [ ] Sync defaults to official docs (`reasoning_effort: medium`, `temperature: 0.75`)
- [ ] Support **mercury-coder** (code-specialized variant)
- [ ] Multi-provider batch setup (loop through config)
- [ ] Interactive mode with model picker
- [ ] Dry-run flag (`--dry-run`)

### [1.2.0] - Future
- [ ] Docker Compose setup (9Router + this tool)
- [ ] Streaming + diffusion instant mode (`reasoning_effort: instant`)
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
