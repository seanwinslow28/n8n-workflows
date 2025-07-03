# n8n Tools

Tools for working with n8n workflows, API interactions, and workflow management.

## Core API Client

### `n8n_client.py`
**⭐ ESSENTIAL**: Complete n8n API client with full CRUD operations.

**Features:**
- Workflow management (list, get, create, update, delete)
- Workflow execution and monitoring
- Node and connection management
- Authentication handling
- Error handling and logging

**Usage:**
```python
from n8n_client import N8nClient

client = N8nClient(base_url="http://localhost:5678", api_key="your_api_key")
workflows = client.list_workflows()
```

## Workflow Testing

### `workflow_tester.py`
**⭐ VERY USEFUL**: Advanced workflow testing and debugging tool.

**Features:**
- Test individual workflows
- Send test data to webhooks
- Monitor execution results
- Debug workflow issues
- Performance testing

**Usage:**
```bash
python3 workflow_tester.py --workflow-id SCbZjNc21BRf0QTI --test-webhook
```

## Setup & Configuration

### `setup_n8n.py`
**⭐ ESSENTIAL**: Guided n8n setup assistant.

**Features:**
- Environment configuration
- API key setup
- Connection testing
- Workflow validation
- Database integration setup

**Usage:**
```bash
python3 setup_n8n.py
```

## Quick Start

1. **Setup n8n**: Run `python3 setup_n8n.py`
2. **Test Connection**: The setup script will test your API connection
3. **Test Workflows**: Use `workflow_tester.py` to test individual workflows
4. **API Integration**: Use `n8n_client.py` for programmatic access

## Environment Variables Required

```
N8N_API_KEY=your_n8n_api_key
N8N_BASE_URL=http://localhost:5678
```

## Common Use Cases

### Testing a Workflow
```bash
cd tools/n8n
python3 workflow_tester.py --workflow-id YOUR_WORKFLOW_ID
```

### Listing All Workflows
```python
from n8n_client import N8nClient
client = N8nClient()
workflows = client.list_workflows()
for workflow in workflows:
    print(f"{workflow['id']}: {workflow['name']}")
```

### Executing a Workflow
```python
client = N8nClient()
result = client.execute_workflow('YOUR_WORKFLOW_ID', {'test': 'data'})
```

## API Documentation

The n8n API client supports all major n8n API endpoints. See the source code for detailed method documentation and examples. 