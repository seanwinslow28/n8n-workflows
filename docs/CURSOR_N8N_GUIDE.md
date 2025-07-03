# 🎯 Cursor + N8N Integration Guide

Complete guide for connecting Cursor to your n8n Docker instance for workflow development and testing.

## 🚀 Quick Start

### 1. Generate n8n API Key

1. Open your n8n instance: http://localhost:5678
2. Click your profile icon → **Settings**
3. Click **API** in the left sidebar
4. Click **Create API Key**
5. Copy the generated key (you'll only see it once!)

### 2. Run the Setup Script

```bash
# Install dependencies
pip install -r requirements.txt

# Run the setup assistant
python setup_n8n.py
```

The setup script will:
- ✅ Check your Docker n8n instance
- ✅ Test the API connection
- ✅ Save your API key securely
- ✅ Show your workflow summary
- ✅ Optionally sync workflows

### 3. Test Your Connection

```bash
# Quick connection test
python test_n8n.py

# Or test manually
python n8n_client.py test
```

## 🛠 Available Tools

### 1. **N8N Client** (`n8n_client.py`)
Direct API client for managing workflows:

```bash
# List all workflows
python n8n_client.py list

# List only active workflows
python n8n_client.py list --active

# Export specific workflow
python n8n_client.py export SCbZjNc21BRf0QTI

# Test connection
python n8n_client.py test
```

### 2. **Workflow Tester** (`workflow_tester.py`)
Advanced testing for individual workflows:

```bash
# Get workflow details
python workflow_tester.py SCbZjNc21BRf0QTI --action details

# Test workflow execution
python workflow_tester.py SCbZjNc21BRf0QTI --action test

# Export and analyze workflow
python workflow_tester.py SCbZjNc21BRf0QTI --action export

# Test webhook endpoints
python workflow_tester.py SCbZjNc21BRf0QTI --action webhooks

# Activate/deactivate workflow
python workflow_tester.py SCbZjNc21BRf0QTI --action activate
python workflow_tester.py SCbZjNc21BRf0QTI --action deactivate
```

### 3. **Documentation Server** (`run.py`)
Browse your workflow collection:

```bash
# Start documentation server
python run.py

# Open http://localhost:8000
```

## 🔧 Working with Your Specific Workflow

For your workflow: `http://localhost:5678/workflow/SCbZjNc21BRf0QTI`

### Quick Analysis
```bash
# Get full details
python workflow_tester.py SCbZjNc21BRf0QTI --action export

# Test execution
python workflow_tester.py SCbZjNc21BRf0QTI --action test

# Check webhook endpoints
python workflow_tester.py SCbZjNc21BRf0QTI --action webhooks
```

### Export to Local File
```bash
# Export the workflow
python n8n_client.py export SCbZjNc21BRf0QTI

# The file will be saved to workflows/ directory
```

### Test with Custom Input
```bash
# Test with JSON input
python workflow_tester.py SCbZjNc21BRf0QTI --action test --input '{"key": "value"}'
```

## 🔄 Sync Workflows

### From n8n to Local Files
```bash
# Export all workflows from n8n
python n8n_client.py sync-from-n8n
```

### From Local Files to n8n
```bash
# Import all local workflows to n8n
python n8n_client.py sync-to-n8n
```

## 📊 Python API Usage

### Basic Usage
```python
from n8n_client import N8nClient
from workflow_tester import WorkflowTester

# Initialize client
client = N8nClient()

# Get all workflows
workflows = client.get_workflows()

# Test specific workflow
tester = WorkflowTester()
result = tester.test_workflow_execution('SCbZjNc21BRf0QTI')
```

### Advanced Usage
```python
# Get workflow details
details = tester.get_workflow_details('SCbZjNc21BRf0QTI')
print(f"Workflow has {details['stats']['total_nodes']} nodes")

# Test webhooks
webhook_results = tester.test_webhook_endpoints('SCbZjNc21BRf0QTI')
for result in webhook_results:
    print(f"Webhook: {result['webhook_url']} - Status: {result['test_result']['status_code']}")
```

## 🔐 Environment Variables

Create a `.env` file in your project root:

```env
N8N_API_KEY=your_api_key_here
N8N_BASE_URL=http://localhost:5678
```

## 🐛 Troubleshooting

### Connection Issues
```bash
# Check if n8n is running
docker ps | grep n8n

# Test API access
curl -H "X-N8N-API-KEY: your_key" http://localhost:5678/api/v1/workflows

# Test connection with Python
python n8n_client.py test
```

### API Key Issues
- Make sure you copied the full API key
- The key is only shown once - create a new one if lost
- Check that API access is enabled in n8n settings

### Workflow Not Found
```bash
# List all workflows to find the correct ID
python n8n_client.py list

# Check if workflow exists in n8n
curl -H "X-N8N-API-KEY: your_key" http://localhost:5678/api/v1/workflows/SCbZjNc21BRf0QTI
```

## 📁 File Structure

```
n8n-workflows/
├── n8n_client.py          # Main API client
├── workflow_tester.py     # Workflow testing utility
├── setup_n8n.py           # Setup assistant
├── test_n8n.py            # Quick connection test
├── .env                   # Environment variables
├── workflows/             # Local workflow files
└── static/                # Documentation UI
```

## 🎯 Common Workflows

### Daily Development
```bash
# 1. Check workflow status
python workflow_tester.py SCbZjNc21BRf0QTI --action details

# 2. Export for editing
python n8n_client.py export SCbZjNc21BRf0QTI

# 3. Test changes
python workflow_tester.py SCbZjNc21BRf0QTI --action test

# 4. Check webhooks
python workflow_tester.py SCbZjNc21BRf0QTI --action webhooks
```

### Debugging
```bash
# Get execution history
python workflow_tester.py SCbZjNc21BRf0QTI --action details | grep -A 10 "executions"

# Test specific webhook
python workflow_tester.py SCbZjNc21BRf0QTI --action webhooks

# Check workflow structure
python workflow_tester.py SCbZjNc21BRf0QTI --action export
```

## 🔗 Links

- **Your n8n Instance**: http://localhost:5678
- **Your Workflow**: http://localhost:5678/workflow/SCbZjNc21BRf0QTI
- **Documentation**: http://localhost:8000 (after running `python run.py`)

## 💡 Tips

1. **Always export before major changes** - keeps a local backup
2. **Use the tester for debugging** - shows detailed execution info
3. **Check webhook endpoints** - common source of issues
4. **Monitor executions** - use the details command to see recent runs
5. **Keep API key secure** - stored in .env file, not in code

Happy workflow automation! 🚀 