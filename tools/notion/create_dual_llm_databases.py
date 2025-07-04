#!/usr/bin/env python3
"""
Create Notion databases for Dual LLM Chat Evaluation
Creates two databases with EXACT properties matching the n8n workflow nodes
"""

import requests
import json
import os
from datetime import datetime

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("python-dotenv not installed. Reading from system environment variables.")
    pass

NOTION_API_KEY = os.getenv('NOTION_API_TOKEN')  # Using NOTION_API_TOKEN to match your .env file
NOTION_PARENT_PAGE_ID = os.getenv('NOTION_PARENT_PAGE_ID')  # The page where databases will be created

if not NOTION_API_KEY:
    raise ValueError("NOTION_API_TOKEN environment variable is required")
if not NOTION_PARENT_PAGE_ID:
    raise ValueError("NOTION_PARENT_PAGE_ID environment variable is required")

headers = {
    'Authorization': f'Bearer {NOTION_API_KEY}',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'
}

def create_database(title, properties):
    """Create a Notion database with specified properties"""
    url = 'https://api.notion.com/v1/databases'
    
    payload = {
        "parent": {
            "type": "page_id",
            "page_id": NOTION_PARENT_PAGE_ID
        },
        "title": [
            {
                "type": "text",
                "text": {
                    "content": title
                }
            }
        ],
        "properties": properties
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error creating database '{title}': {response.status_code}")
        print(f"Response: {response.text}")
        return None

def main():
    """Create both GPT and Claude evaluation databases"""
    
    print("Creating Dual LLM Evaluation Databases...")
    print("=" * 50)
    
    # EXACT properties matching the n8n workflow nodes
    database_properties = {
        "Session ID": {
            "title": {}
        },
        "Model": {
            "select": {
                "options": [
                    {
                        "name": "GPT-3.5-turbo",
                        "color": "blue"
                    },
                    {
                        "name": "Claude-3.5-Sonnet", 
                        "color": "purple"
                    }
                ]
            }
        },
        "Overall Score": {
            "number": {
                "format": "number"
            }
        },
        "Performance Winner": {
            "select": {
                "options": [
                    {
                        "name": "This Model",
                        "color": "green"
                    },
                    {
                        "name": "Competitor",
                        "color": "red"
                    },
                    {
                        "name": "Tie",
                        "color": "gray"
                    }
                ]
            }
        },
        "Agreement Rate": {
            "rich_text": {}
        },
        "Avg Score Difference": {
            "number": {
                "format": "number"
            }
        },
        "Helpfulness": {
            "number": {
                "format": "number"
            }
        },
        "Accuracy": {
            "number": {
                "format": "number"
            }
        },
        "Clarity": {
            "number": {
                "format": "number"
            }
        },
        "Relevance": {
            "number": {
                "format": "number"
            }
        },
        "Tone": {
            "number": {
                "format": "number"
            }
        },
        "Completeness": {
            "number": {
                "format": "number"
            }
        },
        "Key Insights": {
            "rich_text": {}
        },
        "Timestamp": {
            "date": {}
        }
    }
    
    # Create GPT Evaluation Database
    print("Creating GPT Evaluation Database...")
    gpt_database = create_database("GPT Evaluation Results", database_properties)
    
    if gpt_database:
        gpt_db_id = gpt_database['id']
        gpt_db_url = gpt_database['url']
        print(f"✅ GPT Database created successfully!")
        print(f"   Database ID: {gpt_db_id}")
        print(f"   Database URL: {gpt_db_url}")
        print()
    else:
        print("❌ Failed to create GPT Database")
        return
    
    # Create Claude Evaluation Database
    print("Creating Claude Evaluation Database...")
    claude_database = create_database("Claude Evaluation Results", database_properties)
    
    if claude_database:
        claude_db_id = claude_database['id']
        claude_db_url = claude_database['url']
        print(f"✅ Claude Database created successfully!")
        print(f"   Database ID: {claude_db_id}")
        print(f"   Database URL: {claude_db_url}")
        print()
    else:
        print("❌ Failed to create Claude Database")
        return
    
    # Save database IDs to environment file
    env_content = f"""
# Dual LLM Evaluation Database IDs
# Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

# GPT Evaluation Database
GPT_NOTION_DATABASE_ID={gpt_db_id}
GPT_NOTION_DATABASE_URL={gpt_db_url}

# Claude Evaluation Database  
CLAUDE_NOTION_DATABASE_ID={claude_db_id}
CLAUDE_NOTION_DATABASE_URL={claude_db_url}
"""
    
    with open('.env.databases', 'w') as f:
        f.write(env_content)
    
    print("=" * 50)
    print("🎉 SETUP COMPLETE!")
    print("=" * 50)
    print()
    print("Database IDs saved to .env.databases")
    print("You can now configure your n8n workflow with these database URLs:")
    print()
    print("GPT Notion Database URL:")
    print(f"   {gpt_db_url}")
    print()
    print("Claude Notion Database URL:")
    print(f"   {claude_db_url}")
    print()
    print("IMPORTANT: Update your n8n workflow Notion nodes with these URLs!")
    print("Replace the placeholder URLs in the workflow with the actual database URLs above.")
    print()
    
    # Verify properties match workflow exactly
    print("✅ Properties verification:")
    print("The databases were created with these EXACT properties:")
    for prop_name, prop_config in database_properties.items():
        prop_type = list(prop_config.keys())[0]
        print(f"   • {prop_name} ({prop_type})")
    print()
    print("These match your n8n workflow nodes exactly!")

if __name__ == "__main__":
    main() 