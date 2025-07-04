// FIXED DUAL LLM COMPARISON MERGE CODE
// Get original session data from Code node
const originalData = $('Code').first().json;

// FIXED: Properly access the structured output from AI Agent nodes
// The structured output parser integrates the parsed data directly into the json object
const gptResults = $input.first().json;
const claudeResults = $input.last().json;

// Add debugging to see the actual data structure
console.log('=== DEBUGGING DATA STRUCTURE ===');
console.log('GPT Results Keys:', Object.keys(gptResults));
console.log('Claude Results Keys:', Object.keys(claudeResults));
console.log('GPT Results Sample:', JSON.stringify(gptResults, null, 2).substring(0, 500));
console.log('Claude Results Sample:', JSON.stringify(claudeResults, null, 2).substring(0, 500));

// Helper function to safely access nested properties
function safeAccess(obj, path, defaultValue = null) {
  try {
    return path.split('.').reduce((current, key) => current && current[key], obj) || defaultValue;
  } catch (e) {
    console.log(`Error accessing ${path}:`, e.message);
    return defaultValue;
  }
}

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

// Safely extract scores - try multiple possible data structures
function extractScore(results, metric) {
  // Try different possible paths where the data might be stored
  const possiblePaths = [
    `${metric}.score`,           // Standard structured output
    `output.${metric}.score`,    // If wrapped in output
    `parsed.${metric}.score`,    // If wrapped in parsed
    `result.${metric}.score`,    // If wrapped in result
    metric                       // If it's a direct property
  ];
  
  for (const path of possiblePaths) {
    const score = safeAccess(results, path);
    if (score !== null && typeof score === 'number') {
      return score;
    }
  }
  
  console.log(`Warning: Could not find score for ${metric}`);
  return 5; // Default score if not found
}

function extractReason(results, metric) {
  const possiblePaths = [
    `${metric}.reason`,
    `output.${metric}.reason`,
    `parsed.${metric}.reason`,
    `result.${metric}.reason`
  ];
  
  for (const path of possiblePaths) {
    const reason = safeAccess(results, path);
    if (reason && typeof reason === 'string') {
      return reason.substring(0, 2000);
    }
  }
  
  return `Evaluation for ${metric}`;
}

function extractOverallScore(results) {
  const possiblePaths = [
    'overall_score',
    'output.overall_score',
    'parsed.overall_score',
    'result.overall_score'
  ];
  
  for (const path of possiblePaths) {
    const score = safeAccess(results, path);
    if (score !== null && typeof score === 'number') {
      return score;
    }
  }
  
  console.log('Warning: Could not find overall_score');
  return 7.5; // Default overall score
}

function extractStringField(results, field) {
  const possiblePaths = [
    field,
    `output.${field}`,
    `parsed.${field}`,
    `result.${field}`
  ];
  
  for (const path of possiblePaths) {
    const value = safeAccess(results, path);
    if (value && typeof value === 'string') {
      return value.substring(0, 2000);
    }
  }
  
  return `Generated ${field}`;
}

// Calculate detailed comparisons for each metric
const metrics = ['helpfulness', 'accuracy', 'clarity', 'relevance', 'tone', 'completeness'];
const comparisons = {};
let totalDifference = 0;
let highAgreements = 0;

// Extract scores safely
const gptScores = {};
const claudeScores = {};

metrics.forEach(metric => {
  gptScores[metric] = extractScore(gptResults, metric);
  claudeScores[metric] = extractScore(claudeResults, metric);
  
  const comparison = calculateComparison(gptScores[metric], claudeScores[metric]);
  comparisons[metric] = comparison;
  totalDifference += parseFloat(comparison.difference);
  if (comparison.agreement === 'High') highAgreements++;
  
  console.log(`${metric}: GPT=${gptScores[metric]}, Claude=${claudeScores[metric]}, Diff=${comparison.difference}`);
});

// Calculate overall metrics
const overallAgreementRate = ((highAgreements / metrics.length) * 100).toFixed(1);
const averageDifference = (totalDifference / metrics.length).toFixed(2);

const gptOverallScore = extractOverallScore(gptResults);
const claudeOverallScore = extractOverallScore(claudeResults);
const overallComparison = calculateComparison(gptOverallScore, claudeOverallScore);

// Determine which LLM scored higher overall
const gptTotalScore = metrics.reduce((sum, metric) => sum + gptScores[metric], 0);
const claudeTotalScore = metrics.reduce((sum, metric) => sum + claudeScores[metric], 0);
const higherScoringLLM = gptTotalScore > claudeTotalScore ? 'GPT-3.5' : 
                        claudeTotalScore > gptTotalScore ? 'Claude-3.5' : 'Tie';

// Create GPT Database Entry
const gptDatabaseData = {
  sessionId: originalData.sessionId,
  timestamp: originalData.timestamp,
  userId: originalData.userId || 'anonymous',
  duration: originalData.duration || 0,
  messageCount: originalData.messageCount || 0,
  userMessageCount: originalData.userMessageCount || 0,
  assistantMessageCount: originalData.assistantMessageCount || 0,
  model: 'GPT-3.5-turbo',
  evaluator: 'GPT-3.5-turbo',
  helpfulness: gptScores.helpfulness,
  accuracy: gptScores.accuracy,
  clarity: gptScores.clarity,
  relevance: gptScores.relevance,
  tone: gptScores.tone,
  completeness: gptScores.completeness,
  overall_score: gptOverallScore,
  helpfulness_reason: extractReason(gptResults, 'helpfulness'),
  accuracy_reason: extractReason(gptResults, 'accuracy'),
  clarity_reason: extractReason(gptResults, 'clarity'),
  relevance_reason: extractReason(gptResults, 'relevance'),
  tone_reason: extractReason(gptResults, 'tone'),
  completeness_reason: extractReason(gptResults, 'completeness'),
  key_insights: extractStringField(gptResults, 'key_insights'),
  improvement_suggestions: extractStringField(gptResults, 'improvement_suggestions'),
  conversation_summary: extractStringField(gptResults, 'conversation_summary'),
  compared_against: 'Claude-3.5-Sonnet',
  overall_agreement: overallAgreementRate + '%',
  avg_score_difference: averageDifference,
  higher_scoring: higherScoringLLM === 'GPT-3.5' ? 'This Model' : 
                  higherScoringLLM === 'Claude-3.5' ? 'Competitor' : 'Tie',
  helpfulness_vs_claude: comparisons.helpfulness.difference,
  accuracy_vs_claude: comparisons.accuracy.difference,
  clarity_vs_claude: comparisons.clarity.difference,
  relevance_vs_claude: comparisons.relevance.difference,
  tone_vs_claude: comparisons.tone.difference,
  completeness_vs_claude: comparisons.completeness.difference,
  helpfulness_agreement: comparisons.helpfulness.agreement,
  accuracy_agreement: comparisons.accuracy.agreement,
  clarity_agreement: comparisons.clarity.agreement,
  relevance_agreement: comparisons.relevance.agreement,
  tone_agreement: comparisons.tone.agreement,
  completeness_agreement: comparisons.completeness.agreement
};

// Create Claude Database Entry
const claudeDatabaseData = {
  sessionId: originalData.sessionId,
  timestamp: originalData.timestamp,
  userId: originalData.userId || 'anonymous',
  duration: originalData.duration || 0,
  messageCount: originalData.messageCount || 0,
  userMessageCount: originalData.userMessageCount || 0,
  assistantMessageCount: originalData.assistantMessageCount || 0,
  model: 'Claude-3.5-Sonnet',
  evaluator: 'Claude-3.5-Sonnet',
  helpfulness: claudeScores.helpfulness,
  accuracy: claudeScores.accuracy,
  clarity: claudeScores.clarity,
  relevance: claudeScores.relevance,
  tone: claudeScores.tone,
  completeness: claudeScores.completeness,
  overall_score: claudeOverallScore,
  helpfulness_reason: extractReason(claudeResults, 'helpfulness'),
  accuracy_reason: extractReason(claudeResults, 'accuracy'),
  clarity_reason: extractReason(claudeResults, 'clarity'),
  relevance_reason: extractReason(claudeResults, 'relevance'),
  tone_reason: extractReason(claudeResults, 'tone'),
  completeness_reason: extractReason(claudeResults, 'completeness'),
  key_insights: extractStringField(claudeResults, 'key_insights'),
  improvement_suggestions: extractStringField(claudeResults, 'improvement_suggestions'),
  conversation_summary: extractStringField(claudeResults, 'conversation_summary'),
  compared_against: 'GPT-3.5-turbo',
  overall_agreement: overallAgreementRate + '%',
  avg_score_difference: averageDifference,
  higher_scoring: higherScoringLLM === 'Claude-3.5' ? 'This Model' : 
                  higherScoringLLM === 'GPT-3.5' ? 'Competitor' : 'Tie',
  helpfulness_vs_gpt: comparisons.helpfulness.difference,
  accuracy_vs_gpt: comparisons.accuracy.difference,
  clarity_vs_gpt: comparisons.clarity.difference,
  relevance_vs_gpt: comparisons.relevance.difference,
  tone_vs_gpt: comparisons.tone.difference,
  completeness_vs_gpt: comparisons.completeness.difference,
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
console.log('Agreement Rate:', overallAgreementRate + '%');
console.log('Average Difference:', averageDifference);
console.log('GPT Database Data Keys:', Object.keys(gptDatabaseData));
console.log('Claude Database Data Keys:', Object.keys(claudeDatabaseData));

// Return both datasets for separate Notion databases
return [
  { json: gptDatabaseData, pairedItem: 0 },
  { json: claudeDatabaseData, pairedItem: 1 }
]; 