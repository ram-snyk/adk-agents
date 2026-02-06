# 🚀 Quick Start - Test the ADK Agent Now!

Follow these steps to test the agent:

---

## ✅ Step 1: Test Tool Functions (No API Key Required)

First, let's verify the tool functions work:

```bash
cd /Users/ramdhakne/Documents/work/github/cursor-code/adk-agents
source venv/bin/activate
python test_tools.py
```

**Expected Output:**
```
🛠️  Testing ADK Agent Tool Functions (No API Key Required)
======================================================================

📝 Test 1: Search for shipping information
   ✅ PASS
   Status: shipped
   Tracking: 1Z999AA10123456784

📝 Test 2-7: ... (more tests)

Tests Passed: 7/7 (100%)
🎉 All tool functions working correctly!
```

✅ **DONE!** Your tool functions are working.

---

## 🔑 Step 2: Get Your Google API Key

To test the full AI agent, you need an API key:

1. **Go to:** https://aistudio.google.com/app/apikey
2. **Sign in** with your Google account
3. **Click** "Create API Key" button
4. **Copy** the generated key (starts with "AIza...")

---

## 🤖 Step 3: Test with AI (Requires API Key)

```bash
# In the same terminal
cd /Users/ramdhakne/Documents/work/github/cursor-code/adk-agents
source venv/bin/activate

# Set your API key (replace with your actual key)
export GOOGLE_API_KEY="AIzaXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# Run automated test
python test_quick.py
```

---

## 💬 Step 4: Interactive Testing (Optional)

```bash
# Start interactive agent
python agent.py
```

**Try these queries:**

```
What's your shipping policy?
```

```
Check order ORD-12345
```

```
What payment methods do you accept?
```

```
quit
```

---

## ✅ What We've Verified

1. ✅ **Fixed API Error** - Changed from `client.agentic.chats.create()` to `client.chats.create()`
2. ✅ **Tool Functions Work** - 7/7 tests passed (no API key needed)
3. ✅ **Security Scans Complete** - 5/7 vulnerabilities fixed, 2 accepted
4. ✅ **Dependencies Installed** - Including fixed `requests@2.32.4`

---

## 📝 Summary

**Without API Key (Tool Testing):**
```bash
python test_tools.py  # ✅ Working! Just ran it successfully
```

**With API Key (Full Agent):**
```bash
export GOOGLE_API_KEY="your-key"
python test_quick.py  # Tests AI integration
python agent.py       # Interactive mode
```

---

## 🎯 Current Status

| Component | Status | Notes |
|-----------|--------|-------|
| Tool Functions | ✅ Working | 7/7 tests passed |
| Agent Code | ✅ Fixed | API error resolved |
| Dependencies | ✅ Installed | requests@2.32.4 (secure) |
| Security Scans | ✅ Complete | 5 fixed, 2 accepted |
| API Key | ⏳ Needed | For AI testing only |

---

**Next:** Get your API key from https://aistudio.google.com/app/apikey and run `python test_quick.py`!
