# Customer Support Chatbot: Evaluation Report (Simple Version)

## Executive Summary

This report checks whether Llama 3.2 3B can be used as an offline customer support chatbot for a fictional store, "Chic Boutique".
We compared two prompt styles:

- Zero-shot: instructions only
- One-shot: instructions plus one example

Main result: zero-shot performed better overall in this test.

## 1. Goal and Questions

### Goal

Build a privacy-safe chatbot that runs locally and avoids sending customer data to external APIs.

### Why this matters

Rules like GDPR, CCPA, and DPDP require careful handling of personal data.
Running the model locally with Ollama keeps data on company infrastructure.

### Questions asked

1. Can Llama 3.2 3B give relevant and clear support replies?
2. Is one-shot better than zero-shot?
3. Which query types are difficult?
4. What limits should we expect?

## 2. Method

### Data

We used 20 customer-style queries adapted from the Ubuntu Dialogue Corpus.
Example adaptation:

- Original technical query: "How do I check apache logs?"
- Adapted e-commerce query: "How do I track my shipping status?"

### Prompt styles

- Zero-shot: role + instructions + user query
- One-shot: same prompt, plus one example answer

### Scoring rubric (1 to 5)

- Relevance: does it answer the question?
- Coherence: is it clear and grammatically correct?
- Helpfulness: is it useful and actionable?

### Process

1. Generate zero-shot and one-shot replies for all 20 queries (40 total).
2. Score all replies on the 3 metrics.
3. Compare averages and analyze patterns.

## 3. Results

### Quantitative summary

| Prompting Method | Avg Relevance | Avg Coherence | Avg Helpfulness | Overall Avg |
|---|---|---|---|---|
| Zero-Shot | 4.4 | 4.75 | 3.8 | 4.32 |
| One-Shot | 3.9 | 4.75 | 3.6 | 4.08 |
| Difference (One-Shot - Zero-Shot) | -0.5 | 0.0 | -0.2 | -0.24 |

Key finding: zero-shot did better in relevance and helpfulness, while coherence was equal.

### Quality pattern

- Excellent (5/5): 23 responses (57.5%)
- Very good (4-4.5): 11 responses (27.5%)
- Adequate (3-3.5): 4 responses (10%)
- Poor (1-2.5): 2 responses (5%)

## 4. What worked and what failed

### Strengths

1. Language quality was strong in both methods (coherence 4.75).
2. Tone stayed polite and customer-friendly.
3. Process questions (password reset, payments, order history) were handled well.

### Weak points

1. No real-time data: promotions, stock, and live policy details were weak.
2. Inconsistent outputs: same question sometimes got conflicting answers.
3. Inventory and unknown policy questions scored low.

### Prompt behavior insight

The one-shot example was about return policy and had a cautious tone.
This may have pushed the model to be overly cautious in other policy questions too.

## 5. Example observations

1. Password reset query: both methods scored 5/5, but zero-shot was often more step-by-step.
2. Canada shipping query: zero-shot answered confidently; one-shot said it did not know.
3. Return policy query: both methods were vague because the model had no real policy source.
4. Promotions query: both methods could not provide real-time info.

## 6. Conclusion

Llama 3.2 3B is useful as a base chatbot for offline FAQ handling and first-level support.
It is not enough by itself for real-time or account-specific requests.

Best use cases:

- FAQ deflection
- simple process guidance
- first response before human handoff

Not enough for:

- live promotions and inventory
- account-specific transactions
- high-risk decisions without human review

## 7. Recommendations

### Immediate (1-2 weeks)

1. Test few-shot prompts (3-5 examples).
2. Add basic hallucination checks.
3. Add caching and logging.

### Short term (1-2 months)

1. Add knowledge base retrieval (RAG).
2. Add intent classification.
3. Add confidence scoring and escalation logic.

### Medium to long term

1. Fine-tune on domain data.
2. Try a hybrid multi-model setup.
3. Build a human-in-the-loop support pipeline.

## 8. Business summary

Cloud APIs can be expensive at scale and may raise privacy concerns.
Local LLM setup needs hardware up front but is much cheaper over time and keeps data local.

Suggested rollout:

1. Start with FAQ automation.
2. Add knowledge base and guardrails.
3. Escalate uncertain cases to humans.

## Appendix

Full response logs and score columns are in `eval/results.md`.

---

Report generated: March 16, 2026
Model: Llama 3.2 3B via Ollama (quantized)
Total responses: 40 (20 queries x 2 prompt styles)
Average response time: about 15-20 seconds per query
Top finding: zero-shot outperformed one-shot (4.32 vs 4.08)
