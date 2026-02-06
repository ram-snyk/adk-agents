# Manual Testing Guide - Google ADK Agent

This guide walks you through testing the ADK agent locally.

---

## Prerequisites

- Python 3.11 or higher
- Google API key (for Gemini API access)
- pip package manager

---

## Step 1: Set Up Python Environment

### Option A: Using Virtual Environment (Recommended)

```bash
# Navigate to project directory
cd /Users/ramdhakne/Documents/work/github/cursor-code/adk-agents

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows
```

### Option B: System Python

```bash
# Navigate to project directory
cd /Users/ramdhakne/Documents/work/github/cursor-code/adk-agents
```

---

## Step 2: Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt

# Verify installation
pip list | grep -E "google-genai|flask|requests"
```

**Expected Output:**
```
flask              3.0.0
google-genai       1.5.0
requests           2.32.4
```

---

## Step 3: Set Up Google API Key

### Get Your API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click "Create API Key"
3. Copy the generated key

### Configure Environment Variable

```bash
# Set API key for current session
export GOOGLE_API_KEY="your-actual-api-key-here"

# Verify it's set
echo $GOOGLE_API_KEY
```

**Alternative: Create .env file**

```bash
# Copy example file
cp .env.example .env

# Edit .env file
nano .env  # or use your preferred editor

# Add your key:
GOOGLE_API_KEY=your-actual-api-key-here
```

---

## Step 4: Run the Agent

```bash
# Start the agent
python agent.py
```

**Expected Output:**
```
🤖 Google ADK Customer Service Agent
==================================================
Type 'quit' to exit

You: 
```

---

## Step 5: Test the Agent

### Test Case 1: Knowledge Base Search

**Input:**
```
What's your shipping policy?
```

**Expected Response:**
```
🤖 Agent: Standard shipping takes 5-7 business days. Express shipping takes 2-3 business days.
```

---

### Test Case 2: Order Status Check (Existing Order)

**Input:**
```
Check order ORD-12345
```

**Expected Response:**
```
🤖 Agent: Your order has been shipped with tracking number 1Z999AA10123456784. 
Estimated delivery: 2026-02-05
```

---

### Test Case 3: Order Status Check (Processing Order)

**Input:**
```
What's the status of order ORD-67890?
```

**Expected Response:**
```
🤖 Agent: Your order is currently being processed. 
Estimated delivery: 2026-02-10
```

---

### Test Case 4: Order Status Check (Delivered Order)

**Input:**
```
Check order ORD-11111
```

**Expected Response:**
```
🤖 Agent: Your order has been delivered! 
Tracking number: 1Z999AA10123456785
Estimated delivery was: 2026-01-28
```

---

### Test Case 5: Order Status Check (Not Found)

**Input:**
```
Track order ORD-99999
```

**Expected Response:**
```
🤖 Agent: Order not found. Please verify the order ID and try again.
```

---

### Test Case 6: General Customer Service Question

**Input:**
```
What payment methods do you accept?
```

**Expected Response:**
```
🤖 Agent: We accept credit cards, PayPal, and Apple Pay.
```

---

### Test Case 7: Returns Policy

**Input:**
```
How do I return an item?
```

**Expected Response:**
```
🤖 Agent: You can return items within 30 days of purchase for a full refund.
```

---

### Test Case 8: Warranty Information

**Input:**
```
What warranty do your products have?
```

**Expected Response:**
```
🤖 Agent: All products come with a 1-year manufacturer warranty.
```

---

### Test Case 9: Combined Query

**Input:**
```
I need to check order ORD-12345 and also want to know about your return policy
```

**Expected Response:**
```
🤖 Agent: Let me help you with both questions.

Your order ORD-12345 has been shipped with tracking number 1Z999AA10123456784. 
Estimated delivery: 2026-02-05

Regarding our return policy: You can return items within 30 days of purchase for a full refund.
```

---

### Test Case 10: Exit the Agent

**Input:**
```
quit
```

**Expected Response:**
```
Goodbye!
```

---

## Troubleshooting

### Issue 1: Module Not Found Error

```
ModuleNotFoundError: No module named 'google.genai'
```

**Solution:**
```bash
# Ensure you're in the right directory
pwd
# Should show: /Users/ramdhakne/Documents/work/github/cursor-code/adk-agents

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

---

### Issue 2: API Key Error

```
Error: GOOGLE_API_KEY environment variable not set
```

**Solution:**
```bash
# Export API key
export GOOGLE_API_KEY="your-key-here"

# Verify
echo $GOOGLE_API_KEY

# Or use .env file
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print(os.getenv('GOOGLE_API_KEY'))"
```

---

### Issue 3: API Authentication Error

```
Error: google.api_core.exceptions.PermissionDenied: 403 API key not valid
```

**Solution:**
1. Verify your API key at [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Ensure the key has Gemini API access enabled
3. Check for any whitespace or quotes in the key
4. Generate a new key if needed

---

### Issue 4: Connection Error

```
Error: Failed to connect to api.google.com
```

**Solution:**
1. Check your internet connection
2. Verify firewall settings
3. Check if you need a proxy:
```bash
# If behind a proxy
export HTTP_PROXY="http://proxy.example.com:8080"
export HTTPS_PROXY="http://proxy.example.com:8080"
```

---

## Verification Checklist

- [ ] Virtual environment activated (optional but recommended)
- [ ] Dependencies installed successfully
- [ ] Google API key configured
- [ ] Agent starts without errors
- [ ] Agent responds to knowledge base queries
- [ ] Agent can check order status
- [ ] Agent handles multiple queries
- [ ] Agent handles unknown orders gracefully
- [ ] Can exit cleanly with 'quit'

---

## Testing Script (Automated)

Want to run all tests automatically? Create this test script:

```bash
# Create test_agent.sh
cat > test_agent.sh << 'EOF'
#!/bin/bash

echo "Testing Google ADK Agent"
echo "========================"

# Test commands
echo "What's your shipping policy?" | timeout 30 python agent.py
echo "Check order ORD-12345" | timeout 30 python agent.py
echo "quit" | timeout 30 python agent.py

echo "========================"
echo "Tests completed!"
EOF

# Make it executable
chmod +x test_agent.sh

# Run tests
./test_agent.sh
```

---

## Next Steps

After manual testing:
1. ✅ Test with different queries
2. ✅ Verify tool function calls are working
3. ✅ Check error handling
4. 🚀 Deploy to container (Docker)
5. 🚀 Deploy to Cloud Run
6. 📊 Set up monitoring and logging

---

## Advanced Testing

### Test with Python Script

Create `test_agent_automated.py`:

```python
from agent import run_agent

test_cases = [
    "What's your shipping policy?",
    "Check order ORD-12345",
    "What payment methods do you accept?",
    "Track order ORD-99999",
]

print("Running automated tests...\n")

for i, test in enumerate(test_cases, 1):
    print(f"Test {i}: {test}")
    try:
        response = run_agent(test)
        print(f"✅ Response: {response}\n")
    except Exception as e:
        print(f"❌ Error: {e}\n")
```

Run it:
```bash
python test_agent_automated.py
```

---

## Performance Testing

### Response Time Test

```bash
# Time a single query
time echo "What's your shipping policy?" | python agent.py
```

### Load Testing (Multiple Queries)

```bash
# Run 10 queries in parallel
for i in {1..10}; do
    echo "Query $i" &
    echo "Check order ORD-12345" | python agent.py &
done
wait
```

---

## Debugging Mode

### Enable Verbose Logging

Edit `agent.py` and add at the top:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

Run with debug output:
```bash
python agent.py
```

---

## Docker Testing (Optional)

```bash
# Build image
docker build -t adk-agent:latest .

# Run container (interactive mode disabled by default)
docker run -e GOOGLE_API_KEY="your-key" adk-agent:latest

# Or run with custom command
docker run -e GOOGLE_API_KEY="your-key" adk-agent:latest python -c "from agent import run_agent; print(run_agent('What is your shipping policy?'))"
```

---

**Ready to test!** Start with Step 1 and work through the test cases. 🚀
