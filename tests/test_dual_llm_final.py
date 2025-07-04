#!/usr/bin/env python3
"""
COMPREHENSIVE Dual LLM Workflow Test
Tests all properties and data types for proper Notion integration
"""

import requests
import json
import time
from datetime import datetime
import sys
import os

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_dual_llm_workflow():
    """
    Test the complete dual LLM workflow with comprehensive data
    """
    
    # n8n workflow webhook URL
    webhook_url = "http://localhost:5678/webhook/dual-llm-comparison"
    
    # Generate test session ID
    session_id = f"comprehensive_test_{int(time.time())}"
    
    # Comprehensive test conversation
    test_conversation = {
        "sessionId": session_id,
        "timestamp": datetime.now().isoformat(),
        "userId": "test_user_comprehensive",
        "duration": 180000,  # 3 minutes in milliseconds
        "messages": [
            {
                "role": "user",
                "content": "I need help debugging a Python function that's supposed to calculate the factorial of a number, but it's not working correctly. Here's my code:\n\n```python\ndef factorial(n):\n    if n = 0:\n        return 1\n    else:\n        return n * factorial(n-1)\n```\n\nCan you help me fix this?"
            },
            {
                "role": "assistant", 
                "content": "I can see the issue in your factorial function! There's a syntax error in your if condition. You're using a single equals sign `=` which is assignment, but you need double equals `==` for comparison.\n\nHere's the corrected code:\n\n```python\ndef factorial(n):\n    if n == 0:  # Changed = to ==\n        return 1\n    else:\n        return n * factorial(n-1)\n```\n\nAdditionally, I'd recommend adding some error handling for edge cases:\n\n```python\ndef factorial(n):\n    # Handle negative numbers\n    if n < 0:\n        raise ValueError(\"Factorial is not defined for negative numbers\")\n    \n    # Base cases\n    if n == 0 or n == 1:\n        return 1\n    \n    # Recursive case\n    return n * factorial(n-1)\n```\n\nYou can test it with:\n```python\nprint(factorial(5))  # Should output 120\nprint(factorial(0))  # Should output 1\n```"
            },
            {
                "role": "user",
                "content": "Thanks! That fixed the syntax error. But I'm still getting a RecursionError when I try factorial(1000). How can I optimize this?"
            },
            {
                "role": "assistant",
                "content": "Great question! The RecursionError occurs because Python has a default recursion limit (usually around 1000). For large numbers, an iterative approach is much more efficient:\n\n```python\ndef factorial_iterative(n):\n    if n < 0:\n        raise ValueError(\"Factorial is not defined for negative numbers\")\n    \n    result = 1\n    for i in range(1, n + 1):\n        result *= i\n    return result\n```\n\nThis iterative version:\n- Avoids recursion depth issues\n- Is more memory efficient\n- Handles large numbers better\n\nFor even better performance with very large numbers, you could also use Python's built-in `math.factorial()` function:\n\n```python\nimport math\nprint(math.factorial(1000))  # Works perfectly!\n```\n\nThe iterative approach will handle factorial(1000) without any issues. Would you like me to show you how to compare the performance of these different approaches?"
            },
            {
                "role": "user", 
                "content": "Perfect! Yes, I'd love to see a performance comparison. This has been really helpful."
            },
            {
                "role": "assistant",
                "content": "I'm glad this was helpful! Here's a performance comparison script:\n\n```python\nimport time\nimport math\n\ndef factorial_recursive(n):\n    if n < 0:\n        raise ValueError(\"Factorial is not defined for negative numbers\")\n    if n == 0 or n == 1:\n        return 1\n    return n * factorial_recursive(n-1)\n\ndef factorial_iterative(n):\n    if n < 0:\n        raise ValueError(\"Factorial is not defined for negative numbers\")\n    result = 1\n    for i in range(1, n + 1):\n        result *= i\n    return result\n\ndef benchmark_factorial(n):\n    # Test iterative approach\n    start = time.time()\n    result_iterative = factorial_iterative(n)\n    time_iterative = time.time() - start\n    \n    # Test built-in math.factorial\n    start = time.time()\n    result_builtin = math.factorial(n)\n    time_builtin = time.time() - start\n    \n    print(f\"n = {n}\")\n    print(f\"Iterative: {time_iterative:.6f} seconds\")\n    print(f\"Built-in:  {time_builtin:.6f} seconds\")\n    print(f\"Results match: {result_iterative == result_builtin}\")\n    print(\"---\")\n\n# Run benchmarks\nfor n in [100, 500, 1000, 2000]:\n    benchmark_factorial(n)\n```\n\nThis will show you that the built-in `math.factorial()` is typically the fastest, followed by the iterative approach. The recursive version would cause a stack overflow for these large numbers.\n\nKey takeaways:\n1. Always use iterative or built-in solutions for large factorials\n2. Python's `math.factorial()` is optimized and should be your first choice\n3. Understanding both approaches helps you write better recursive algorithms in general"
            }
        ]
    }
    
    print("🧪 COMPREHENSIVE DUAL LLM WORKFLOW TEST")
    print("=" * 50)
    print(f"Session ID: {session_id}")
    print(f"Webhook URL: {webhook_url}")
    print(f"Test Messages: {len(test_conversation['messages'])}")
    print(f"Duration: {test_conversation['duration']}ms")
    print()
    
    # Send test request
    try:
        print("📤 Sending test request...")
        response = requests.post(
            webhook_url,
            json=test_conversation,
            headers={'Content-Type': 'application/json'},
            timeout=120  # 2 minutes timeout
        )
        
        print(f"✅ HTTP Status: {response.status_code}")
        print(f"📋 Response: {response.text}")
        
        if response.status_code == 200:
            print("\n🎉 TEST SUCCESSFUL!")
            print("=" * 30)
            print("✅ Webhook received data")
            print("✅ Workflow should be processing")
            print("✅ Check your n8n workflow execution")
            print("✅ Verify data appears in both Notion databases")
            print()
            print("📊 Expected Results:")
            print("- GPT Database: https://www.notion.so/2260a4634b4e81618e72dd644e0a718f")
            print("- Claude Database: https://www.notion.so/2260a4634b4e8154b338d3643dc353b9")
            print()
            print("🔍 Key Properties to Verify:")
            print("- Session ID: Should be title field")
            print("- Model: Should be select field (GPT-3.5-turbo / Claude-3.5-Sonnet)")
            print("- Overall Score: Should be number field")
            print("- Performance Winner: Should be select field")
            print("- Agreement Rate: Should be rich_text field")
            print("- Avg Score Difference: Should be NUMBER field (not string)")
            print("- Helpfulness/Accuracy/Clarity/Relevance/Tone/Completeness: Should be numbers")
            print("- Key Insights: Should be rich_text field")
            print("- Timestamp: Should be date field")
            
        else:
            print(f"\n❌ TEST FAILED!")
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.text}")
            
    except requests.exceptions.RequestException as e:
        print(f"\n❌ REQUEST ERROR: {e}")
        print("Make sure n8n is running on localhost:5678")
    
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {e}")

def print_data_types():
    """Print expected data types for debugging"""
    print("\n📋 EXPECTED DATA TYPES:")
    print("=" * 30)
    print("sessionId: string")
    print("model: string")
    print("overall_score: number")
    print("higher_scoring: string")
    print("overall_agreement: string (with %)")
    print("avg_score_difference: NUMBER (not string!)")
    print("helpfulness: number")
    print("accuracy: number")
    print("clarity: number")
    print("relevance: number")
    print("tone: number")
    print("completeness: number")
    print("key_insights: string")
    print("timestamp: ISO string")

if __name__ == "__main__":
    test_dual_llm_workflow()
    print_data_types() 