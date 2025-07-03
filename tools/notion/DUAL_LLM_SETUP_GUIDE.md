# 🚀 DUAL LLM COMPARISON SETUP GUIDE
## GPT-3.5 vs Claude Side-by-Side Evaluation

### 🎯 **OVERVIEW**
This enhanced workflow compares **GPT-3.5-turbo** vs **Claude-3.5-Sonnet** evaluations side-by-side, storing results in **two separate Notion databases** for easy comparison.

---

## 📊 **WORKFLOW ARCHITECTURE**

```
Webhook → Code → [GPT Agent] → [Comparison Merge] → [GPT Database]
              ↘ [Claude Agent] ↗                  ↘ [Claude Database]
```

### **Key Features:**
- ✅ **Parallel Evaluation**: Both LLMs evaluate simultaneously  
- ✅ **Agreement Analysis**: Calculate score differences and agreement levels
- ✅ **Separate Databases**: Side-by-side comparison in two Notion tables
- ✅ **Detailed Insights**: Each LLM's reasoning and perspective
- ✅ **Performance Metrics**: Which LLM scores higher overall

---

## 🗄️ **NOTION DATABASE SETUP**

### **Step 1: Create Two Notion Databases**

#### **Database 1: "GPT Evaluations"**
Create a new Notion database with these properties:

**📋 Required Properties:**
```
Session ID (Title) - Text
Model (Select) - Options: GPT-3.5-turbo
Evaluator (Text) - Text  
Timestamp (Date) - Date & Time
User ID (Text) - Text
Duration (Number) - Number
Message Count (Number) - Number
User Message Count (Number) - Number
Assistant Message Count (Number) - Number

--- EVALUATION SCORES ---
Helpfulness (Number) - Number (0-10)
Accuracy (Number) - Number (0-10)
Clarity (Number) - Number (0-10)
Relevance (Number) - Number (0-10)  
Tone (Number) - Number (0-10)
Completeness (Number) - Number (0-10)
Overall Score (Number) - Number (0-10)

--- DETAILED REASONING ---
Helpfulness Reason (Text) - Text
Accuracy Reason (Text) - Text
Clarity Reason (Text) - Text
Relevance Reason (Text) - Text
Tone Reason (Text) - Text
Completeness Reason (Text) - Text

--- ANALYSIS ---
Key Insights (Text) - Text
Improvement Suggestions (Text) - Text
Conversation Summary (Text) - Text

--- COMPARISON METRICS ---
Compared Against (Text) - Text (Claude-3.5-Sonnet)
Overall Agreement (Text) - Text (% agreement)
Avg Score Difference (Number) - Number
Higher Scoring (Select) - Options: This Model, Competitor, Tie

--- INDIVIDUAL COMPARISONS ---
Helpfulness vs Claude (Number) - Number
Accuracy vs Claude (Number) - Number
Clarity vs Claude (Number) - Number
Relevance vs Claude (Number) - Number
Tone vs Claude (Number) - Number
Completeness vs Claude (Number) - Number

--- AGREEMENT LEVELS ---
Helpfulness Agreement (Select) - Options: High, Medium, Low
Accuracy Agreement (Select) - Options: High, Medium, Low
Clarity Agreement (Select) - Options: High, Medium, Low
Relevance Agreement (Select) - Options: High, Medium, Low
Tone Agreement (Select) - Options: High, Medium, Low
Completeness Agreement (Select) - Options: High, Medium, Low
```

#### **Database 2: "Claude Evaluations"**  
Create an identical database but replace:
- **Model Options**: Claude-3.5-Sonnet
- **Compared Against**: GPT-3.5-turbo
- **Individual Comparisons**: "vs GPT" instead of "vs Claude"

---

## ⚙️ **WORKFLOW CONFIGURATION**

### **Step 2: Import Workflow**
1. Copy the workflow JSON from `AI_Chat_Evaluation_Dual_LLM_Comparison.json`
2. Import into n8n
3. Configure the following nodes:

### **Step 3: Configure LLM Credentials**

#### **OpenAI Configuration (GPT Agent)**
- Add your OpenAI API key to credentials
- Model: `gpt-3.5-turbo`

#### **Anthropic Configuration (Claude Agent)**  
- Add your Anthropic API key to credentials
- Model: `claude-3-5-sonnet-20241022`

### **Step 4: Configure Notion Databases**

#### **GPT Database Node**
```json
{
  "databaseId": "YOUR_GPT_DATABASE_URL",
  "properties": {
    "Session ID": "={{ $json.sessionId }}",
    "Model": "={{ $json.model }}",
    "Evaluator": "={{ $json.evaluator }}",
    // ... all other properties as listed above
  }
}
```

#### **Claude Database Node**
```json
{
  "databaseId": "YOUR_CLAUDE_DATABASE_URL", 
  "properties": {
    "Session ID": "={{ $json.sessionId }}",
    "Model": "={{ $json.model }}",
    "Evaluator": "={{ $json.evaluator }}",
    // ... all other properties as listed above
  }
}
```

### **Step 5: Add Comparison Merge Code**
Copy the code from `dual_llm_comparison_merge.js` into a new Code node between the AI Agents and Notion nodes.

---

## 🔗 **NODE CONNECTIONS**

```
Webhook → Code → GPT Agent ↘
                      ↘      → Comparison Merge → GPT Database
                Claude Agent ↗                    ↘ Claude Database

LLM Models and Tools:
- OpenAI Chat Model → GPT Agent
- Claude Chat Model → Claude Agent  
- Structured Output Parsers → Both Agents
- Calculator Tools → Both Agents
```

---

## 🧪 **TESTING**

### **Step 6: Test the Workflow**

#### **Webhook URL**
After saving, get your webhook URL:
```
http://localhost:5678/webhook/dual-llm-comparison
```

#### **Test Data**
Use the existing `test_sample_data.json` or create new test conversations.

#### **Expected Results**
✅ **Two Database Entries**: One in each Notion database  
✅ **Score Comparisons**: Numerical differences between LLMs  
✅ **Agreement Analysis**: High/Medium/Low agreement levels  
✅ **Detailed Reasoning**: Each LLM's evaluation perspective  

---

## 📈 **ANALYSIS FEATURES**

### **Comparison Insights You'll Get:**

1. **Score Differences**: Exact numerical gaps between evaluations
2. **Agreement Levels**: How often the LLMs agree (High/Medium/Low)
3. **Performance Winner**: Which LLM scores higher overall
4. **Reasoning Styles**: Compare how each LLM justifies scores
5. **Consistency**: Track agreement patterns across sessions

### **Notion Views to Create:**

#### **Side-by-Side Comparison View**
- Filter by Session ID
- Show both databases side-by-side
- Compare scores and reasoning

#### **Agreement Analysis View**  
- Group by Agreement Levels
- Show sessions where LLMs disagree
- Identify evaluation patterns

#### **Performance Tracking View**
- Track which LLM scores higher over time
- Average score comparisons
- Quality trends

---

## 🎯 **USAGE SCENARIOS**

### **Quality Assurance**
- Validate evaluation consistency
- Identify edge cases where LLMs disagree
- Improve prompt engineering

### **Model Selection**
- Determine which LLM is better for your use case
- Cost vs performance analysis
- Bias detection between models

### **Research & Analysis**
- Study evaluation patterns
- Compare reasoning approaches
- Understand model strengths/weaknesses

---

## 🔧 **TROUBLESHOOTING**

### **Common Issues:**
1. **Credential Errors**: Ensure both OpenAI and Anthropic API keys are valid
2. **Database Connection**: Verify Notion database URLs are correct
3. **Property Mismatch**: Ensure all database properties match the merge code output
4. **Rate Limits**: Monitor API usage for both providers

### **Debug Tips:**
- Check the Comparison Merge node logs for detailed analysis
- Use n8n's execution view to trace data flow
- Test with simple conversations first

---

## 🚀 **NEXT STEPS**

1. **Import the workflow** 
2. **Set up your two Notion databases**
3. **Configure API credentials**
4. **Run test evaluations**
5. **Analyze the side-by-side results!**

Ready to see how GPT and Claude compare? Let's build this! 🎉 