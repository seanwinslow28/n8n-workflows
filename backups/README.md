# Backups

This directory contains backup files of workflows and configurations.

## Files

### `workflow_backup_SCbZjNc21BRf0QTI.json`
**⭐ IMPORTANT**: Backup of the "AI Chat Evaluation_Multiple LLMs" workflow.

**Contents:**
- Complete workflow definition
- All node configurations
- Connection mappings
- Parameter settings
- Webhook configurations

**Usage:**
- Restore workflow if needed
- Compare configurations
- Reference for new workflows

## Backup Strategy

### Automatic Backups
Backups are created automatically when making significant changes to workflows:
- Before updating Notion node configurations
- Before changing workflow structure
- Before API modifications

### Manual Backups
Create manual backups before major changes:
```bash
# Export current workflow
python3 tools/n8n/n8n_client.py export-workflow SCbZjNc21BRf0QTI > backups/workflow_backup_$(date +%Y%m%d_%H%M%S).json
```

## Restore Workflow

### From Backup File
```bash
# Restore workflow from backup
python3 tools/n8n/n8n_client.py import-workflow backups/workflow_backup_SCbZjNc21BRf0QTI.json
```

### Manual Restore
1. Open n8n: http://localhost:5678
2. Go to Workflows → Import
3. Select backup file
4. Configure connections and credentials

## File Naming Convention

```
workflow_backup_[WORKFLOW_ID]_[TIMESTAMP].json
```

Examples:
- `workflow_backup_SCbZjNc21BRf0QTI.json` - Main backup
- `workflow_backup_SCbZjNc21BRf0QTI_20250703_141500.json` - Timestamped backup

## Best Practices

1. **Regular Backups**: Create backups before major changes
2. **Version Control**: Keep timestamped versions for rollback
3. **Testing**: Test restored workflows thoroughly
4. **Documentation**: Document changes made between backups 