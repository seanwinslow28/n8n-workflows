# ⚡ N8N Workflow Collection & Documentation

A professionally organized collection of **2,053 n8n workflows** with a lightning-fast documentation system that provides instant search, analysis, and browsing capabilities.

## 🚀 **NEW: AI Chat Evaluation - Dual LLM Comparison System**

**🎯 FEATURED WORKFLOW: Compare GPT-3.5 vs Claude-3.5 side-by-side!**

### 🤖 Dual LLM Comparison Features
- **Parallel AI Evaluation**: GPT-3.5-turbo vs Claude-3.5-Sonnet
- **6 Evaluation Metrics**: Helpfulness, Accuracy, Clarity, Relevance, Tone, Completeness
- **Agreement Analysis**: Calculates score differences and agreement levels
- **Dual Notion Databases**: Side-by-side comparison tables
- **Performance Tracking**: Identifies which LLM scores higher
- **Structured Output**: Detailed reasoning from both models

### Quick Start - Dual LLM System
```bash
# 1. Set up the workflow (see DUAL_LLM_IMPLEMENTATION_SUMMARY.md)
# 2. Configure your API keys in n8n (OpenAI + Anthropic)
# 3. Import the workflow: workflows/AI_Chat_Evaluation_Dual_LLM_Comparison.json
# 4. Test with: python tests/test_dual_llm_workflow.py

# Webhook endpoint:
POST http://localhost:5678/webhook/dual-llm-comparison
```

## 🚀 **High-Performance Documentation System**

**Experience 100x performance improvement over traditional documentation!**

### Quick Start - Fast Documentation System
```bash
# Install dependencies
pip install -r requirements.txt

# Start the fast API server
python run.py

# Open in browser
http://localhost:8000
```

**Features:**
- ⚡ **Sub-100ms response times** with SQLite FTS5 search
- 🔍 **Instant full-text search** with advanced filtering
- 📱 **Responsive design** - works perfectly on mobile
- 🌙 **Dark/light themes** with system preference detection
- 📊 **Live statistics** - 365 unique integrations, 29,445 total nodes
- 🎯 **Smart categorization** by trigger type and complexity
- 📄 **On-demand JSON viewing** and download
- 🔗 **Mermaid diagram generation** for workflow visualization
- 🔄 **Real-time workflow naming** with intelligent formatting

### Performance Comparison

| Metric | Old System | New System | Improvement |
|--------|------------|------------|-------------|
| **File Size** | 71MB HTML | <100KB | **700x smaller** |
| **Load Time** | 10+ seconds | <1 second | **10x faster** |
| **Search** | Client-side only | Full-text with FTS5 | **Instant** |
| **Memory Usage** | ~2GB RAM | <50MB RAM | **40x less** |
| **Mobile Support** | Poor | Excellent | **Fully responsive** |

---

## 📂 Repository Organization

### Workflow Collection
- **2,053 workflows** with meaningful, searchable names
- **365 unique integrations** across popular platforms
- **29,445 total nodes** with professional categorization
- **Quality assurance** - All workflows analyzed and categorized

### Advanced Naming System ✨
Our intelligent naming system converts technical filenames into readable titles:
- **Before**: `2051_Telegram_Webhook_Automation_Webhook.json`
- **After**: `Telegram Webhook Automation`
- **100% meaningful names** with smart capitalization
- **Automatic integration detection** from node analysis

---

## 📁 Project Structure

### Organized Directory Layout
```
n8n-workflows/
├── 📂 tools/          # Specialized tools
│   ├── 📂 notion/     # Notion database management
│   └── 📂 n8n/        # n8n workflow tools
├── 📂 docs/           # Documentation
├── 📂 tests/          # Test files and sample data
├── 📂 backups/        # Workflow backups
├── 📂 workflows/      # 2,053 workflow JSON files
├── 📂 static/         # Web interface assets
├── 📄 api_server.py   # FastAPI documentation server
├── 📄 workflow_db.py  # Database management
├── 📄 run.py          # Application launcher
└── 📄 README.md       # This file
```

### Key Directories

#### `/tools/`
Specialized tools for workflow management:
- **`notion/`**: Database creation, field configuration, node setup
- **`n8n/`**: API client, workflow testing, setup assistance

#### `/docs/`
Complete documentation:
- **`CURSOR_N8N_GUIDE.md`**: Essential setup guide
- **`CLAUDE.md`**: Development notes

#### `/tests/`
Testing and validation:
- **`test_webhook.py`**: Webhook testing script
- **`test_sample_data.json`**: Sample data for testing

#### `/backups/`
Workflow backups and version control

---

## 🛠 Usage Instructions

### Option 1: Modern Fast System (Recommended)
```bash
# Clone repository
git clone <repo-url>
cd n8n-workflows

# Install Python dependencies
pip install -r requirements.txt

# Start the documentation server
python run.py

# Browse workflows at http://localhost:8000
# - Instant search across 2,053 workflows
# - Professional responsive interface
# - Real-time workflow statistics
```

### Option 2: Development Mode
```bash
# Start with auto-reload for development
python run.py --dev

# Or specify custom host/port
python run.py --host 0.0.0.0 --port 3000

# Force database reindexing
python run.py --reindex
```

### Import Workflows into n8n
```bash
# Use the Python importer (recommended)
python import_workflows.py

# Or manually import individual workflows:
# 1. Open your n8n Editor UI
# 2. Click menu (☰) → Import workflow
# 3. Choose any .json file from the workflows/ folder
# 4. Update credentials/webhook URLs before running
```

---

## 📊 Workflow Statistics

### Current Collection Stats
- **Total Workflows**: 2,053 automation workflows
- **Active Workflows**: 215 (10.5% active rate)
- **Total Nodes**: 29,445 (avg 14.3 nodes per workflow)
- **Unique Integrations**: 365 different services and APIs
- **Database**: SQLite with FTS5 full-text search

### Trigger Distribution
- **Complex**: 831 workflows (40.5%) - Multi-trigger systems
- **Webhook**: 519 workflows (25.3%) - API-triggered automations  
- **Manual**: 477 workflows (23.2%) - User-initiated workflows
- **Scheduled**: 226 workflows (11.0%) - Time-based executions

### Complexity Analysis
- **Low (≤5 nodes)**: ~35% - Simple automations
- **Medium (6-15 nodes)**: ~45% - Standard workflows
- **High (16+ nodes)**: ~20% - Complex enterprise systems

### Popular Integrations
Top services by usage frequency:
- **Communication**: Telegram, Discord, Slack, WhatsApp
- **Cloud Storage**: Google Drive, Google Sheets, Dropbox
- **Databases**: PostgreSQL, MySQL, MongoDB, Airtable
- **AI/ML**: OpenAI, Anthropic, Hugging Face
- **Development**: HTTP Request, Webhook, GraphQL

---

## 🔍 Advanced Search Features

### Smart Search Categories
Our system automatically categorizes workflows into 12 service categories:

#### Available Categories:
- **messaging**: Telegram, Discord, Slack, WhatsApp, Teams
- **ai_ml**: OpenAI, Anthropic, Hugging Face 
- **database**: PostgreSQL, MySQL, MongoDB, Redis, Airtable
- **email**: Gmail, Mailjet, Outlook, SMTP/IMAP
- **cloud_storage**: Google Drive, Google Docs, Dropbox, OneDrive
- **project_management**: Jira, GitHub, GitLab, Trello, Asana
- **social_media**: LinkedIn, Twitter/X, Facebook, Instagram
- **ecommerce**: Shopify, Stripe, PayPal
- **analytics**: Google Analytics, Mixpanel
- **calendar_tasks**: Google Calendar, Cal.com, Calendly
- **forms**: Typeform, Google Forms, Form Triggers
- **development**: Webhook, HTTP Request, GraphQL, SSE

### API Usage Examples
```bash
# Search workflows by text
curl "http://localhost:8000/api/workflows?q=telegram+automation"

# Filter by trigger type and complexity
curl "http://localhost:8000/api/workflows?trigger=Webhook&complexity=high"

# Find all messaging workflows
curl "http://localhost:8000/api/workflows/category/messaging"

# Get database statistics
curl "http://localhost:8000/api/stats"

# Browse available categories
curl "http://localhost:8000/api/categories"
```

---

## 🏗 Technical Architecture

### Modern Stack
- **SQLite Database** - FTS5 full-text search with 365 indexed integrations
- **FastAPI Backend** - RESTful API with automatic OpenAPI documentation
- **Responsive Frontend** - Modern HTML5 with embedded CSS/JavaScript
- **Smart Analysis** - Automatic workflow categorization and naming

### Key Features
- **Change Detection** - MD5 hashing for efficient re-indexing
- **Background Processing** - Non-blocking workflow analysis
- **Compressed Responses** - Gzip middleware for optimal speed
- **Error Handling** - Graceful degradation and comprehensive logging
- **Mobile Optimization** - Touch-friendly interface design

### Database Performance
```sql
-- Optimized schema for lightning-fast queries
CREATE TABLE workflows (
    id INTEGER PRIMARY KEY,
    filename TEXT UNIQUE,
    name TEXT,
    active BOOLEAN,
    trigger_type TEXT,
    complexity TEXT,
    node_count INTEGER,
    integrations TEXT,  -- JSON array of 365 unique services
    description TEXT,
    file_hash TEXT,     -- MD5 for change detection
    analyzed_at TIMESTAMP
);

-- Full-text search with ranking
CREATE VIRTUAL TABLE workflows_fts USING fts5(
    filename, name, description, integrations, tags,
    content='workflows', content_rowid='id'
);
```

---

## 🔧 Setup & Requirements

### System Requirements
- **Python 3.7+** - For running the documentation system
- **Modern Browser** - Chrome, Firefox, Safari, Edge
- **50MB Storage** - For SQLite database and indexes
- **n8n Instance** - For importing and running workflows

### Installation
```bash
# Clone repository
git clone <repo-url>
cd n8n-workflows

# Install dependencies
pip install -r requirements.txt

# Start documentation server
python run.py

# Access at http://localhost:8000
```

### Development Setup
```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or .venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run with auto-reload for development
python api_server.py --reload

# Force database reindexing
python workflow_db.py --index --force
```

---

## 📋 Naming Convention

### Intelligent Formatting System
Our system automatically converts technical filenames to user-friendly names:

```bash
# Automatic transformations:
2051_Telegram_Webhook_Automation_Webhook.json → "Telegram Webhook Automation"
0250_HTTP_Discord_Import_Scheduled.json → "HTTP Discord Import Scheduled"  
0966_OpenAI_Data_Processing_Manual.json → "OpenAI Data Processing Manual"
```

### Technical Format
```
[ID]_[Service1]_[Service2]_[Purpose]_[Trigger].json
```

### Smart Capitalization Rules
- **HTTP** → HTTP (not Http)
- **API** → API (not Api)  
- **webhook** → Webhook
- **automation** → Automation
- **scheduled** → Scheduled

---

## 🚀 API Documentation

### Core Endpoints
- `GET /` - Main workflow browser interface
- `GET /api/stats` - Database statistics and metrics
- `GET /api/workflows` - Search with filters and pagination
- `GET /api/workflows/{filename}` - Detailed workflow information
- `GET /api/workflows/{filename}/download` - Download workflow JSON
- `GET /api/workflows/{filename}/diagram` - Generate Mermaid diagram

### Advanced Search
- `GET /api/workflows/category/{category}` - Search by service category
- `GET /api/categories` - List all available categories
- `GET /api/integrations` - Get integration statistics
- `POST /api/reindex` - Trigger background reindexing

### Response Examples
```json
// GET /api/stats
{
  "total": 2053,
  "active": 215,
  "inactive": 1838,
  "triggers": {
    "Complex": 831,
    "Webhook": 519,
    "Manual": 477,
    "Scheduled": 226
  },
  "total_nodes": 29445,
  "unique_integrations": 365
}
```

---

## 🤝 Contributing

### Adding New Workflows
1. **Export workflow** as JSON from n8n
2. **Name descriptively** following the established pattern
3. **Add to workflows/** directory
4. **Remove sensitive data** (credentials, personal URLs)
5. **Run reindexing** to update the database

### Quality Standards
- ✅ Workflow must be functional and tested
- ✅ Remove all credentials and sensitive data
- ✅ Follow naming convention for consistency
- ✅ Verify compatibility with recent n8n versions
- ✅ Include meaningful description or comments

---

## ⚠️ Important Notes

### Security & Privacy
- **Review before use** - All workflows shared as-is for educational purposes
- **Update credentials** - Replace API keys, tokens, and webhooks
- **Test safely** - Verify in development environment first
- **Check permissions** - Ensure proper access rights for integrations

### Compatibility
- **n8n Version** - Compatible with n8n 1.0+ (most workflows)
- **Community Nodes** - Some workflows may require additional node installations
- **API Changes** - External services may have updated their APIs since creation
- **Dependencies** - Verify required integrations before importing

---

## 📚 Resources & References

### Workflow Sources
This comprehensive collection includes workflows from:
- **Official n8n.io** - Documentation and community examples
- **GitHub repositories** - Open source community contributions  
- **Blog posts & tutorials** - Real-world automation patterns
- **User submissions** - Tested and verified workflows
- **Enterprise use cases** - Business process automations

### Learn More
- [n8n Documentation](https://docs.n8n.io/) - Official documentation
- [n8n Community](https://community.n8n.io/) - Community forum and support
- [Workflow Templates](https://n8n.io/workflows/) - Official template library
- [Integration Docs](https://docs.n8n.io/integrations/) - Service-specific guides

---

## 🏆 Project Achievements

### Repository Transformation
- **2,053 workflows** professionally organized and named
- **365 unique integrations** automatically detected and categorized
- **100% meaningful names** (improved from basic filename patterns)
- **Zero data loss** during intelligent renaming process
- **Advanced search** with 12 service categories

### Performance Revolution
- **Sub-100ms search** with SQLite FTS5 full-text indexing
- **Instant filtering** across 29,445 workflow nodes
- **Mobile-optimized** responsive design for all devices
- **Real-time statistics** with live database queries
- **Professional interface** with modern UX principles

### System Reliability
- **Robust error handling** with graceful degradation
- **Change detection** for efficient database updates
- **Background processing** for non-blocking operations
- **Comprehensive logging** for debugging and monitoring
- **Production-ready** with proper middleware and security

---

*This repository represents the most comprehensive and well-organized collection of n8n workflows available, featuring cutting-edge search technology and professional documentation that makes workflow discovery and usage a delightful experience.*

**🎯 Perfect for**: Developers, automation engineers, business analysts, and anyone looking to streamline their workflows with proven n8n automations.