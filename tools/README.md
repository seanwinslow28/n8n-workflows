# Tools Directory

This directory contains specialized tools for working with n8n workflows and Notion databases.

## Directory Structure

### `/notion/`
Contains tools for working with Notion databases:
- **Database Management**: Create, enhance, and configure Notion databases
- **Field Configuration**: Manage database fields and properties
- **Node Configuration**: Configure n8n Notion nodes with proper field mappings
- **Connection Testing**: Test Notion API connections

### `/n8n/`
Contains tools for working with n8n workflows:
- **API Client**: Direct n8n API interaction
- **Workflow Testing**: Test and debug individual workflows
- **Setup Assistant**: Guided n8n configuration
- **Workflow Management**: Import, export, and manage workflows

## Usage

Each directory contains specialized tools for its respective service. See the individual README files in each subdirectory for specific usage instructions.

## Key Files

- `notion/setup_notion_database.py` - Complete Notion database setup
- `notion/notion_properties_copy_paste.json` - Property mappings for manual configuration
- `n8n/n8n_client.py` - Complete n8n API client
- `n8n/workflow_tester.py` - Test individual workflows 