#!/bin/bash

# Google ADK Agent - Run Tests & Agent
# This script runs all tests and then starts the interactive agent

echo "🚀 Starting ADK Agent Test Suite & Interactive Mode"
echo "=================================================="
echo ""

# Activate virtual environment
source venv/bin/activate

# Test 1: Tool Functions (no API key needed)
echo "📝 Test 1: Tool Functions..."
python test_tools.py
TOOLS_EXIT=$?

if [ $TOOLS_EXIT -ne 0 ]; then
    echo "❌ Tool tests failed!"
    exit 1
fi

echo ""
echo "=================================================="
echo ""

# Test 2: Full Agent Test (requires API key)
echo "📝 Test 2: Full Agent with AI..."
python test_quick.py
AGENT_EXIT=$?

if [ $AGENT_EXIT -ne 0 ]; then
    echo "⚠️  Agent tests failed (check API key)"
    echo "Continuing to interactive mode..."
fi

echo ""
echo "=================================================="
echo ""

# Start interactive agent
echo "🤖 Starting Interactive Agent..."
echo ""
python agent.py
