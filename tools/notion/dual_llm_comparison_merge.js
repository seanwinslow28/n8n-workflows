// DUAL LLM COMPARISON MERGE CODE
// This node combines and analyzes results from both GPT and Claude
// Use this code in a "Code" node that receives inputs from both AI Agents

// Get original session data from Code node
const originalData = $('Code').first().json;

// Get GPT evaluation results
const gptResults = $('GPT Agent').first().json;

// Get Claude evaluation results  
const claudeResults = $('Claude Agent').first().json;

// Helper function to calculate score differences and agreement
function calculateComparison(gptScore, claudeScore) {
  const difference = Math.abs(gptScore - claudeScore);
  let agreement;
  if (difference <= 1) agreement = 'High';
  else if (difference <= 2) agreement = 'Medium';
  else agreement = 'Low';
  
  return {
    difference: difference.toFixed(1),
    agreement: agreement,
    gpt_higher: gptScore > claudeScore,
    claude_higher: claudeScore > gptScore
  };
}

// Calculate detailed comparisons for each metric
const metrics = ['helpfulness', 'accuracy', 'clarity', 'relevance', 'tone', 'completeness'];
const comparisons = {};
let totalDifference = 0;
let highAgreements = 0;

metrics.forEach(metric => {
  const gptScore = gptResults[metric].score;
  const claudeScore = claudeResults[metric].score;
  const comparison = calculateComparison(gptScore, claudeScore);
  
  comparisons[metric] = comparison;
  totalDifference += parseFloat(comparison.difference);
  if (comparison.agreement === 'High') highAgreements++;
});

// Calculate overall metrics
const overallAgreementRate = ((highAgreements / metrics.length) * 100).toFixed(1);
const averageDifference = (totalDifference / metrics.length).toFixed(2);
const overallComparison = calculateComparison(gptResults.overall_score, claudeResults.overall_score);

// Determine which LLM scored higher overall
const gptTotalScore = metrics.reduce((sum, metric) => sum + gptResults[metric].score, 0);
const claudeTotalScore = metrics.reduce((sum, metric) => sum + claudeResults[metric].score, 0);
const higherScoringLLM = gptTotalScore > claudeTotalScore ? 'GPT-3.5' : 
                        claudeTotalScore > gptTotalScore ? 'Claude-3.5' : 'Tie';

// Create comparison summary
const comparisonSummary = {
  session_id: originalData.sessionId,
  timestamp: originalData.timestamp,
  agreement_rate: overallAgreementRate + '%',
  avg_score_difference: averageDifference,
  higher_scoring_llm: higherScoringLLM,
  gpt_total_score: gptTotalScore.toFixed(1),
  claude_total_score: claudeTotalScore.toFixed(1),
  score_gap: Math.abs(gptTotalScore - claudeTotalScore).toFixed(1)
};

// Create GPT Database Entry
const gptDatabaseData = {
  // Session metadata
  sessionId: originalData.sessionId,
  timestamp: originalData.timestamp,
  userId: originalData.userId || 'anonymous',
  duration: originalData.duration || 0,
  messageCount: originalData.messageCount || 0,
  userMessageCount: originalData.userMessageCount || 0,
  assistantMessageCount: originalData.assistantMessageCount || 0,
  
  // Model identification
  model: 'GPT-3.5-turbo',
  evaluator: 'GPT-3.5-turbo',
  
  // Evaluation scores
  helpfulness: gptResults.helpfulness.score,
  accuracy: gptResults.accuracy.score,
  clarity: gptResults.clarity.score,
  relevance: gptResults.relevance.score,
  tone: gptResults.tone.score,
  completeness: gptResults.completeness.score,
  overall_score: gptResults.overall_score,
  
  // Detailed reasoning (truncated for Notion limits)
  helpfulness_reason: gptResults.helpfulness.reason.substring(0, 2000),
  accuracy_reason: gptResults.accuracy.reason.substring(0, 2000),
  clarity_reason: gptResults.clarity.reason.substring(0, 2000),
  relevance_reason: gptResults.relevance.reason.substring(0, 2000),
  tone_reason: gptResults.tone.reason.substring(0, 2000),
  completeness_reason: gptResults.completeness.reason.substring(0, 2000),
  
  // Analysis fields
  key_insights: gptResults.key_insights.substring(0, 2000),
  improvement_suggestions: gptResults.improvement_suggestions.substring(0, 2000),
  conversation_summary: gptResults.conversation_summary.substring(0, 2000),
  
  // Comparison metrics
  compared_against: 'Claude-3.5-Sonnet',
  overall_agreement: comparisonSummary.agreement_rate,
  avg_score_difference: comparisonSummary.avg_score_difference,
  higher_scoring: higherScoringLLM === 'GPT-3.5' ? 'This Model' : 
                  higherScoringLLM === 'Claude-3.5' ? 'Competitor' : 'Tie',
  
  // Individual score comparisons
  helpfulness_vs_claude: comparisons.helpfulness.difference,
  accuracy_vs_claude: comparisons.accuracy.difference,
  clarity_vs_claude: comparisons.clarity.difference,
  relevance_vs_claude: comparisons.relevance.difference,
  tone_vs_claude: comparisons.tone.difference,
  completeness_vs_claude: comparisons.completeness.difference,
  
  // Agreement levels
  helpfulness_agreement: comparisons.helpfulness.agreement,
  accuracy_agreement: comparisons.accuracy.agreement,
  clarity_agreement: comparisons.clarity.agreement,
  relevance_agreement: comparisons.relevance.agreement,
  tone_agreement: comparisons.tone.agreement,
  completeness_agreement: comparisons.completeness.agreement
};

// Create Claude Database Entry
const claudeDatabaseData = {
  // Session metadata
  sessionId: originalData.sessionId,
  timestamp: originalData.timestamp,
  userId: originalData.userId || 'anonymous',
  duration: originalData.duration || 0,
  messageCount: originalData.messageCount || 0,
  userMessageCount: originalData.userMessageCount || 0,
  assistantMessageCount: originalData.assistantMessageCount || 0,
  
  // Model identification
  model: 'Claude-3.5-Sonnet',
  evaluator: 'Claude-3.5-Sonnet',
  
  // Evaluation scores
  helpfulness: claudeResults.helpfulness.score,
  accuracy: claudeResults.accuracy.score,
  clarity: claudeResults.clarity.score,
  relevance: claudeResults.relevance.score,
  tone: claudeResults.tone.score,
  completeness: claudeResults.completeness.score,
  overall_score: claudeResults.overall_score,
  
  // Detailed reasoning (truncated for Notion limits)
  helpfulness_reason: claudeResults.helpfulness.reason.substring(0, 2000),
  accuracy_reason: claudeResults.accuracy.reason.substring(0, 2000),
  clarity_reason: claudeResults.clarity.reason.substring(0, 2000),
  relevance_reason: claudeResults.relevance.reason.substring(0, 2000),
  tone_reason: claudeResults.tone.reason.substring(0, 2000),
  completeness_reason: claudeResults.completeness.reason.substring(0, 2000),
  
  // Analysis fields
  key_insights: claudeResults.key_insights.substring(0, 2000),
  improvement_suggestions: claudeResults.improvement_suggestions.substring(0, 2000),
  conversation_summary: claudeResults.conversation_summary.substring(0, 2000),
  
  // Comparison metrics
  compared_against: 'GPT-3.5-turbo',
  overall_agreement: comparisonSummary.agreement_rate,
  avg_score_difference: comparisonSummary.avg_score_difference,
  higher_scoring: higherScoringLLM === 'Claude-3.5' ? 'This Model' : 
                  higherScoringLLM === 'GPT-3.5' ? 'Competitor' : 'Tie',
  
  // Individual score comparisons
  helpfulness_vs_gpt: comparisons.helpfulness.difference,
  accuracy_vs_gpt: comparisons.accuracy.difference,
  clarity_vs_gpt: comparisons.clarity.difference,
  relevance_vs_gpt: comparisons.relevance.difference,
  tone_vs_gpt: comparisons.tone.difference,
  completeness_vs_gpt: comparisons.completeness.difference,
  
  // Agreement levels
  helpfulness_agreement: comparisons.helpfulness.agreement,
  accuracy_agreement: comparisons.accuracy.agreement,
  clarity_agreement: comparisons.clarity.agreement,
  relevance_agreement: comparisons.relevance.agreement,
  tone_agreement: comparisons.tone.agreement,
  completeness_agreement: comparisons.completeness.agreement
};

// Log detailed comparison for debugging
console.log('=== DUAL LLM COMPARISON ANALYSIS ===');
console.log('Session:', originalData.sessionId);
console.log('GPT Total Score:', gptTotalScore.toFixed(1));
console.log('Claude Total Score:', claudeTotalScore.toFixed(1));
console.log('Higher Scoring LLM:', higherScoringLLM);
console.log('Agreement Rate:', comparisonSummary.agreement_rate);
console.log('Average Difference:', comparisonSummary.avg_score_difference);

// Return both datasets for separate Notion databases
return [
  { json: gptDatabaseData, pairedItem: 0 },
  { json: claudeDatabaseData, pairedItem: 1 }
]; 