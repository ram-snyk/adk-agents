# Model Troubleshooting

## ✅ Working Model: gemini-2.5-flash-lite

The agent is currently configured to use `gemini-2.5-flash-lite` which has been verified to work.

---

## If you need to change models:

In `agent.py`, line ~14, change `MODEL_ID` to one of these:

### Option 1: gemini-2.5-flash-lite (✅ Verified Working)
```python
MODEL_ID = "gemini-2.5-flash-lite"
```

### Option 2: gemini-pro (common fallback)
```python
MODEL_ID = "gemini-pro"
```

### Option 3: gemini-1.5-pro
```python
MODEL_ID = "gemini-1.5-pro"
```

### Option 4: gemini-1.5-flash-latest
```python
MODEL_ID = "gemini-1.5-flash-latest"
```

---

## To find all available models for your API key:

```bash
# Set your API key first
export GOOGLE_API_KEY="your-key"

# List all models
curl "https://generativelanguage.googleapis.com/v1beta/models?key=$GOOGLE_API_KEY" | python -m json.tool | grep '"name"'
```

---

## Model Characteristics

**gemini-2.5-flash-lite:**
- ✅ Fast response times
- ✅ Supports function calling (tools)
- ✅ Lightweight and efficient
- ✅ Good for customer service use cases

**Note:** Different API keys may have access to different models depending on your Google AI Studio account settings and region.
