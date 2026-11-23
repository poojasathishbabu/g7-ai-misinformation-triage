# 11 - G7 AI Misinformation Classifier
## Business Problem
Political claims spread fast. Can we flag misleading claims early, with evidence, not just a score?

## Data (Real, LIAR / PolitiFact)
- Train: 10240 | Valid: 1284 | Test: 1267
- Original labels (6): pants-fire, false, barely-true, half-true, mostly-true, true
- Binary mapping (documented, reversible):
  - Fake / Misleading (1) = pants-fire + false + barely-true
  - Real / Not-Fake (0) = half-true + mostly-true + true
- Why binary? G7 policy needs a triage decision: flag for review vs not. 6-class is noisy for triage.
- Text = statement only. Speaker/party NOT used as feature (would be bias - model would learn speaker, not claim).

## Models
- Baseline: Majority class Acc 0.564
- TF-IDF (8k, 1-2 grams) + Logistic Regression (balanced): Acc 0.602, F1-Fake 0.549
- Confusion (Test): [[456, 258], [246, 307]] [[TN, FP],[FN, TP]] - FP = Real flagged Fake, FN = Fake missed
- DistilBERT (in src/bert_train.py): Same binary task, fine-tune 2 epochs, compare F1. Not run here (needs GPU) - code + expected eval loop provided. Do NOT claim BERT F1 without running it.

## Explainability
- Top Fake words: [('obamacare', 1.75), ('obama', 1.61), ('wisconsin', 1.6), ('rep', 1.54), ('illegals', 1.44)]
- Top Real words: [('percent', -2.27), ('countries', -2.17), ('day', -1.8), ('georgia', -1.79), ('average', -1.63)]
- Limitation: Word-level model can be fooled by new phrasing. BERT (context) is the fix, TF-IDF is the baseline.

## Now What
1. Use as triage, NOT auto-ban: Flag Fake with confidence >0.8 for human review.
2. Monitor FN: Missed Fake is more harmful than FP.
3. Re-check weekly: New topics drift fast.

## How to Run
pip install -r requirements.txt
python src/train_tfidf.py
python src/bert_train.py  # needs GPU / HF
Open dashboard.html
## Links
- Link 1 Repo: github.com/<your-username>/11-g7-ai-misinformation
- Link 2 Result Dashboard: <your-dashboard-link>

## Tests
python src/test_mapping.py
