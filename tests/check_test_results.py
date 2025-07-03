#!/usr/bin/env python3
"""
Quick validation script to check if the test was successful
"""

import webbrowser
import time

def check_test_results():
    """Help user validate the test results step by step."""
    
    print("🔍 AI CHAT EVALUATION - RESULTS VALIDATION")
    print("=" * 50)
    
    # Step 1: Check n8n executions
    print("\n1️⃣ STEP 1: Check n8n Execution Status")
    print("   Opening n8n executions page...")
    
    try:
        webbrowser.open("http://localhost:5678/executions")
        time.sleep(2)
    except:
        print("   ❌ Could not open browser automatically")
        print("   🔗 Go to: http://localhost:5678/executions")
    
    print("\n   ✅ Look for recent execution of 'AI Chat Evaluation'")
    print("   ✅ All nodes should be green (successful)")
    print("   ❌ If any node is red, click it to see error details")
    
    input("\n   Press Enter when you've checked the execution status...")
    
    # Step 2: Check Notion database
    print("\n2️⃣ STEP 2: Check Notion Database")
    print("   Opening Notion database...")
    
    try:
        webbrowser.open("https://www.notion.so/2250a4634b4e81d5bce7ea9d29bd2089")
        time.sleep(2)
    except:
        print("   ❌ Could not open browser automatically")
        print("   🔗 Go to: https://www.notion.so/2250a4634b4e81d5bce7ea9d29bd2089")
    
    print("\n   ✅ Look for new entry with Session ID: test_session_001")
    print("   ✅ Verify all 23 properties are filled:")
    print("      • Numbers (1-10): Helpfulness, Accuracy, Clarity, etc.")
    print("      • Text fields: Key Insights, Improvement Suggestions")
    print("      • Metadata: Message Count (6), Duration (2 min)")
    print("      • Classifications: Model (GPT-4), Use Case (Code Review)")
    
    input("\n   Press Enter when you've checked the Notion database...")
    
    # Step 3: Validate results
    print("\n3️⃣ STEP 3: Results Validation")
    print("   Expected AI evaluation scores (1-10 scale):")
    print("   • Helpfulness: 8-10 (excellent debugging help)")
    print("   • Accuracy: 9-10 (correct Python syntax fixes)")
    print("   • Clarity: 8-10 (clear code explanations)")
    print("   • Relevance: 9-10 (directly answered questions)")
    print("   • Tone: 8-10 (professional and helpful)")
    print("   • Completeness: 8-10 (thorough responses)")
    print("   • Overall Score: 8+ average")
    
    # Get user feedback
    print("\n4️⃣ STEP 4: Test Status")
    
    execution_ok = input("   ✅ Was the n8n execution successful? (y/n): ").lower().strip()
    notion_ok = input("   ✅ Were all 23 properties created in Notion? (y/n): ").lower().strip()
    scores_ok = input("   ✅ Do the AI evaluation scores look reasonable? (y/n): ").lower().strip()
    
    print("\n" + "="*50)
    
    if execution_ok == 'y' and notion_ok == 'y' and scores_ok == 'y':
        print("🎉 SUCCESS! All 23 properties are working correctly!")
        print("✅ Your AI Chat Evaluation workflow is fully operational")
        print("\n🚀 READY FOR PRODUCTION:")
        print("   • All scoring metrics working")
        print("   • All metadata captured")
        print("   • All classifications populated")
        print("   • Notion integration complete")
        
    else:
        print("⚠️  ISSUES DETECTED - Let's troubleshoot:")
        
        if execution_ok != 'y':
            print("   🔧 n8n execution failed:")
            print("      • Check credentials (OpenAI API, Notion API)")
            print("      • Verify workflow is active")
            print("      • Check node configurations")
        
        if notion_ok != 'y':
            print("   🔧 Notion properties missing:")
            print("      • Verify database URL is correct")
            print("      • Check Notion API permissions")
            print("      • Validate property names match database")
        
        if scores_ok != 'y':
            print("   🔧 AI evaluation scores issue:")
            print("      • Check OpenAI API key")
            print("      • Verify prompt is working")
            print("      • Review structured output parser")
    
    print("\n📋 NEXT STEPS:")
    print("   • Test with your own conversation data")
    print("   • Adjust scoring criteria if needed")
    print("   • Set up production webhook endpoint")
    print("   • Monitor evaluation quality over time")


if __name__ == "__main__":
    check_test_results() 