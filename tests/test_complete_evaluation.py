#!/usr/bin/env python3
"""
Complete test script for AI Chat Evaluation workflow
Tests all 23 Notion properties
"""

import requests
import json
import time
from datetime import datetime

def test_complete_evaluation():
    """Test the complete AI Chat Evaluation workflow with all 23 properties."""
    
    # Your workflow webhook URL
    webhook_url = "http://localhost:5678/webhook/8f7c07c4-f36a-4d13-8f96-69ba52cb12a1"
    
    # Load sample data
    try:
        with open('test_sample_data.json', 'r') as f:
            sample_data = json.load(f)
    except FileNotFoundError:
        print("❌ test_sample_data.json not found!")
        return
    
    print("🚀 COMPLETE AI CHAT EVALUATION TEST")
    print("=" * 60)
    print(f"🔗 Webhook URL: {webhook_url}")
    print(f"📊 Sample Data Overview:")
    print(f"   • Session ID: {sample_data.get('sessionId', 'N/A')}")
    print(f"   • Messages: {len(sample_data.get('messages', []))}")
    print(f"   • Duration: {sample_data.get('duration', 0)/1000:.1f}s")
    print(f"   • Model: {sample_data.get('model', 'N/A')}")
    print(f"   • Use Case: {sample_data.get('useCase', 'N/A')}")
    print(f"   • Tags: {sample_data.get('tags', [])}")
    print()
    
    # Properties we expect to be created in Notion
    expected_properties = [
        "Session ID (title)",
        "Helpfulness (number)",
        "Accuracy (number)", 
        "Clarity (number)",
        "Relevance (number)",
        "Tone (number)",
        "Completeness (number)",
        "Overall Score (number)",
        "Key Insights (rich_text)",
        "Improvement Suggestions (rich_text)",
        "Conversation Summary (rich_text)",
        "Timestamp (date)",
        "User ID (rich_text)",
        "Message Count (number)",
        "Duration (minutes) (number)",
        "User Message Count (number)",
        "Assistant Message Count (number)",
        "Avg User Msg Length (number)",
        "Avg Assistant Msg Length (number)",
        "Model (select)",
        "Use Case Type (select)",
        "Evaluation Status (select)",
        "Tags (multi_select)"
    ]
    
    print("📋 EXPECTED PROPERTIES TO BE CREATED:")
    for i, prop in enumerate(expected_properties, 1):
        print(f"   {i:2d}. {prop}")
    print()
    
    try:
        print("🔄 Sending test request...")
        start_time = time.time()
        
        # Send POST request to webhook
        response = requests.post(
            webhook_url,
            json=sample_data,
            headers={'Content-Type': 'application/json'},
            timeout=60  # Increased timeout for AI processing
        )
        
        end_time = time.time()
        duration = end_time - start_time
        
        print(f"⏱️  Request completed in {duration:.2f} seconds")
        print(f"📡 Response Status: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ WEBHOOK TEST SUCCESSFUL!")
            print()
            print("🎯 WHAT TO CHECK NOW:")
            print("1. 🔍 n8n Executions:")
            print("   • Go to: http://localhost:5678/executions")
            print("   • Look for recent execution of 'AI Chat Evaluation'")
            print("   • Verify all nodes executed successfully")
            print()
            print("2. 📊 Notion Database:")
            print("   • Check: https://www.notion.so/2250a4634b4e81d5bce7ea9d29bd2089")
            print("   • Look for new entry with Session ID: test_session_001")
            print("   • Verify all 23 properties are populated")
            print()
            print("3. 🔬 Property Validation:")
            print("   Expected values:")
            print(f"   • Session ID: {sample_data['sessionId']}")
            print(f"   • Message Count: {len(sample_data['messages'])}")
            print(f"   • Duration: {round(sample_data['duration']/60000)} minutes")
            print(f"   • Model: {sample_data['model']}")
            print(f"   • Use Case: {sample_data['useCase']}")
            print(f"   • Tags: {sample_data['tags']}")
            print()
            
            # Display scoring expectations
            print("4. 📈 AI Evaluation Scores (1-10 scale):")
            print("   • Helpfulness: Should be 8-10 (excellent debugging help)")
            print("   • Accuracy: Should be 9-10 (correct Python syntax)")
            print("   • Clarity: Should be 8-10 (clear explanations)")
            print("   • Relevance: Should be 9-10 (directly answered questions)")
            print("   • Tone: Should be 8-10 (professional and helpful)")
            print("   • Completeness: Should be 8-10 (thorough responses)")
            print("   • Overall Score: Should be 8+ average")
            print()
            
        elif response.status_code == 404:
            print("❌ WEBHOOK NOT FOUND (404)")
            print("💡 SOLUTION:")
            print("   1. Make sure workflow is ACTIVE:")
            print("      • Go to: http://localhost:5678/workflow/SCbZjNc21BRf0QTI")
            print("      • Click toggle switch in top-right")
            print("      • Save the workflow")
            print("   2. Check webhook URL matches the one in your workflow")
            
        else:
            print(f"⚠️  UNEXPECTED RESPONSE: {response.status_code}")
            print(f"Response: {response.text}")
    
    except requests.exceptions.ConnectionError:
        print("❌ CONNECTION FAILED!")
        print("💡 SOLUTION:")
        print("   • Make sure n8n is running on localhost:5678")
        print("   • Start n8n with: npx n8n start")
    
    except requests.exceptions.Timeout:
        print("⏰ REQUEST TIMED OUT!")
        print("💡 This might be normal - AI evaluation takes time")
        print("   • Check n8n executions for progress")
        print("   • The workflow might still be processing")
    
    except Exception as e:
        print(f"❌ ERROR: {e}")
    
    print()
    print("🔗 USEFUL LINKS:")
    print("   • Workflow Editor: http://localhost:5678/workflow/SCbZjNc21BRf0QTI")
    print("   • Executions: http://localhost:5678/executions")
    print("   • Notion Database: https://www.notion.so/2250a4634b4e81d5bce7ea9d29bd2089")


if __name__ == "__main__":
    test_complete_evaluation() 