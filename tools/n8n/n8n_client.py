#!/usr/bin/env python3
"""
N8N API Client for Direct Integration
Connect Cursor to your n8n Docker instance for workflow management.
"""

import requests
import json
import os
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path
import urllib.parse
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class N8nClient:
    """Direct API client for n8n instance integration."""
    
    def __init__(self, base_url: str = "http://localhost:5678", api_key: str = None):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key or os.getenv('N8N_API_KEY')
        self.session = requests.Session()
        
        if not self.api_key:
            raise ValueError("N8N API key required. Set N8N_API_KEY environment variable or pass api_key parameter.")
        
        self.session.headers.update({
            'X-N8N-API-KEY': self.api_key,
            'Content-Type': 'application/json'
        })
    
    def test_connection(self) -> Dict[str, Any]:
        """Test connection to n8n API."""
        try:
            response = self.session.get(f"{self.base_url}/api/v1/workflows")
            if response.status_code == 200:
                data = response.json()
                return {
                    "status": "success",
                    "message": "Connected to n8n API",
                    "workflow_count": len(data.get('data', [])),
                    "api_version": "v1"
                }
            else:
                return {
                    "status": "error",
                    "message": f"API returned status {response.status_code}",
                    "details": response.text
                }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Connection failed: {str(e)}"
            }
    
    def get_workflows(self, active_only: bool = False) -> List[Dict[str, Any]]:
        """Get all workflows from n8n."""
        try:
            url = f"{self.base_url}/api/v1/workflows"
            if active_only:
                url += "?active=true"
            
            response = self.session.get(url)
            response.raise_for_status()
            
            data = response.json()
            return data.get('data', [])
        except Exception as e:
            print(f"Error fetching workflows: {e}")
            return []
    
    def get_workflow_by_id(self, workflow_id: str) -> Optional[Dict[str, Any]]:
        """Get a specific workflow by ID."""
        try:
            response = self.session.get(f"{self.base_url}/api/v1/workflows/{workflow_id}")
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching workflow {workflow_id}: {e}")
            return None
    
    def create_workflow(self, workflow_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Create a new workflow in n8n."""
        try:
            response = self.session.post(
                f"{self.base_url}/api/v1/workflows",
                json=workflow_data
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error creating workflow: {e}")
            return None
    
    def update_workflow(self, workflow_id: str, workflow_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Update an existing workflow."""
        try:
            response = self.session.put(
                f"{self.base_url}/api/v1/workflows/{workflow_id}",
                json=workflow_data
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error updating workflow {workflow_id}: {e}")
            return None
    
    def delete_workflow(self, workflow_id: str) -> bool:
        """Delete a workflow."""
        try:
            response = self.session.delete(f"{self.base_url}/api/v1/workflows/{workflow_id}")
            response.raise_for_status()
            return True
        except Exception as e:
            print(f"Error deleting workflow {workflow_id}: {e}")
            return False
    
    def activate_workflow(self, workflow_id: str) -> bool:
        """Activate a workflow."""
        try:
            response = self.session.patch(
                f"{self.base_url}/api/v1/workflows/{workflow_id}/activate"
            )
            response.raise_for_status()
            return True
        except Exception as e:
            print(f"Error activating workflow {workflow_id}: {e}")
            return False
    
    def deactivate_workflow(self, workflow_id: str) -> bool:
        """Deactivate a workflow."""
        try:
            response = self.session.patch(
                f"{self.base_url}/api/v1/workflows/{workflow_id}/deactivate"
            )
            response.raise_for_status()
            return True
        except Exception as e:
            print(f"Error deactivating workflow {workflow_id}: {e}")
            return False
    
    def execute_workflow(self, workflow_id: str, input_data: Dict[str, Any] = None) -> Optional[Dict[str, Any]]:
        """Execute a workflow manually."""
        try:
            payload = {"triggerData": input_data or {}}
            response = self.session.post(
                f"{self.base_url}/api/v1/workflows/{workflow_id}/execute",
                json=payload
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error executing workflow {workflow_id}: {e}")
            return None
    
    def get_executions(self, workflow_id: str = None, limit: int = 20) -> List[Dict[str, Any]]:
        """Get workflow executions."""
        try:
            url = f"{self.base_url}/api/v1/executions"
            params = {"limit": limit}
            if workflow_id:
                params["workflowId"] = workflow_id
            
            response = self.session.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()
            return data.get('data', [])
        except Exception as e:
            print(f"Error fetching executions: {e}")
            return []
    
    def get_execution_by_id(self, execution_id: str) -> Optional[Dict[str, Any]]:
        """Get execution details by ID."""
        try:
            response = self.session.get(f"{self.base_url}/api/v1/executions/{execution_id}")
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching execution {execution_id}: {e}")
            return None
    
    def get_workflow_credentials(self) -> List[Dict[str, Any]]:
        """Get available credentials."""
        try:
            response = self.session.get(f"{self.base_url}/api/v1/credentials")
            response.raise_for_status()
            
            data = response.json()
            return data.get('data', [])
        except Exception as e:
            print(f"Error fetching credentials: {e}")
            return []
    
    def test_webhook(self, webhook_url: str, method: str = "GET", data: Dict[str, Any] = None) -> Dict[str, Any]:
        """Test a webhook endpoint."""
        try:
            if method.upper() == "GET":
                response = requests.get(webhook_url, params=data)
            elif method.upper() == "POST":
                response = requests.post(webhook_url, json=data)
            elif method.upper() == "PUT":
                response = requests.put(webhook_url, json=data)
            elif method.upper() == "DELETE":
                response = requests.delete(webhook_url)
            else:
                return {"status": "error", "message": f"Unsupported method: {method}"}
            
            return {
                "status": "success",
                "status_code": response.status_code,
                "response": response.text,
                "headers": dict(response.headers)
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Webhook test failed: {str(e)}"
            }


class N8nSync:
    """Synchronization between local files and n8n instance."""
    
    def __init__(self, client: N8nClient, workflows_dir: str = "workflows"):
        self.client = client
        self.workflows_dir = Path(workflows_dir)
        self.workflows_dir.mkdir(exist_ok=True)
    
    def export_workflow_from_n8n(self, workflow_id: str, filename: str = None) -> bool:
        """Export a workflow from n8n to local file."""
        try:
            workflow = self.client.get_workflow_by_id(workflow_id)
            if not workflow:
                return False
            
            if not filename:
                # Generate filename from workflow name
                name = workflow.get('name', f'workflow_{workflow_id}')
                safe_name = "".join(c for c in name if c.isalnum() or c in (' ', '-', '_')).rstrip()
                filename = f"{safe_name.replace(' ', '_')}.json"
            
            # Ensure .json extension
            if not filename.endswith('.json'):
                filename += '.json'
            
            file_path = self.workflows_dir / filename
            
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(workflow, f, indent=2, ensure_ascii=False)
            
            print(f"✅ Exported workflow to {file_path}")
            return True
        except Exception as e:
            print(f"❌ Error exporting workflow: {e}")
            return False
    
    def import_workflow_to_n8n(self, filename: str) -> Optional[str]:
        """Import a local workflow file to n8n."""
        try:
            file_path = self.workflows_dir / filename
            
            with open(file_path, 'r', encoding='utf-8') as f:
                workflow_data = json.load(f)
            
            # Check if workflow already exists
            workflow_id = workflow_data.get('id')
            if workflow_id:
                existing = self.client.get_workflow_by_id(workflow_id)
                if existing:
                    # Update existing workflow
                    result = self.client.update_workflow(workflow_id, workflow_data)
                    if result:
                        print(f"✅ Updated existing workflow {workflow_id}")
                        return workflow_id
                    else:
                        return None
            
            # Create new workflow
            result = self.client.create_workflow(workflow_data)
            if result:
                new_id = result.get('id')
                print(f"✅ Created new workflow {new_id}")
                return new_id
            else:
                return None
                
        except Exception as e:
            print(f"❌ Error importing workflow: {e}")
            return None
    
    def sync_all_from_n8n(self) -> Dict[str, int]:
        """Export all workflows from n8n to local files."""
        workflows = self.client.get_workflows()
        exported = 0
        failed = 0
        
        for workflow in workflows:
            workflow_id = workflow.get('id')
            if workflow_id:
                if self.export_workflow_from_n8n(workflow_id):
                    exported += 1
                else:
                    failed += 1
        
        return {"exported": exported, "failed": failed, "total": len(workflows)}
    
    def sync_all_to_n8n(self) -> Dict[str, int]:
        """Import all local workflow files to n8n."""
        json_files = list(self.workflows_dir.glob("*.json"))
        imported = 0
        failed = 0
        
        for file_path in json_files:
            if self.import_workflow_to_n8n(file_path.name):
                imported += 1
            else:
                failed += 1
        
        return {"imported": imported, "failed": failed, "total": len(json_files)}


def main():
    """CLI interface for n8n client."""
    import argparse
    
    parser = argparse.ArgumentParser(description="N8N API Client")
    parser.add_argument("--api-key", help="N8N API key")
    parser.add_argument("--base-url", default="http://localhost:5678", help="N8N base URL")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Test connection
    subparsers.add_parser("test", help="Test connection to n8n")
    
    # List workflows
    list_parser = subparsers.add_parser("list", help="List workflows")
    list_parser.add_argument("--active", action="store_true", help="Show only active workflows")
    
    # Export workflow
    export_parser = subparsers.add_parser("export", help="Export workflow from n8n")
    export_parser.add_argument("workflow_id", help="Workflow ID to export")
    export_parser.add_argument("--filename", help="Output filename")
    
    # Import workflow
    import_parser = subparsers.add_parser("import", help="Import workflow to n8n")
    import_parser.add_argument("filename", help="Workflow file to import")
    
    # Sync commands
    subparsers.add_parser("sync-from-n8n", help="Export all workflows from n8n")
    subparsers.add_parser("sync-to-n8n", help="Import all workflows to n8n")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    try:
        client = N8nClient(args.base_url, args.api_key)
        sync = N8nSync(client)
        
        if args.command == "test":
            result = client.test_connection()
            print(json.dumps(result, indent=2))
        
        elif args.command == "list":
            workflows = client.get_workflows(args.active)
            print(f"Found {len(workflows)} workflows:")
            for wf in workflows:
                status = "🟢 Active" if wf.get('active') else "🔴 Inactive"
                print(f"  {status} [{wf.get('id')}] {wf.get('name', 'Unnamed')}")
        
        elif args.command == "export":
            success = sync.export_workflow_from_n8n(args.workflow_id, args.filename)
            if not success:
                exit(1)
        
        elif args.command == "import":
            result = sync.import_workflow_to_n8n(args.filename)
            if not result:
                exit(1)
        
        elif args.command == "sync-from-n8n":
            result = sync.sync_all_from_n8n()
            print(f"Sync complete: {result['exported']} exported, {result['failed']} failed")
        
        elif args.command == "sync-to-n8n":
            result = sync.sync_all_to_n8n()
            print(f"Sync complete: {result['imported']} imported, {result['failed']} failed")
    
    except Exception as e:
        print(f"❌ Error: {e}")
        exit(1)


if __name__ == "__main__":
    main() 