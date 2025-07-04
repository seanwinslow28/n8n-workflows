# 🔧 NOTION PROPERTY MAPPING - COMPLETE FIX

## 🚨 **Issues Fixed**

### 1. **Data Type Error (CRITICAL)**
- **Problem**: `avg_score_difference` was being sent as string `"4.00"`
- **Solution**: Changed to `parseFloat((totalDifference / metrics.length).toFixed(2))`
- **Result**: Now sends proper number to Notion number field

### 2. **Property Configuration (CRITICAL)**
- **Problem**: Some properties not properly configured in Notion nodes
- **Solution**: Complete property mapping verification

## 📊 **COMPLETE PROPERTY MAPPING**

### **GPT Notion Database**
Database URL: `https://www.notion.so/2260a4634b4e81618e72dd644e0a718f`

| Property Name | Type | n8n Mapping | Data Source |
|---------------|------|-------------|-------------|
| **Session ID** | title | `{{ $json.sessionId }}` | Original session data |
| **Model** | select | `{{ $json.model }}` | "GPT-3.5-turbo" |
| **Overall Score** | number | `{{ $json.overall_score }}` | GPT evaluation overall score |
| **Performance Winner** | select | `{{ $json.higher_scoring }}` | "This Model" / "Competitor" / "Tie" |
| **Agreement Rate** | rich_text | `{{ $json.overall_agreement }}` | "75.0%" format |
| **Avg Score Difference** | number | `{{ $json.avg_score_difference }}` | **NUMBER** (not string!) |
| **Helpfulness** | number | `{{ $json.helpfulness }}` | GPT helpfulness score |
| **Accuracy** | number | `{{ $json.accuracy }}` | GPT accuracy score |
| **Clarity** | number | `{{ $json.clarity }}` | GPT clarity score |
| **Relevance** | number | `{{ $json.relevance }}` | GPT relevance score |
| **Tone** | number | `{{ $json.tone }}` | GPT tone score |
| **Completeness** | number | `{{ $json.completeness }}` | GPT completeness score |
| **Key Insights** | rich_text | `{{ $json.key_insights }}` | GPT generated insights |
| **Timestamp** | date | `{{ $json.timestamp }}` | ISO timestamp |

### **Claude Notion Database**  
Database URL: `https://www.notion.so/2260a4634b4e8154b338d3643dc353b9`

| Property Name | Type | n8n Mapping | Data Source |
|---------------|------|-------------|-------------|
| **Session ID** | title | `{{ $json.sessionId }}` | Original session data |
| **Model** | select | `{{ $json.model }}` | "Claude-3.5-Sonnet" |
| **Overall Score** | number | `{{ $json.overall_score }}` | Claude evaluation overall score |
| **Performance Winner** | select | `{{ $json.higher_scoring }}` | "This Model" / "Competitor" / "Tie" |
| **Agreement Rate** | rich_text | `{{ $json.overall_agreement }}` | "75.0%" format |
| **Avg Score Difference** | number | `{{ $json.avg_score_difference }}` | **NUMBER** (not string!) |
| **Helpfulness** | number | `{{ $json.helpfulness }}` | Claude helpfulness score |
| **Accuracy** | number | `{{ $json.accuracy }}` | Claude accuracy score |
| **Clarity** | number | `{{ $json.clarity }}` | Claude clarity score |
| **Relevance** | number | `{{ $json.relevance }}` | Claude relevance score |
| **Tone** | number | `{{ $json.tone }}` | Claude tone score |
| **Completeness** | number | `{{ $json.completeness }}` | Claude completeness score |
| **Key Insights** | rich_text | `{{ $json.key_insights }}` | Claude generated insights |
| **Timestamp** | date | `{{ $json.timestamp }}` | ISO timestamp |

## 🔍 **Key Changes Made**

### **1. Data Type Fix in Comparison Logic**
```javascript
// OLD (caused error):
const averageDifference = (totalDifference / metrics.length).toFixed(2);

// NEW (fixed):
const averageDifference = parseFloat((totalDifference / metrics.length).toFixed(2));
```

### **2. Credential Configuration**
- Both Notion nodes now properly reference "Notion_Cursor" credentials
- GPT Database: `position: [1120, -100]`
- Claude Database: `position: [1120, 100]`

### **3. Property Value Mapping**
All properties use proper n8n expression syntax:
- Numbers: `"numberValue": "={{ $json.property_name }}"`
- Text: `"textContent": "={{ $json.property_name }}"`
- Select: `"selectValue": "={{ $json.property_name }}"`
- Title: `"title": "={{ $json.property_name }}"`
- Date: `"date": "={{ $json.property_name }}"`

## 🧪 **Testing**

### **Run Comprehensive Test**
```bash
cd /Users/seanwinslow/Desktop/Cursor_n8n_workflow_repo/n8n-workflows
python3 tests/test_dual_llm_final.py
```

### **Verify Results**
1. **GPT Database**: https://www.notion.so/2260a4634b4e81618e72dd644e0a718f
2. **Claude Database**: https://www.notion.so/2260a4634b4e8154b338d3643dc353b9

### **Expected Data**
- **Session ID**: Should appear as title
- **Model**: Should show "GPT-3.5-turbo" or "Claude-3.5-Sonnet"
- **Overall Score**: Should be number (e.g., 7.5)
- **Performance Winner**: Should be "This Model", "Competitor", or "Tie"
- **Agreement Rate**: Should be text like "75.0%"
- **Avg Score Difference**: Should be **NUMBER** (e.g., 1.2, not "1.2")
- **Individual Scores**: Should all be numbers 1-10
- **Key Insights**: Should be rich text
- **Timestamp**: Should be formatted date

## ✅ **Verification Checklist**

- [ ] Import updated workflow JSON
- [ ] Verify Notion credentials are set to "Notion_Cursor"
- [ ] Run test script
- [ ] Check GPT database for new record
- [ ] Check Claude database for new record
- [ ] Verify all properties are filled correctly
- [ ] Confirm no validation errors in n8n
- [ ] Test with different conversation data

## 🎯 **SUCCESS INDICATORS**

1. **n8n Workflow**: All nodes should be green after execution
2. **GPT Database**: New record with all 14 properties filled
3. **Claude Database**: New record with all 14 properties filled
4. **No Errors**: No validation errors in n8n execution log
5. **Proper Data Types**: All number fields show as numbers, not strings

## 🔧 **If Still Getting Errors**

1. **Check Notion Credentials**: Ensure "Notion_Cursor" is properly configured
2. **Verify Database URLs**: Ensure URLs match exactly
3. **Check Property Names**: Ensure property names match database exactly
4. **Review Data Types**: Ensure all number fields get number values
5. **Test Individual Nodes**: Execute nodes one by one to isolate issues

---

**All fixes have been applied to the workflow. The critical issue was the data type mismatch for `avg_score_difference` which is now properly converted to a number.** 