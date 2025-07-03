#!/usr/bin/env python3
"""
N8N Workflow Tester & Manager
Specifically designed for testing and managing individual workflows.
"""

import os
import json
import time
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path
from dotenv import load_dotenv
from n8n_client import N8nClient, N8nSync

# Load environment variables from .env file
load_dotenv()


class WorkflowTester:
    """Test and manage individual n8n workflows."""
    
    def __init__(self, api_key: str = None):
        self.client = N8nClient(api_key=api_key or os.getenv('N8N_API_KEY'))
        self.sync = N8nSync(self.client)
    
    def get_workflow_details(self, workflow_id: str) -> Optional[Dict[str, Any]]:
        """Get detailed information about a specific workflow."""
        try:
            workflow = self.client.get_workflow_by_id(workflow_id)
            if not workflow:
                return None
            
            # Get recent executions
            executions = self.client.get_executions(workflow_id, limit=5)
            
            # Analyze workflow structure
            nodes = workflow.get('nodes', [])
            connections = workflow.get('connections', {})
            
            # Find trigger nodes
            trigger_nodes = [node for node in nodes if node.get('type', '').endswith('Trigger')]
            
            # Find webhook nodes
            webhook_nodes = [node for node in nodes if 'webhook' in node.get('type', '').lower()]
            
            return {
                'workflow': workflow,
                'executions': executions,
                'stats': {
                    'total_nodes': len(nodes),
                    'trigger_nodes': len(trigger_nodes),
                    'webhook_nodes': len(webhook_nodes),
                    'is_active': workflow.get('active', False)
                },
                'triggers': trigger_nodes,
                'webhooks': webhook_nodes
            }
        except Exception as e:
            print(f"❌ Error getting workflow details: {e}")
            return None
    
    def test_workflow_execution(self, workflow_id: str, input_data: Dict[str, Any] = None) -> Dict[str, Any]:
        """Test workflow execution with optional input data."""
        try:
            print(f"🚀 Testing workflow {workflow_id}...")
            
            # Execute the workflow
            execution = self.client.execute_workflow(workflow_id, input_data)
            
            if execution:
                execution_id = execution.get('id')
                print(f"✅ Workflow execution started: {execution_id}")
                
                # Wait a bit and check status
                time.sleep(2)
                execution_details = self.client.get_execution_by_id(execution_id)
                
                if execution_details:
                    status = execution_details.get('status', 'unknown')
                    print(f"📊 Execution status: {status}")
                    
                    if status == 'success':
                        print("🎉 Workflow executed successfully!")
                    elif status == 'error':
                        print("❌ Workflow execution failed")
                        error = execution_details.get('error', {})
                        if error:
                            print(f"Error: {error.get('message', 'Unknown error')}")
                    
                    return {
                        'success': True,
                        'execution_id': execution_id,
                        'status': status,
                        'details': execution_details
                    }
                else:
                    return {
                        'success': False,
                        'message': 'Could not retrieve execution details'
                    }
            else:
                return {
                    'success': False,
                    'message': 'Failed to start workflow execution'
                }
        
        except Exception as e:
            return {
                'success': False,
                'message': f'Execution error: {str(e)}'
            }
    
    def test_webhook_endpoints(self, workflow_id: str) -> List[Dict[str, Any]]:
        """Test webhook endpoints in the workflow."""
        try:
            details = self.get_workflow_details(workflow_id)
            if not details:
                return []
            
            webhook_results = []
            webhook_nodes = details.get('webhooks', [])
            
            for node in webhook_nodes:
                node_name = node.get('name', 'Unknown')
                node_type = node.get('type', 'Unknown')
                
                print(f"🔗 Testing webhook node: {node_name} ({node_type})")
                
                # Try to construct webhook URL
                webhook_path = node.get('parameters', {}).get('path', '')
                if webhook_path:
                    webhook_url = f"http://localhost:5678/webhook/{webhook_path}"
                    
                    # Test the webhook
                    test_result = self.client.test_webhook(webhook_url, 'GET')
                    webhook_results.append({
                        'node_name': node_name,
                        'node_type': node_type,
                        'webhook_url': webhook_url,
                        'test_result': test_result
                    })
                    
                    print(f"  Status: {test_result.get('status_code', 'unknown')}")
                else:
                    webhook_results.append({
                        'node_name': node_name,
                        'node_type': node_type,
                        'webhook_url': None,
                        'test_result': {'status': 'error', 'message': 'No webhook path found'}
                    })
            
            return webhook_results
        
        except Exception as e:
            print(f"❌ Error testing webhooks: {e}")
            return []
    
    def export_and_analyze(self, workflow_id: str) -> bool:
        """Export workflow and provide analysis."""
        try:
            print(f"📥 Exporting workflow {workflow_id}...")
            
            # Export the workflow
            success = self.sync.export_workflow_from_n8n(workflow_id)
            if not success:
                return False
            
            # Get details for analysis
            details = self.get_workflow_details(workflow_id)
            if not details:
                return False
            
            workflow = details['workflow']
            stats = details['stats']
            
            print(f"\n📊 Workflow Analysis")
            print("=" * 40)
            print(f"Name: {workflow.get('name', 'Unnamed')}")
            print(f"ID: {workflow_id}")
            print(f"Active: {'Yes' if stats['is_active'] else 'No'}")
            print(f"Total nodes: {stats['total_nodes']}")
            print(f"Trigger nodes: {stats['trigger_nodes']}")
            print(f"Webhook nodes: {stats['webhook_nodes']}")
            
            # Show recent executions
            executions = details['executions']
            if executions:
                print(f"\nRecent executions ({len(executions)}):")
                for i, exec in enumerate(executions[:3], 1):
                    status = exec.get('status', 'unknown')
                    started = exec.get('startedAt', 'unknown')
                    print(f"  {i}. {status} - {started}")
            
            # Show triggers
            triggers = details['triggers']
            if triggers:
                print(f"\nTrigger nodes:")
                for trigger in triggers:
                    print(f"  • {trigger.get('name', 'Unknown')} ({trigger.get('type', 'Unknown')})")
            
            # Show webhooks
            webhooks = details['webhooks']
            if webhooks:
                print(f"\nWebhook nodes:")
                for webhook in webhooks:
                    print(f"  • {webhook.get('name', 'Unknown')} ({webhook.get('type', 'Unknown')})")
            
            return True
        
        except Exception as e:
            print(f"❌ Error exporting and analyzing: {e}")
            return False
    
    def manage_workflow_state(self, workflow_id: str, action: str) -> bool:
        """Activate or deactivate a workflow."""
        try:
            if action.lower() == 'activate':
                result = self.client.activate_workflow(workflow_id)
                if result:
                    print(f"✅ Workflow {workflow_id} activated")
                else:
                    print(f"❌ Failed to activate workflow {workflow_id}")
                return result
            
            elif action.lower() == 'deactivate':
                result = self.client.deactivate_workflow(workflow_id)
                if result:
                    print(f"✅ Workflow {workflow_id} deactivated")
                else:
                    print(f"❌ Failed to deactivate workflow {workflow_id}")
                return result
            
            else:
                print(f"❌ Unknown action: {action}")
                return False
        
        except Exception as e:
            print(f"❌ Error managing workflow state: {e}")
            return False


def main():
    """CLI interface for workflow testing."""
    import argparse
    
    parser = argparse.ArgumentParser(description="N8N Workflow Tester")
    parser.add_argument("workflow_id", help="Workflow ID to test")
    parser.add_argument("--api-key", help="N8N API key")
    parser.add_argument("--action", choices=['details', 'test', 'export', 'activate', 'deactivate', 'webhooks'],
                       default='details', help="Action to perform")
    parser.add_argument("--input", help="JSON input data for testing")
    
    args = parser.parse_args()
    
    try:
        tester = WorkflowTester(args.api_key)
        
        if args.action == 'details':
            details = tester.get_workflow_details(args.workflow_id)
            if details:
                print(json.dumps(details['workflow'], indent=2))
            else:
                print("❌ Could not retrieve workflow details")
        
        elif args.action == 'test':
            input_data = {}
            if args.input:
                input_data = json.loads(args.input)
            
            result = tester.test_workflow_execution(args.workflow_id, input_data)
            print(json.dumps(result, indent=2))
        
        elif args.action == 'export':
            success = tester.export_and_analyze(args.workflow_id)
            if not success:
                exit(1)
        
        elif args.action in ['activate', 'deactivate']:
            success = tester.manage_workflow_state(args.workflow_id, args.action)
            if not success:
                exit(1)
        
        elif args.action == 'webhooks':
            results = tester.test_webhook_endpoints(args.workflow_id)
            print(json.dumps(results, indent=2))
    
    except Exception as e:
        print(f"❌ Error: {e}")
        exit(1)


if __name__ == "__main__":
    main() 