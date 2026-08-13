#!/usr/bin/env python3
"""Auto-setup Inception Labs Mercury-2 to 9router DB.
Injects providerNode + providerConnection without killing dashboard."""

import sqlite3
import json
import uuid
import datetime
import os
import sys

DB_PATH = "/root/.9router/db/data.sqlite"
BASE_URL = "https://api.inceptionlabs.ai/v1"
DEFAULT_MODELS = ["mercury-2"]

def main():
    api_key = os.environ.get("INCEPTION_API_KEY")
    if not api_key:
        print("ERROR: Set INCEPTION_API_KEY env var")
        print("  INCEPTION_API_KEY='sk_...' python3 setup.py")
        sys.exit(1)

    # Fetch available models from Inception API
    import urllib.request
    try:
        req = urllib.request.Request(
            f"{BASE_URL}/models",
            headers={"Authorization": f"Bearer {api_key}"}
        )
        resp = urllib.request.urlopen(req, timeout=15)
        data = json.loads(resp.read().decode())
        models = [m["id"] for m in data.get("data", [])]
        if not models:
            models = DEFAULT_MODELS
        print(f"✓ Fetched {len(models)} models from Inception API")
    except Exception as e:
        print(f"⚠ Could not fetch models ({e}), using default: {DEFAULT_MODELS}")
        models = DEFAULT_MODELS

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Generate IDs
    node_id = f"openai-compatible-chat-{uuid.uuid4().hex[:8]}"
    conn_id = str(uuid.uuid4())
    now = datetime.datetime.utcnow().isoformat() + "Z"

    # 1) Insert providerNode
    cur.execute(
        """INSERT INTO providerNodes (id, type, name, data, createdAt, updatedAt)
           VALUES (?, 'openai-compatible', ?, ?, ?, ?)""",
        (node_id, "Inception Labs",
         json.dumps({"baseUrl": BASE_URL, "description": "Inception Labs Mercury-2 dLLM"}),
         now, now)
    )
    print(f"✓ providerNode: {node_id}")

    # 2) Insert providerConnection
    conn_data = json.dumps({
        "apiKey": api_key,
        "providerSpecificData": {
            "prefix": "inception",
            "apiType": "chat",
            "baseUrl": BASE_URL,
            "nodeName": "Inception Labs",
            "models": models,
        },
        "testStatus": "available",
        "lastError": None,
    })
    cur.execute(
        """INSERT INTO providerConnections
           (id, provider, authType, name, email, priority, isActive, data, createdAt, updatedAt)
           VALUES (?, ?, 'apiKey', 'inception-mercury', 'user@inception', 0, 1, ?, ?, ?)""",
        (conn_id, node_id, conn_data, now, now)
    )
    print(f"✓ providerConnection: {conn_id}")

    # 3) Insert model registry into kv table
    for model_id in models:
        kv_key = f"{node_id}|{model_id}|llm"
        kv_val = json.dumps({
            "providerAlias": node_id,
            "id": model_id,
            "type": "llm",
            "name": model_id,
        })
        cur.execute(
            "INSERT OR REPLACE INTO kv (key, value) VALUES (?, ?)",
            (kv_key, kv_val)
        )
    print(f"✓ Registered {len(models)} models in kv table")

    conn.commit()
    conn.close()

    print(f"\n✅ DONE! Inception Labs Mercury-2 connected to 9router.")
    print(f"   Node ID: {node_id}")
    print(f"   Models: {', '.join(models)}")
    print(f"\n   Call via 9router:")
    print(f"   model: {node_id}/mercury-2")
    print(f"\n   Restart 9router gateway to load new provider:")
    print(f"   kill $(pgrep -f 'node /usr/local/bin/9router')")
    print(f"   screen -S router -X stuff '9router -p 20128\\n'")

if __name__ == "__main__":
    main()
