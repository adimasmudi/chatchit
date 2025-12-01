#!/usr/bin/env python3
"""
Simple test script to verify Ollama integration works
"""
import ollama

def test_ollama_connection():
    try:
        # Test basic connection
        response = ollama.chat(
            model='llama2',
            messages=[
                {
                    'role': 'user',
                    'content': 'Hello, can you respond with just "Hello back!" to confirm you\'re working?'
                }
            ]
        )
        print("Ollama connection successful!")
        print(f"Response: {response['message']['content']}")
        return True
    except Exception as e:
        print(f"❌ Ollama connection failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing Ollama with Llama2...")
    test_ollama_connection()