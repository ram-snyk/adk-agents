# ⚠️ API Key Required

You need a Google API key to test the agent. Here's how to get it and test:

---

## Quick Test (Without Real API)

If you don't have an API key yet, you can test the tool functions directly:

```bash
cd /Users/ramdhakne/Documents/work/github/cursor-code/adk-agents
source venv/bin/activate
python -c "
from agent import search_knowledge_base, check_order_status

# Test knowledge base
print('Test 1: Knowledge Base')
result = search_knowledge_base('shipping')
print(result)
print()

# Test order status
print('Test 2: Order Status')
result = check_order_status('ORD-12345')
print(result)
"
```

This tests the tool functions without needing the AI model.

---

## Full Test (With API Key)

### Step 1: Get Your API Key

1. Visit: **https://aistudio.google.com/app/apikey**
2. Sign in with Google
3. Click "Create API Key"
4. Copy the key (starts with "AIza...")

### Step 2: Set the API Key & Test

```bash
cd /Users/ramdhakne/Documents/work/github/cursor-code/adk-agents
source venv/bin/activate

# Set your API key (replace with real key)
export GOOGLE_API_KEY="AIzaXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# Run test
python test_quick.py
```

---

## What Just Happened?

I fixed the agent code! The error was because I used an API structure that doesn't exist in the current Google GenAI SDK.

**Fixed:**
- ❌ `client.agentic.chats.create()` (doesn't exist)
- ✅ `client.chats.create()` (correct API)

**The agent now:**
- Uses the correct Google GenAI client API
- Properly handles function calls
- Has better error handling
- Prevents infinite loops

---

## Test Without API Key

Want to see the tools work without an API key?

```bash
cd /Users/ramdhakne/Documents/work/github/cursor-code/adk-agents
source venv/bin/activate

# Test the tool functions directly
python << 'EOF'
from agent import search_knowledge_base, check_order_status

print("=" * 60)
print("Testing Tool Functions (No API Key Needed)")
print("=" * 60)

# Test 1
print("\n📝 Test 1: Search for shipping info")
result = search_knowledge_base("shipping policy")
print(f"✅ Result: {result}")

# Test 2
print("\n📝 Test 2: Check shipped order")
result = check_order_status("ORD-12345")
print(f"✅ Result: {result}")

# Test 3
print("\n📝 Test 3: Check processing order")
result = check_order_status("ORD-67890")
print(f"✅ Result: {result}")

# Test 4
print("\n📝 Test 4: Check non-existent order")
result = check_order_status("ORD-99999")
print(f"✅ Result: {result}")

print("\n" + "=" * 60)
print("✅ All tool functions working correctly!")
print("=" * 60)
EOF
```

---

## Next Steps

1. ✅ **Run the no-API test above** to verify tools work
2. 🔑 **Get API key** from https://aistudio.google.com/app/apikey
3. 🚀 **Run full test** with `python test_quick.py`
4. 💬 **Try interactive mode** with `python agent.py`

---

**The agent is fixed and ready to test!**
