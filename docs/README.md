# Documentation

This directory contains comprehensive documentation for the n8n-workflows project.

## Files

### `CURSOR_N8N_GUIDE.md`
**⭐ ESSENTIAL**: Complete guide for using Cursor with n8n.

**Contents:**
- Initial setup and configuration
- API key management
- Workflow testing procedures
- Troubleshooting common issues
- Best practices

### `CLAUDE.md`
Development notes and conversation history with Claude AI.

## Getting Started

1. **Read the Guide**: Start with `CURSOR_N8N_GUIDE.md` for complete setup instructions
2. **Environment Setup**: Follow the API key configuration steps
3. **Test Connection**: Verify your n8n instance is accessible
4. **Explore Tools**: Use the tools in `/tools/` directory

## Quick Reference

### Essential Commands
```bash
# Test n8n connection
python3 tools/n8n/setup_n8n.py

# Test webhook
python3 tests/test_webhook.py

# Setup Notion database
python3 tools/notion/setup_notion_database.py
```

### Important URLs
- **n8n Instance**: http://localhost:5678
- **API Documentation**: http://localhost:5678/api-docs
- **Workflow**: http://localhost:5678/workflow/SCbZjNc21BRf0QTI

### Environment Variables
```
N8N_API_KEY=your_n8n_api_key
NOTION_API_TOKEN=your_notion_api_token
NOTION_DATABASE_ID=your_database_id
```

## Support

For issues or questions, refer to the troubleshooting sections in `CURSOR_N8N_GUIDE.md` or check the conversation history in `CLAUDE.md`. 