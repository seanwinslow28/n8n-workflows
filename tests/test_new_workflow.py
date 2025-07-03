#!/usr/bin/env python3
"""
Test script for the NEW AI Chat Evaluation workflow
Workflow ID: cHpmNleWCIiAoqFo
"""

import requests
import json
import time
from datetime import datetime

def get_webhook_url():
    """Get the webhook URL from the user."""
    print("🔗 WEBHOOK URL NEEDED")
    print("=" * 50)
    print("Please get the webhook URL from your new workflow:")
    print("1. In the workflow editor (http://localhost:5678/workflow/cHpmNleWCIiAoqFo)")
    print("2. Click on the 'Webhook' node (first node)")
    print("3. Copy the 'Webhook URL' field")
    print("4. It should look like: http://localhost:5678/webhook/[some-uuid]")
    print()
    
    webhook_url = input("📋 Paste the webhook URL here: ").strip()
    
    if not webhook_url:
        print("❌ No webhook URL provided!")
        return None
    
    if not webhook_url.startswith("http://localhost:5678/webhook/"):
        print("⚠️  Warning: URL format doesn't match expected pattern")
        print("   Expected: http://localhost:5678/webhook/[uuid]")
        print("   Got: " + webhook_url)
        
        continue_anyway = input("   Continue anyway? (y/n): ").lower().strip()
        if continue_anyway != 'y':
            return None
    
    return webhook_url

def test_new_workflow():
    """Test the new AI Chat Evaluation workflow."""
    
    print("🚀 NEW WORKFLOW TEST - AI Chat Evaluation")
    print("=" * 60)
    print(f"🆔 Workflow ID: cHpmNleWCIiAoqFo")
    print(f"🔗 Workflow URL: http://localhost:5678/workflow/cHpmNleWCIiAoqFo")
    print()
    
    # Get webhook URL
    webhook_url = get_webhook_url()
    if not webhook_url:
        print("❌ Cannot proceed without webhook URL")
        return
    
    # Load sample data
    try:
        with open('test_sample_data.json', 'r') as f:
            sample_data = json.load(f)
    except FileNotFoundError:
        print("❌ test_sample_data.json not found!")
        return
    
    # Use a new session ID for this test
    sample_data['sessionId'] = f"new_workflow_test_{int(time.time())}"
    
    print(f"📊 Test Data:")
    print(f"   • Session ID: {sample_data['sessionId']}")
    print(f"   • Messages: {len(sample_data.get('messages', []))}")
    print(f"   • Duration: {sample_data.get('duration', 0)/1000:.1f}s")
    print(f"   • Model: {sample_data.get('model', 'N/A')}")
    print(f"   • Use Case: {sample_data.get('useCase', 'N/A')}")
    print()
    
    # Expected properties (all 23)
    expected_properties = [
        "Session ID (title)", "Helpfulness (number)", "Accuracy (number)", 
        "Clarity (number)", "Relevance (number)", "Tone (number)",
        "Completeness (number)", "Overall Score (number)", "Key Insights (rich_text)",
        "Improvement Suggestions (rich_text)", "Conversation Summary (rich_text)",
        "Timestamp (date)", "User ID (rich_text)", "Message Count (number)",
        "Duration (minutes) (number)", "User Message Count (number)",
        "Assistant Message Count (number)", "Avg User Msg Length (number)",
        "Avg Assistant Msg Length (number)", "Model (select)",
        "Use Case Type (select)", "Evaluation Status (select)", "Tags (multi_select)"
    ]
    
    print("📋 Testing All 23 Properties:")
    for i, prop in enumerate(expected_properties, 1):
        print(f"   {i:2d}. {prop}")
    print()
    
    # Run the test
    try:
        print("🔄 Sending test request...")
        start_time = time.time()
        
        response = requests.post(
            webhook_url,
            json=sample_data,
            headers={'Content-Type': 'application/json'},
            timeout=60
        )
        
        end_time = time.time()
        duration = end_time - start_time
        
        print(f"⏱️  Request completed in {duration:.2f} seconds")
        print(f"📡 Response Status: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ WEBHOOK TEST SUCCESSFUL!")
            print()
            print("🎯 VALIDATION STEPS:")
            print("1. 🔍 Check n8n Executions:")
            print(f"   • Go to: http://localhost:5678/executions")
            print(f"   • Look for execution with Session ID: {sample_data['sessionId']}")
            print("   • All nodes should be green ✅")
            print()
            print("2. 📊 Check Notion Database:")
            print("   • Go to: https://www.notion.so/2250a4634b4e81d5bce7ea9d29bd2089")
            print(f"   • Look for new entry with Session ID: {sample_data['sessionId']}")
            print("   • Verify all 23 properties are populated")
            print()
            print("3. 🚀 If successful, your workflow is ready!")
            
        elif response.status_code == 404:
            print("❌ WEBHOOK NOT FOUND (404)")
            print("💡 POSSIBLE ISSUES:")
            print("   • Workflow is not active (check the toggle switch)")
            print("   • Wrong webhook URL")
            print("   • Webhook node not configured properly")
            
        else:
            print(f"⚠️  UNEXPECTED RESPONSE: {response.status_code}")
            print(f"Response: {response.text}")
    
    except requests.exceptions.ConnectionError:
        print("❌ CONNECTION FAILED!")
        print("💡 Make sure n8n is running on localhost:5678")
    
    except requests.exceptions.Timeout:
        print("⏰ REQUEST TIMED OUT!")
        print("💡 This might be normal - AI evaluation takes time")
        print("   Check n8n executions for progress")
    
    except Exception as e:
        print(f"❌ ERROR: {e}")
    
    print()
    print("🔗 USEFUL LINKS:")
    print(f"   • Workflow Editor: http://localhost:5678/workflow/cHpmNleWCIiAoqFo")
    print("   • Executions: http://localhost:5678/executions")
    print("   • Notion Database: https://www.notion.so/2250a4634b4e81d5bce7ea9d29bd2089")


if __name__ == "__main__":
    test_new_workflow() 