# Notion Tools

Tools for working with Notion databases and n8n Notion node configuration.

## Database Management

### `setup_notion_database.py`
Complete guided setup for creating a Notion database with all required fields.

### `create_database_direct.py`
Direct database creation script for advanced users.

### `enhance_database_with_views.py`
Add ChatGPT-suggested views and additional fields to existing databases.

## Field Configuration

### `notion_field_config.py`
Configuration helper for database fields and properties.

### `notion_properties_copy_paste.json`
**⭐ MOST USEFUL**: JSON file with all 23 property mappings for manual n8n configuration.

### `notion_view_templates.json`
Template configurations for different database views.

## Node Configuration

### `notion_node_manual_config.md`
**⭐ ESSENTIAL**: Step-by-step guide for manually configuring the n8n Notion node.

### `update_n8n_notion_node.py`
Script to update n8n Notion node via API (may have validation issues).

### `fix_notion_node.py`
Attempts to fix common Notion node configuration issues.

### `replace_notion_node.py`
Replace entire Notion node configuration.

### `update_notion_node_correct.py`
Update Notion node with correct format.

## JSON Configurations

### `notion_node_complete.json`
Complete Notion node configuration in JSON format.

### `notion_node_correct_format.json`
Notion node configuration using proper n8n format.

## Testing & Verification

### `test_notion_connection.py`
Test Notion API connection and verify database access.

### `update_notion_fields.py`
Update and verify database field configurations.

## Quick Start

1. **Setup Database**: Run `python3 setup_notion_database.py`
2. **Configure n8n Node**: Use `notion_node_manual_config.md` guide
3. **Copy Properties**: Use `notion_properties_copy_paste.json` for manual configuration
4. **Test Connection**: Run `python3 test_notion_connection.py`

## Environment Variables Required

```
NOTION_API_TOKEN=your_notion_api_token
NOTION_DATABASE_ID=your_database_id
``` 