# Tests

This directory contains test files and sample data for testing n8n workflows and integrations.

## Files

### `test_webhook.py`
**⭐ ESSENTIAL**: Test webhook endpoints and workflow execution.

**Features:**
- Send test data to workflow webhooks
- Monitor execution results
- Verify response formats
- Debug webhook issues

**Usage:**
```bash
python3 test_webhook.py
```

### `test_sample_data.json`
**⭐ USEFUL**: Realistic sample data for testing AI chat evaluation workflows.

**Contents:**
- Sample conversation data
- User and assistant messages
- Metadata fields
- Analytics data

**Usage:**
```bash
# Use with test_webhook.py
python3 test_webhook.py --data-file test_sample_data.json
```

## Running Tests

### Basic Webhook Test
```bash
cd tests
python3 test_webhook.py
```

### Test with Custom Data
```bash
cd tests
python3 test_webhook.py --data-file your_custom_data.json
```

### Test Specific Workflow
```bash
cd tests
python3 test_webhook.py --workflow-id SCbZjNc21BRf0QTI
```

## Sample Data Format

The test data includes:
- `sessionId`: Unique conversation identifier
- `output`: AI evaluation results with scores
- `messageCount`: Number of messages in conversation
- `duration`: Conversation duration in milliseconds
- `userMessageCount`: Number of user messages
- `assistantMessageCount`: Number of assistant messages
- `averageUserMessageLength`: Average length of user messages
- `averageAssistantMessageLength`: Average length of assistant messages
- `model`: AI model used
- `useCase`: Type of use case
- `tags`: Categorization tags

## Environment Variables

```
N8N_API_KEY=your_n8n_api_key
```

## Troubleshooting

- **Connection Issues**: Verify n8n is running on http://localhost:5678
- **API Key Issues**: Check your N8N_API_KEY in .env file
- **Workflow Issues**: Ensure workflow is active and webhook URL is correct 