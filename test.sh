#!/bin/bash
# Test Inception Mercury-2 via 9router
# Usage: ./test.sh <9ROUTER_KEY> [NODE_ID]

KEY="${1:?Usage: ./test.sh <9ROUTER_KEY> [NODE_ID]}"
NODE_ID="${2:-openai-compatible-chat-f1e0d427}"
BASE="http://127.0.0.1:20128"

echo "=== Test 9router /v1/models ==="
curl -s -m 10 "$BASE/v1/models" \
  -H "Authorization: Bearer $KEY" | python3 -c "
import sys, json
d = json.load(sys.stdin)
models = [m['id'] for m in d.get('data', []) if 'mercury' in m.get('id','').lower()]
print(f'  Mercury models found: {models}')
" 2>/dev/null || echo "  (could not parse)"

echo ""
echo "=== Test chat completions (mercury-2) ==="
curl -s -m 60 "$BASE/v1/chat/completions" \
  -H "Authorization: Bearer $KEY" \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"$NODE_ID/mercury-2\",
    \"messages\": [{\"role\": \"user\", \"content\": \"say hello world\"}],
    \"max_tokens\": 500,
    \"stream\": false
  }" | python3 -c "
import sys, json
d = json.load(sys.stdin)
if 'error' in d:
    print(f'  ❌ Error: {d[\"error\"][\"message\"][:100]}')
else:
    c = d['choices'][0]['message']['content']
    print(f'  ✅ Response: {c!r}')
    print(f'  Model: {d[\"model\"]}')
    print(f'  Tokens: {d[\"usage\"][\"total_tokens\"]}')
"

echo ""
echo "=== Test direct Inception API ==="
curl -s -m 30 "https://api.inceptionlabs.ai/v1/chat/completions" \
  -H "Authorization: Bearer $INCEPTION_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"mercury-2","messages":[{"role":"user","content":"hi"}],"max_tokens":100}' \
  -w "\n  HTTP %{http_code}\n" 2>&1 | tail -3
