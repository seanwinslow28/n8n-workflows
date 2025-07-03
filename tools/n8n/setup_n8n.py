#!/usr/bin/env python3
"""
N8N Setup Assistant
Guide users through connecting Cursor to their n8n Docker instance.
"""

import os
import json
import subprocess
from pathlib import Path
from n8n_client import N8nClient, N8nSync


def check_docker_n8n():
    """Check if n8n is running in Docker."""
    try:
        result = subprocess.run(
            ["docker", "ps", "--format", "table {{.Names}}\t{{.Status}}\t{{.Ports}}"],
            capture_output=True, text=True
        )
        
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')
            for line in lines:
                if 'n8n' in line.lower():
                    return line
        return None
    except Exception:
        return None


def prompt_for_api_key():
    """Guide user through API key creation."""
    print("🔑 N8N API Key Setup")
    print("=" * 40)
    print("To connect to your n8n instance, you need an API key.")
    print("")
    print("Steps to create an API key:")
    print("1. Open your n8n instance: http://localhost:5678")
    print("2. Click your profile icon → Settings")
    print("3. Click 'API' in the left sidebar")
    print("4. Click 'Create API Key'")
    print("5. Copy the generated API key")
    print("")
    
    api_key = input("Paste your API key here: ").strip()
    
    if not api_key:
        print("❌ No API key provided. Exiting.")
        return None
    
    return api_key


def save_api_key(api_key: str):
    """Save API key to environment file."""
    env_file = Path('.env')
    
    # Read existing content
    existing_content = ""
    if env_file.exists():
        with open(env_file, 'r') as f:
            existing_content = f.read()
    
    # Remove existing N8N_API_KEY line if present
    lines = existing_content.split('\n')
    filtered_lines = [line for line in lines if not line.startswith('N8N_API_KEY=')]
    
    # Add new API key
    filtered_lines.append(f'N8N_API_KEY={api_key}')
    
    # Write back to file
    with open(env_file, 'w') as f:
        f.write('\n'.join(filtered_lines))
    
    print(f"✅ API key saved to {env_file}")


def test_connection(api_key: str):
    """Test connection to n8n."""
    print("\n🔗 Testing Connection")
    print("=" * 40)
    
    try:
        # Set environment variable for this session
        os.environ['N8N_API_KEY'] = api_key
        
        client = N8nClient()
        result = client.test_connection()
        
        if result['status'] == 'success':
            print("✅ Connection successful!")
            print(f"📊 Found {result['workflow_count']} workflows in your n8n instance")
            return True
        else:
            print(f"❌ Connection failed: {result['message']}")
            if 'details' in result:
                print(f"Details: {result['details']}")
            return False
    
    except Exception as e:
        print(f"❌ Connection error: {e}")
        return False


def show_workflow_info(api_key: str):
    """Show some workflow information."""
    try:
        os.environ['N8N_API_KEY'] = api_key
        client = N8nClient()
        
        workflows = client.get_workflows()
        active_workflows = [w for w in workflows if w.get('active')]
        
        print(f"\n📋 Workflow Summary")
        print("=" * 40)
        print(f"Total workflows: {len(workflows)}")
        print(f"Active workflows: {len(active_workflows)}")
        
        if workflows:
            print("\nRecent workflows:")
            for i, wf in enumerate(workflows[:5], 1):
                status = "🟢" if wf.get('active') else "🔴"
                print(f"  {i}. {status} {wf.get('name', 'Unnamed')} [{wf.get('id')}]")
        
        return True
    
    except Exception as e:
        print(f"❌ Error fetching workflow info: {e}")
        return False


def setup_workflow_sync(api_key: str):
    """Set up workflow synchronization."""
    print(f"\n🔄 Workflow Synchronization Setup")
    print("=" * 40)
    
    try:
        os.environ['N8N_API_KEY'] = api_key
        client = N8nClient()
        sync = N8nSync(client)
        
        choice = input("Do you want to sync workflows from n8n to local files? (y/n): ").strip().lower()
        
        if choice == 'y':
            print("Syncing workflows from n8n...")
            result = sync.sync_all_from_n8n()
            print(f"✅ Sync complete: {result['exported']} exported, {result['failed']} failed")
        
        return True
    
    except Exception as e:
        print(f"❌ Error setting up sync: {e}")
        return False


def create_test_script():
    """Create a test script for quick workflow testing."""
    test_script = """#!/usr/bin/env python3
'''
Quick N8N Workflow Tester
Run this script to test your n8n workflows quickly.
'''

import os
from n8n_client import N8nClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    try:
        client = N8nClient()
        
        # Test connection
        print("Testing n8n connection...")
        result = client.test_connection()
        
        if result['status'] == 'success':
            print(f"✅ Connected! Found {result['workflow_count']} workflows")
            
            # List workflows
            workflows = client.get_workflows()
            print("\\nAvailable workflows:")
            for i, wf in enumerate(workflows, 1):
                status = "🟢" if wf.get('active') else "🔴"
                print(f"  {i}. {status} {wf.get('name', 'Unnamed')} [{wf.get('id')}]")
        
        else:
            print(f"❌ Connection failed: {result['message']}")
    
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
"""
    
    with open("test_n8n.py", "w") as f:
        f.write(test_script)
    
    print("✅ Created test_n8n.py script")


def main():
    """Main setup process."""
    print("🚀 N8N + Cursor Integration Setup")
    print("=" * 50)
    
    # Check Docker
    docker_info = check_docker_n8n()
    if docker_info:
        print(f"✅ Found n8n Docker container: {docker_info}")
    else:
        print("⚠️  Could not find n8n Docker container")
        print("   Make sure n8n is running: docker run -it --rm --name n8n -p 5678:5678 n8nio/n8n")
        choice = input("Continue anyway? (y/n): ").strip().lower()
        if choice != 'y':
            return
    
    # Get API key
    api_key = prompt_for_api_key()
    if not api_key:
        return
    
    # Test connection
    if not test_connection(api_key):
        print("❌ Setup failed. Please check your API key and n8n instance.")
        return
    
    # Save API key
    save_api_key(api_key)
    
    # Show workflow info
    show_workflow_info(api_key)
    
    # Setup sync
    setup_workflow_sync(api_key)
    
    # Create test script
    create_test_script()
    
    print("\n🎉 Setup Complete!")
    print("=" * 50)
    print("Your n8n instance is now connected to Cursor!")
    print("")
    print("Next steps:")
    print("1. Run: python test_n8n.py - to test your connection")
    print("2. Use: python n8n_client.py list - to list all workflows")
    print("3. Use: python n8n_client.py export <workflow_id> - to export workflows")
    print("4. Check your specific workflow: http://localhost:5678/workflow/SCbZjNc21BRf0QTI")
    print("")
    print("Happy workflow automation! 🎯")


if __name__ == "__main__":
    main() 