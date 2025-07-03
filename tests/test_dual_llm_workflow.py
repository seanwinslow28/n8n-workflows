#!/usr/bin/env python3
"""
Dual LLM Comparison Workflow Test Script
Tests the GPT vs Claude side-by-side evaluation workflow
"""

import json
import requests
import time
from datetime import datetime
from typing import Dict, Any, List

# Configuration
WEBHOOK_URL = "http://localhost:5678/webhook/dual-llm-comparison"
TEST_DATA_FILE = "test_sample_data.json"

class DualLLMWorkflowTester:
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url
        self.session_id = f"dual_test_{int(time.time())}"
        
    def create_test_conversation(self, scenario: str) -> Dict[str, Any]:
        """Create test conversation data for different scenarios"""
        
        scenarios = {
            "coding_help": {
                "messages": [
                    {"role": "user", "content": "I need help with a Python function that calculates the factorial of a number. Can you help me write one?"},
                    {"role": "assistant", "content": "I'd be happy to help you write a factorial function in Python! Here are a few different approaches:\\n\\n```python\\n# Recursive approach\\ndef factorial_recursive(n):\\n    if n == 0 or n == 1:\\n        return 1\\n    return n * factorial_recursive(n - 1)\\n\\n# Iterative approach\\ndef factorial_iterative(n):\\n    result = 1\\n    for i in range(1, n + 1):\\n        result *= i\\n    return result\\n```\\n\\nThe recursive approach is elegant but can hit recursion limits for large numbers. The iterative approach is more efficient for larger values.\\n\\nWould you like me to explain any of these approaches in more detail?"},
                    {"role": "user", "content": "That's great! Can you also add error handling for negative numbers?"},
                    {"role": "assistant", "content": "Absolutely! Here's the improved version with proper error handling:\\n\\n```python\\ndef factorial_safe(n):\\n    '''Calculate factorial with error handling'''\\n    \\n    # Type checking\\n    if not isinstance(n, int):\\n        raise TypeError('Input must be an integer')\\n    \\n    # Handle negative numbers\\n    if n < 0:\\n        raise ValueError('Factorial is not defined for negative numbers')\\n    \\n    # Handle base cases\\n    if n == 0 or n == 1:\\n        return 1\\n    \\n    # Calculate factorial iteratively\\n    result = 1\\n    for i in range(2, n + 1):\\n        result *= i\\n    \\n    return result\\n```\\n\\nThis version:\\n- Checks if the input is an integer\\n- Raises a clear error for negative numbers\\n- Handles the base cases (0! = 1, 1! = 1)\\n- Uses an efficient iterative approach\\n\\nThis makes the function much more robust and user-friendly!"}
                ],
                "sessionId": self.session_id + "_coding",
                "userId": "test_user_coding",
                "timestamp": datetime.now().isoformat(),
                "duration": 45000
            },
            
            "simple_question": {
                "messages": [
                    {"role": "user", "content": "What's the capital of France?"},
                    {"role": "assistant", "content": "The capital of France is Paris."}
                ],
                "sessionId": self.session_id + "_simple",
                "userId": "test_user_simple",
                "timestamp": datetime.now().isoformat(),
                "duration": 2000
            }
        }
        
        return scenarios.get(scenario, scenarios["simple_question"])
    
    def send_test_request(self, test_data: Dict[str, Any]) -> Dict[str, Any]:
        """Send test request to the webhook"""
        try:
            print(f"🚀 Sending test request to: {self.webhook_url}")
            print(f"📊 Test scenario: {test_data['sessionId']}")
            print(f"💬 Messages: {len(test_data['messages'])}")
            
            response = requests.post(
                self.webhook_url,
                json=test_data,
                timeout=120,  # 2 minutes timeout for dual LLM processing
                headers={'Content-Type': 'application/json'}
            )
            
            print(f"📨 Response status: {response.status_code}")
            
            if response.status_code == 200:
                return {
                    "success": True,
                    "status_code": response.status_code,
                    "response_time": response.elapsed.total_seconds(),
                    "data": response.json() if response.text else None
                }
            else:
                print(f"❌ Error response: {response.text}")
                return {
                    "success": False,
                    "status_code": response.status_code,
                    "error": response.text,
                    "response_time": response.elapsed.total_seconds()
                }
                
        except requests.exceptions.Timeout:
            print("⏰ Request timed out - this is expected for dual LLM processing")
            return {
                "success": False,
                "error": "Request timeout (expected for dual LLM processing)",
                "response_time": 120
            }
        except requests.exceptions.RequestException as e:
            print(f"❌ Request failed: {e}")
            return {
                "success": False,
                "error": str(e),
                "response_time": 0
            }
    
    def run_comprehensive_test(self):
        """Run comprehensive test suite"""
        print("🎯 DUAL LLM WORKFLOW COMPREHENSIVE TEST")
        print("=" * 50)
        
        test_scenarios = [
            ("simple_question", "Simple Q&A"),
            ("coding_help", "Coding Assistance")
        ]
        
        results = []
        
        for scenario_key, scenario_name in test_scenarios:
            print(f"\\n🧪 Testing: {scenario_name}")
            print("-" * 30)
            
            test_data = self.create_test_conversation(scenario_key)
            result = self.send_test_request(test_data)
            
            result['scenario'] = scenario_name
            result['scenario_key'] = scenario_key
            result['test_data'] = test_data
            
            results.append(result)
            
            # Wait between tests to avoid rate limiting
            time.sleep(5)
        
        return results

def main():
    """Main test execution"""
    print("🚀 DUAL LLM COMPARISON WORKFLOW TESTER")
    print("=" * 50)
    
    # Initialize tester
    tester = DualLLMWorkflowTester(WEBHOOK_URL)
    
    # Run comprehensive test
    results = tester.run_comprehensive_test()
    
    print("\\n🎉 Testing complete! Check your Notion databases for the results.")

if __name__ == "__main__":
    main()
