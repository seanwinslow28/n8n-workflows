#!/usr/bin/env python3
"""
Test script for AI Chat Evaluation webhook
"""

import requests
import json

def test_webhook():
    """Test the AI Chat Evaluation webhook with sample data."""
    
    # Webhook URL for your workflow
    webhook_url = "http://localhost:5678/webhook/8f7c07c4-f36a-4d13-8f96-69ba52cb12a1"
    
    # Load sample data
    try:
        with open('test_sample_data.json', 'r') as f:
            sample_data = json.load(f)
    except FileNotFoundError:
        print("❌ test_sample_data.json not found!")
        return
    
    print("🚀 Testing AI Chat Evaluation Webhook")
    print("=" * 50)
    print(f"Webhook URL: {webhook_url}")
    print(f"Sample conversation has {len(sample_data['messages'])} messages")
    
    try:
        # Send POST request to webhook
        response = requests.post(
            webhook_url,
            json=sample_data,
            headers={'Content-Type': 'application/json'},
            timeout=30
        )
        
        print(f"\n📊 Response Status: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Webhook request successful!")
            print("🎉 Your AI evaluation workflow should now be processing...")
            print("\nYou can check:")
            print("1. n8n Executions tab for workflow progress")
            print("2. Your Notion database for results")
            
        elif response.status_code == 404:
            print("❌ Webhook not found (404)")
            print("💡 Make sure your workflow is ACTIVE:")
            print("   1. Open: http://localhost:5678/workflow/SCbZjNc21BRf0QTI")
            print("   2. Click the toggle switch in top-right")
            print("   3. Save the workflow")
            
        else:
            print(f"⚠️  Unexpected response: {response.status_code}")
            print(f"Response: {response.text}")
    
    except requests.exceptions.ConnectionError:
        print("❌ Connection failed!")
        print("   Make sure n8n is running on localhost:5678")
    
    except requests.exceptions.Timeout:
        print("⏰ Request timed out!")
        print("   The workflow might be taking longer to process")
    
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    test_webhook() 