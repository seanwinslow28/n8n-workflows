#!/usr/bin/env python3
"""
Database Enhancement with ChatGPT Suggested Views
Adds missing fields and creates the suggested views for better organization
"""

import os
import json
from notion_client import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def add_missing_fields_to_database():
    """Add the fields needed for ChatGPT's suggested views."""
    
    notion = Client(auth=os.getenv('NOTION_API_TOKEN'))
    database_id = os.getenv('NOTION_DATABASE_ID')
    
    if not database_id:
        print("❌ NOTION_DATABASE_ID not found in .env file")
        return False
    
    print("🔧 Adding missing fields for advanced views...")
    
    # New fields needed for the suggested views
    new_fields = {
        "Model": {
            "select": {
                "options": [
                    {"name": "GPT-4", "color": "blue"},
                    {"name": "GPT-3.5-turbo", "color": "green"},
                    {"name": "Claude-3", "color": "purple"},
                    {"name": "Claude-3.5-sonnet", "color": "pink"},
                    {"name": "Gemini-Pro", "color": "orange"},
                    {"name": "Other", "color": "gray"}
                ]
            }
        },
        "Use Case Type": {
            "select": {
                "options": [
                    {"name": "Technical Support", "color": "blue"},
                    {"name": "Creative Writing", "color": "green"},
                    {"name": "Code Review", "color": "purple"},
                    {"name": "General Q&A", "color": "yellow"},
                    {"name": "Educational", "color": "orange"},
                    {"name": "Problem Solving", "color": "red"},
                    {"name": "Other", "color": "gray"}
                ]
            }
        },
        "Evaluation Status": {
            "select": {
                "options": [
                    {"name": "Draft", "color": "yellow"},
                    {"name": "Complete", "color": "green"},
                    {"name": "Needs Review", "color": "orange"},
                    {"name": "Archived", "color": "gray"}
                ]
            }
        },
        "Tags": {
            "multi_select": {
                "options": [
                    {"name": "High Quality", "color": "green"},
                    {"name": "Needs Improvement", "color": "orange"},
                    {"name": "Edge Case", "color": "red"},
                    {"name": "Exemplary", "color": "blue"},
                    {"name": "Training Data", "color": "purple"},
                    {"name": "Production", "color": "pink"},
                    {"name": "Test", "color": "gray"}
                ]
            }
        }
    }
    
    try:
        # Get current database properties
        db_response = notion.databases.retrieve(database_id=database_id)
        current_properties = db_response.get("properties", {})
        
        # Add new fields to existing properties
        updated_properties = current_properties.copy()
        
        for field_name, field_config in new_fields.items():
            if field_name not in updated_properties:
                updated_properties[field_name] = field_config
                print(f"✅ Added field: {field_name}")
            else:
                print(f"⚠️  Field already exists: {field_name}")
        
        # Update the database with new properties
        notion.databases.update(
            database_id=database_id,
            properties=updated_properties
        )
        
        print(f"✅ Successfully updated database with {len(new_fields)} new fields")
        return True
        
    except Exception as e:
        print(f"❌ Error adding fields: {e}")
        return False

def create_sample_record_with_new_fields():
    """Create a sample record with the new fields populated."""
    
    notion = Client(auth=os.getenv('NOTION_API_TOKEN'))
    database_id = os.getenv('NOTION_DATABASE_ID')
    
    try:
        print("📝 Creating enhanced sample record...")
        
        sample_data = {
            "Session ID": {
                "title": [{"text": {"content": "enhanced_sample_002"}}]
            },
            "Helpfulness": {"number": 9.0},
            "Accuracy": {"number": 8.8},
            "Clarity": {"number": 9.2},
            "Relevance": {"number": 9.5},
            "Tone": {"number": 8.7},
            "Completeness": {"number": 8.9},
            "Overall Score": {"number": 9.0},
            "Key Insights": {
                "rich_text": [{"text": {"content": "Excellent technical explanation with practical examples and edge case handling."}}]
            },
            "Improvement Suggestions": {
                "rich_text": [{"text": {"content": "Could benefit from more visual aids or diagrams for complex concepts."}}]
            },
            "Conversation Summary": {
                "rich_text": [{"text": {"content": "User needed help with React hooks optimization. Assistant provided comprehensive solution with performance considerations."}}]
            },
            "User ID": {
                "rich_text": [{"text": {"content": "dev_user_456"}}]
            },
            "Message Count": {"number": 8},
            "Duration (minutes)": {"number": 5},
            "User Message Count": {"number": 4},
            "Assistant Message Count": {"number": 4},
            "Avg User Msg Length": {"number": 125},
            "Avg Assistant Msg Length": {"number": 380},
            
            # New fields
            "Model": {"select": {"name": "GPT-4"}},
            "Use Case Type": {"select": {"name": "Code Review"}},
            "Evaluation Status": {"select": {"name": "Complete"}},
            "Tags": {
                "multi_select": [
                    {"name": "High Quality"},
                    {"name": "Exemplary"},
                    {"name": "Production"}
                ]
            }
        }
        
        response = notion.pages.create(
            parent={"database_id": database_id},
            properties=sample_data
        )
        
        print(f"✅ Enhanced sample record created!")
        print(f"🔗 Record URL: {response.get('url')}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating sample record: {e}")
        return False

def print_view_creation_guide():
    """Print instructions for creating the suggested views."""
    
    print("\n🎯 Creating ChatGPT Suggested Views")
    print("=" * 50)
    print("Since Notion API doesn't support view creation, here's how to create them manually:")
    print()
    
    views = [
        {
            "name": "🧪 All Sessions",
            "type": "Table View",
            "setup": [
                "1. In your database, click '+ New view'",
                "2. Select 'Table' view type",
                "3. Name it '🧪 All Sessions'",
                "4. Add filters: None (show all)",
                "5. Sort by: Timestamp (newest first)",
                "6. Show all properties for full visibility"
            ]
        },
        {
            "name": "📊 Model Comparison Dashboard",
            "type": "Board View",
            "setup": [
                "1. Click '+ New view' → 'Board'",
                "2. Name it '📊 Model Comparison Dashboard'",
                "3. Group by: 'Model' property",
                "4. Show properties: Overall Score, Use Case Type, Tags",
                "5. This creates columns for each AI model"
            ]
        },
        {
            "name": "🧵 Evaluation Timeline",
            "type": "Calendar View",
            "setup": [
                "1. Click '+ New view' → 'Calendar'",
                "2. Name it '🧵 Evaluation Timeline'",
                "3. Date property: 'Timestamp'",
                "4. Show on calendar: Session ID, Overall Score, Model",
                "5. Color by: Model or Evaluation Status"
            ]
        },
        {
            "name": "📁 Use Case Filtered View",
            "type": "Table/Gallery View",
            "setup": [
                "1. Click '+ New view' → 'Gallery' (or Table)",
                "2. Name it '📁 Use Case Filtered View'",
                "3. Group by: 'Use Case Type'",
                "4. Show properties: Session ID, Overall Score, Tags",
                "5. Add filters as needed per use case"
            ]
        },
        {
            "name": "🔍 Needs Review",
            "type": "Board View",
            "setup": [
                "1. Click '+ New view' → 'Board'",
                "2. Name it '🔍 Needs Review'",
                "3. Group by: 'Evaluation Status'",
                "4. Add filter: Evaluation Status = 'Draft' OR 'Needs Review'",
                "5. Show properties: Session ID, Overall Score, Model"
            ]
        }
    ]
    
    for i, view in enumerate(views, 1):
        print(f"\n📋 View {i}: {view['name']} ({view['type']})")
        print("-" * 40)
        for step in view['setup']:
            print(f"   {step}")
    
    print("\n💡 Pro Tips:")
    print("• Use colors to make views more visually appealing")
    print("• Set up filters to focus on specific data sets")
    print("• Use sorting to prioritize important evaluations")
    print("• Share specific views with team members")

def create_view_templates():
    """Create template configurations for the views."""
    
    templates = {
        "all_sessions": {
            "name": "🧪 All Sessions",
            "type": "table",
            "properties": ["Session ID", "Model", "Overall Score", "Use Case Type", "Tags", "Timestamp"],
            "sorts": [{"property": "Timestamp", "direction": "descending"}],
            "filters": []
        },
        "model_comparison": {
            "name": "📊 Model Comparison Dashboard", 
            "type": "board",
            "group_by": "Model",
            "properties": ["Session ID", "Overall Score", "Use Case Type", "Tags"],
            "sorts": [{"property": "Overall Score", "direction": "descending"}]
        },
        "evaluation_timeline": {
            "name": "🧵 Evaluation Timeline",
            "type": "calendar",
            "date_property": "Timestamp",
            "properties": ["Session ID", "Overall Score", "Model"]
        },
        "use_case_filtered": {
            "name": "📁 Use Case Filtered View",
            "type": "gallery",
            "group_by": "Use Case Type",
            "properties": ["Session ID", "Overall Score", "Tags", "Model"]
        },
        "needs_review": {
            "name": "🔍 Needs Review",
            "type": "board",
            "group_by": "Evaluation Status",
            "filters": [
                {"property": "Evaluation Status", "select": {"equals": "Draft"}},
                {"property": "Evaluation Status", "select": {"equals": "Needs Review"}}
            ],
            "properties": ["Session ID", "Overall Score", "Model"]
        }
    }
    
    # Save templates to file
    with open("notion_view_templates.json", "w") as f:
        json.dump(templates, f, indent=2)
    
    print("✅ View templates saved to notion_view_templates.json")

def main():
    """Main function to enhance the database."""
    
    print("🚀 Database Enhancement with ChatGPT Views")
    print("=" * 50)
    
    # Check prerequisites
    if not os.getenv('NOTION_API_TOKEN'):
        print("❌ NOTION_API_TOKEN not found")
        return
    
    if not os.getenv('NOTION_DATABASE_ID'):
        print("❌ NOTION_DATABASE_ID not found")
        return
    
    # Add missing fields
    if add_missing_fields_to_database():
        print("✅ Database fields updated successfully")
        
        # Create enhanced sample record
        if create_sample_record_with_new_fields():
            print("✅ Enhanced sample record created")
        
        # Create view templates
        create_view_templates()
        
        # Print view creation guide
        print_view_creation_guide()
        
        print("\n🎉 Database Enhancement Complete!")
        print("=" * 50)
        print("✅ Added 4 new fields for advanced views")
        print("✅ Created enhanced sample record")
        print("✅ Generated view templates")
        print("✅ Ready for manual view creation in Notion")
        
        print(f"\n🔗 Go to your database to create the views:")
        print(f"   https://www.notion.so/{os.getenv('NOTION_DATABASE_ID', '').replace('-', '')}")
        
    else:
        print("❌ Failed to update database fields")

if __name__ == "__main__":
    main() 