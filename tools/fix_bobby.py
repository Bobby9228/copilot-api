import json
import sys

path = sys.argv[1] if len(sys.argv) > 1 else "/docker/openclaw-q9eh/data/.openclaw/openclaw.json"

with open(path, "r") as f:
    data = json.load(f)

openai_models = [
    {"id": "claude-haiku-4.5", "name": "0.33 Claude Haiku 4.5"},
    {"id": "claude-opus-4.5", "name": "3 Claude Opus 4.5"},
    {"id": "claude-opus-4.6", "name": "3 Claude Opus 4.6"},
    {"id": "claude-opus-4.6-fast", "name": "30 Claude Opus 4.6 (fast mode) (preview)"},
    {"id": "claude-sonnet-4", "name": "1 Claude Sonnet 4"},
    {"id": "claude-sonnet-4.5", "name": "1 Claude Sonnet 4.5"},
    {"id": "claude-sonnet-4.6", "name": "1 Claude Sonnet 4.6"},
    {"id": "gemini-2.5-pro", "name": "1 Gemini 2.5 Pro"},
    {"id": "gemini-3-flash", "name": "0.33 Gemini 3 Flash"},
    {"id": "gemini-3-pro", "name": "1 Gemini 3 Pro"},
    {"id": "gemini-3.1-pro", "name": "1 Gemini 3.1 Pro"},
    {"id": "gpt-4.1", "name": "0 GPT-4.1"},
    {"id": "gpt-4o", "name": "0 GPT-4o"},
    {"id": "gpt-5-mini", "name": "0 GPT-5 mini"},
    {"id": "gpt-5.1", "name": "1 GPT-5.1"},
    {"id": "gpt-5.1-codex", "name": "1 GPT-5.1-Codex"},
    {"id": "gpt-5.1-codex-mini", "name": "0.33 GPT-5.1-Codex-Mini"},
    {"id": "gpt-5.1-codex-max", "name": "1 GPT-5.1-Codex-Max"},
    {"id": "gpt-5.2", "name": "1 GPT-5.2"},
    {"id": "gpt-5.2-codex", "name": "1 GPT-5.2-Codex"},
    {"id": "gpt-5.3-codex", "name": "1 GPT-5.3-Codex"},
    {"id": "grok-code-fast-1", "name": "0.25 Grok Code Fast 1"},
    {"id": "raptor-mini", "name": "0 Raptor mini"}
]

data["models"]["providers"]["openai"]["models"] = openai_models
data["models"]["mode"] = "replace"

if "agents" in data and "defaults" in data["agents"]:
    for m in openai_models:
        alias_key = f"openai/{m['id']}"
        data["agents"]["defaults"]["models"][alias_key] = {"alias": m["name"]}
    data["agents"]["defaults"]["model"]["primary"] = "openai/gpt-4o"

if "list" in data["agents"] and len(data["agents"]["list"]) > 0:
    data["agents"]["list"][0]["model"] = "openai/gpt-4o"

with open(path, "w") as f:
    json.dump(data, f, indent=2)
