#!/usr/bin/env python3
"""
List available models for your API key
"""
import os
from google import genai

api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    print("⚠️  GOOGLE_API_KEY not set!")
    exit(1)

print("🔍 Checking available models...\n")

try:
    client = genai.Client(api_key=api_key)
    
    # List available models
    models = client.models.list()
    
    print("✅ Available models that support generateContent:\n")
    
    for model in models:
        # Check if model supports generateContent
        if hasattr(model, 'supported_generation_methods'):
            if 'generateContent' in model.supported_generation_methods:
                print(f"  • {model.name}")
                if hasattr(model, 'display_name'):
                    print(f"    Display Name: {model.display_name}")
        elif hasattr(model, 'name'):
            print(f"  • {model.name}")
    
    print("\n💡 Use one of these model names in agent.py")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nTrying alternative approach...")
    
    # Try just gemini-pro which is usually available
    print("\n📝 Recommended model names to try:")
    print("  • gemini-pro")
    print("  • gemini-1.5-pro")
    print("  • models/gemini-pro")
    print("  • models/gemini-1.5-pro")
