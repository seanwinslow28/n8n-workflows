#!/usr/bin/env python3
"""
Test Notion database connection and verify database structure
"""

import requests
import json
import os

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

NOTION_API_TOKEN = os.getenv('NOTION_API_TOKEN')

def test_notion_connection():
    """Test connection to both Notion databases"""
    print("🔍 Testing Notion Database Connection...")
    print("=" * 50)
    
    if not NOTION_API_TOKEN:
        print("❌ NOTION_API_TOKEN not found in environment variables")
        return False
    
    headers = {
        'Authorization': f'Bearer {NOTION_API_TOKEN}',
        'Content-Type': 'application/json',
        'Notion-Version': '2022-06-28'
    }
    
    # Database IDs from the workflow
    databases = {
        'GPT Database': '2260a4634b4e81618e72dd644e0a718f',
        'Claude Database': '2260a4634b4e8154b338d3643dc353b9'
    }
    
    all_working = True
    
    for db_name, db_id in databases.items():
        print(f"\n📊 Testing {db_name}...")
        print(f"Database ID: {db_id}")
        
        try:
            # Test database access
            response = requests.get(
                f'https://api.notion.com/v1/databases/{db_id}',
                headers=headers
            )
            
            if response.status_code == 200:
                db_data = response.json()
                print(f"✅ {db_name} - Connection successful!")
                
                # Check properties
                properties = db_data.get('properties', {})
                print(f"   Properties found: {len(properties)}")
                
                expected_props = [
                    'Session ID', 'Model', 'Overall Score', 'Performance Winner',
                    'Agreement Rate', 'Avg Score Difference', 'Helpfulness',
                    'Accuracy', 'Clarity', 'Relevance', 'Tone', 'Completeness',
                    'Key Insights', 'Timestamp'
                ]
                
                missing_props = []
                for prop in expected_props:
                    if prop not in properties:
                        missing_props.append(prop)
                
                if missing_props:
                    print(f"⚠️  Missing properties: {missing_props}")
                    all_working = False
                else:
                    print(f"✅ All required properties present!")
                    
            elif response.status_code == 404:
                print(f"❌ {db_name} - Database not found (404)")
                print(f"   Database ID might be incorrect: {db_id}")
                all_working = False
                
            elif response.status_code == 401:
                print(f"❌ {db_name} - Authorization failed (401)")
                print(f"   Check your NOTION_API_TOKEN")
                all_working = False
                
            else:
                print(f"❌ {db_name} - Error {response.status_code}")
                print(f"   Response: {response.text}")
                all_working = False
                
        except Exception as e:
            print(f"❌ {db_name} - Connection error: {e}")
            all_working = False
    
    print("\n" + "=" * 50)
    if all_working:
        print("🎉 ALL DATABASES WORKING! The issue might be in n8n configuration.")
        print("\n🔧 Next steps:")
        print("1. Check Notion credentials in n8n nodes")
        print("2. Verify database URLs in Notion nodes")
        print("3. Check if Notion integration has write permissions")
    else:
        print("❌ Database connection issues found. Fix these first.")
        
    return all_working

def test_simple_write():
    """Test writing a simple record to verify permissions"""
    print("\n🧪 Testing Write Permissions...")
    print("=" * 30)
    
    if not NOTION_API_TOKEN:
        print("❌ NOTION_API_TOKEN not found")
        return
    
    headers = {
        'Authorization': f'Bearer {NOTION_API_TOKEN}',
        'Content-Type': 'application/json',
        'Notion-Version': '2022-06-28'
    }
    
    # Test write to GPT database
    db_id = '2260a4634b4e81618e72dd644e0a718f'
    
    test_data = {
        "parent": {"database_id": db_id},
        "properties": {
            "Session ID": {
                "title": [{"text": {"content": "connection_test"}}]
            },
            "Model": {
                "select": {"name": "GPT-3.5-turbo"}
            },
            "Overall Score": {
                "number": 8.5
            },
            "Performance Winner": {
                "select": {"name": "This Model"}
            },
            "Agreement Rate": {
                "rich_text": [{"text": {"content": "85%"}}]
            },
            "Avg Score Difference": {
                "number": 1.2
            },
            "Helpfulness": {"number": 8},
            "Accuracy": {"number": 9},
            "Clarity": {"number": 8},
            "Relevance": {"number": 9},
            "Tone": {"number": 8},
            "Completeness": {"number": 7},
            "Key Insights": {
                "rich_text": [{"text": {"content": "Test connection successful"}}]
            },
            "Timestamp": {
                "date": {"start": "2025-01-03T10:00:00.000Z"}
            }
        }
    }
    
    try:
        response = requests.post(
            'https://api.notion.com/v1/pages',
            headers=headers,
            json=test_data
        )
        
        if response.status_code == 200:
            print("✅ Write test successful! Database has proper permissions.")
            page_data = response.json()
            print(f"   Created page ID: {page_data.get('id')}")
        else:
            print(f"❌ Write test failed: {response.status_code}")
            print(f"   Response: {response.text}")
            
    except Exception as e:
        print(f"❌ Write test error: {e}")

if __name__ == "__main__":
    connection_ok = test_notion_connection()
    if connection_ok:
        test_simple_write() 