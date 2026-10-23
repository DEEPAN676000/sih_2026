import { Complaint, OverlapPair } from '../types';

/**
 * AI-Assisted Cross-Bureau Overlap Detection Algorithm
 * Computes multi-factor similarity across complaints to spot redundant investigations:
 * 1. AICTE Permanent ID (Deterministic matching)
 * 2. Cross-Bureau condition (e.g. RB vs PGRC)
 * 3. Categorical & regulatory relation
 * 4. N-gram / Token Jaccard text similarity on description
 */
export function calculateSimilarityScore(caseA: Complaint, caseB: Complaint): {
  score: number;
  isOverlap: boolean;
  reasons: string[];
} {
  if (caseA.caseId === caseB.caseId) {
    return { score: 0, isOverlap: false, reasons: [] };
  }

  let score = 0;
  const reasons: string[] = [];

  // 1. AICTE Permanent ID Exact Match (High weight)
  if (caseA.aicteId && caseB.aicteId && caseA.aicteId === caseB.aicteId) {
    score += 55;
    reasons.push(`Identical AICTE Permanent ID: ${caseA.aicteId}`);
  }

  // 2. Cross-Bureau Condition: Regulation Bureau (RB) vs PGRC
  const bureaus = [caseA.assignedBureau, caseB.assignedBureau];
  const isCrossBureau =
    bureaus.includes('Regulation Bureau (RB)') &&
    bureaus.includes('Public Grievance Redressal Cell (PGRC)');
  
  if (isCrossBureau) {
    score += 25;
    reasons.push('Cross-Bureau Active Proceedings (Regulation Bureau & PGRC concurrently investigating)');
  }

  // 3. Category match or related regulatory violations
  if (caseA.category === caseB.category) {
    score += 15;
    reasons.push(`Identical Category: ${caseA.category}`);
  } else if (
    (caseA.category.includes('Pay Scale') && caseB.category.includes('Certificates')) ||
    (caseA.category.includes('Intake') && caseB.category.includes('Fee'))
  ) {
    score += 12;
    reasons.push(`Correlated Violations (${caseA.category} ⟷ ${caseB.category})`);
  }

  // 4. Text Token Jaccard Similarity on grievance description
  const tokenize = (text: string) =>
    new Set(
      text
        .toLowerCase()
        .replace(/[^a-z0-9 ]/g, '')
        .split(/\s+/)
        .filter((w) => w.length > 3)
    );

  const tokensA = tokenize(caseA.description);
  const tokensB = tokenize(caseB.description);

  let intersection = 0;
  tokensA.forEach((token) => {
    if (tokensB.has(token)) intersection++;
  });
  const union = tokensA.size + tokensB.size - intersection;
  const jaccard = union > 0 ? intersection / union : 0;

  if (jaccard > 0.15) {
    const textWeight = Math.min(25, Math.round(jaccard * 100));
    score += textWeight;
    reasons.push(`Grievance Narrative Similarity: ${Math.round(jaccard * 100)}% keyword overlap`);
  }

  return {
    score: Math.min(99, score),
    isOverlap: score >= 60,
    reasons
  };
}

export function detectAllOverlaps(complaints: Complaint[]): OverlapPair[] {
  const pairs: OverlapPair[] = [];
  const visited = new Set<string>();

  for (let i = 0; i < complaints.length; i++) {
    for (let j = i + 1; j < complaints.length; j++) {
      const caseA = complaints[i];
      const caseB = complaints[j];
      const pairKey = [caseA.caseId, caseB.caseId].sort().join('<->');

      if (!visited.has(pairKey)) {
        visited.add(pairKey);
        const sim = calculateSimilarityScore(caseA, caseB);
        if (sim.isOverlap) {
          const isLinked = (caseA.linkedCaseIds || []).includes(caseB.caseId);
          pairs.push({
            caseA,
            caseB,
            score: sim.score,
            reasons: sim.reasons,
            isLinked
          });
        }
      }
    }
  }
  return pairs;
}
