#!/usr/bin/env python3
"""
Direct Database Creator for AI Chat Evaluations
Creates the database directly in your Notion workspace
"""

import os
import json
from notion_client import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_ai_chat_database():
    """Create the AI Chat Evaluation database directly."""
    
    # Your teamspace page ID from the URL
    parent_page_id = "2210a4634b4e8083a67ed4fc3bf00100"
    
    # Initialize Notion client
    notion = Client(auth=os.getenv('NOTION_API_TOKEN'))
    
    print("🏗️  Creating AI Chat Evaluation Database...")
    print(f"📍 Parent page: {parent_page_id}")
    
    # Database schema with all 19 fields
    properties = {
        # Title field (required)
        "Session ID": {
            "title": {}
        },
        
        # AI Evaluation Scores (1-10 scale)
        "Helpfulness": {
            "number": {"format": "number"}
        },
        "Accuracy": {
            "number": {"format": "number"}
        },
        "Clarity": {
            "number": {"format": "number"}
        },
        "Relevance": {
            "number": {"format": "number"}
        },
        "Tone": {
            "number": {"format": "number"}
        },
        "Completeness": {
            "number": {"format": "number"}
        },
        "Overall Score": {
            "number": {"format": "number"}
        },
        
        # AI-generated insights
        "Key Insights": {
            "rich_text": {}
        },
        "Improvement Suggestions": {
            "rich_text": {}
        },
        "Conversation Summary": {
            "rich_text": {}
        },
        
        # Metadata fields
        "Timestamp": {
            "date": {}
        },
        "User ID": {
            "rich_text": {}
        },
        
        # Conversation analytics
        "Message Count": {
            "number": {"format": "number"}
        },
        "Duration (minutes)": {
            "number": {"format": "number"}
        },
        "User Message Count": {
            "number": {"format": "number"}
        },
        "Assistant Message Count": {
            "number": {"format": "number"}
        },
        "Avg User Msg Length": {
            "number": {"format": "number"}
        },
        "Avg Assistant Msg Length": {
            "number": {"format": "number"}
        }
    }
    
    try:
        # Create the database
        response = notion.databases.create(
            parent={
                "type": "page_id",
                "page_id": parent_page_id
            },
            title=[
                {
                    "type": "text",
                    "text": {
                        "content": "AI Chat Evaluations"
                    }
                }
            ],
            properties=properties
        )
        
        database_id = response.get("id")
        database_url = response.get("url")
        
        print(f"✅ Database created successfully!")
        print(f"📊 Database ID: {database_id}")
        print(f"🔗 Database URL: {database_url}")
        print(f"📋 Created {len(properties)} fields")
        
        # Update .env file with database ID
        update_env_file(database_id)
        
        # Create sample record
        create_sample_record(notion, database_id)
        
        # Show n8n URL format
        n8n_url = f"https://www.notion.so/{database_id.replace('-', '')}"
        print(f"\n🔗 URL for n8n workflow:")
        print(f"   {n8n_url}")
        
        return database_id
        
    except Exception as e:
        print(f"❌ Error creating database: {e}")
        return None

def create_sample_record(notion, database_id):
    """Create a sample evaluation record."""
    
    try:
        print("📝 Adding sample evaluation record...")
        
        sample_data = {
            "Session ID": {
                "title": [{"text": {"content": "sample_session_001"}}]
            },
            "Helpfulness": {"number": 8.5},
            "Accuracy": {"number": 9.0},
            "Clarity": {"number": 8.0},
            "Relevance": {"number": 9.5},
            "Tone": {"number": 8.5},
            "Completeness": {"number": 7.5},
            "Overall Score": {"number": 8.5},
            "Key Insights": {
                "rich_text": [{"text": {"content": "The assistant provided comprehensive and accurate technical guidance with clear examples."}}]
            },
            "Improvement Suggestions": {
                "rich_text": [{"text": {"content": "Could include more error handling examples and edge cases."}}]
            },
            "Conversation Summary": {
                "rich_text": [{"text": {"content": "User asked for help with Python factorial function debugging. Assistant identified syntax and logic errors, provided corrections, and explained error handling."}}]
            },
            "User ID": {
                "rich_text": [{"text": {"content": "test_user_123"}}]
            },
            "Message Count": {"number": 6},
            "Duration (minutes)": {"number": 2},
            "User Message Count": {"number": 3},
            "Assistant Message Count": {"number": 3},
            "Avg User Msg Length": {"number": 85},
            "Avg Assistant Msg Length": {"number": 245}
        }
        
        response = notion.pages.create(
            parent={"database_id": database_id},
            properties=sample_data
        )
        
        print(f"✅ Sample record created!")
        print(f"🔗 Record URL: {response.get('url')}")
        
    except Exception as e:
        print(f"⚠️  Could not create sample record: {e}")

def update_env_file(database_id):
    """Update .env file with database ID."""
    
    try:
        # Read current .env content
        with open(".env", "r") as f:
            lines = f.readlines()
        
        # Remove existing NOTION_DATABASE_ID if present
        lines = [line for line in lines if not line.startswith('NOTION_DATABASE_ID=')]
        
        # Add new database ID
        lines.append(f'NOTION_DATABASE_ID={database_id}\n')
        
        # Write back to file
        with open(".env", "w") as f:
            f.writelines(lines)
        
        print(f"✅ Updated .env file with database ID")
        
    except Exception as e:
        print(f"⚠️  Could not update .env file: {e}")

def main():
    """Main function."""
    
    print("🎯 AI Chat Evaluation Database Creator")
    print("=" * 50)
    
    # Check if token exists
    if not os.getenv('NOTION_API_TOKEN'):
        print("❌ NOTION_API_TOKEN not found in .env file")
        return
    
    # Create the database
    database_id = create_ai_chat_database()
    
    if database_id:
        print("\n🎉 Database Setup Complete!")
        print("=" * 50)
        print("✅ Database created with 19 fields")
        print("✅ Sample record added")
        print("✅ Database ID saved to .env file")
        print("✅ Ready for n8n workflow integration")
        
        print("\n📋 Next Steps:")
        print("1. Copy the database URL above")
        print("2. Update your n8n workflow Notion node")
        print("3. Test with: python3 test_webhook.py")
        
    else:
        print("❌ Database creation failed")

if __name__ == "__main__":
    main() 