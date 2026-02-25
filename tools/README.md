# tools/

Utility scripts for Bobby setup.

## fix_bobby.py

Patches `openclaw.json` with the correct model list for the OpenAI provider.

**Usage:**
```bash
python3 tools/fix_bobby.py /path/to/openclaw.json
```

The script updates:
- `models.providers.openai.models` — replaces with current model list
- `models.mode` — sets to "replace"
- `agents.defaults.models` — updates model aliases
- `agents.defaults.model.primary` — sets to gpt-4o
- `agents.list[0].model` — sets to gpt-4o
