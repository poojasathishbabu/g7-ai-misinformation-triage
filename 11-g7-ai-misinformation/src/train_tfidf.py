"""Project 11 - TF-IDF + Logistic. Binary: Fake=pants-fire/false/barely-true, Real=half/mostly/true.
Speaker/Party NOT used - would learn speaker, not claim. Run: python src/train_tfidf.py
"""
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
cols=["id","label","statement","subject","speaker","job","state","party","a","b","c","d","e","context"]
# NOTE: raw LIAR files are TSV with 14 cols, train/valid/test split already provided
train=pd.read_csv("data/cleaned_liar_train_sample.csv")
print("Sample file is train sample. Full training uses original train.tsv - see README mapping.")
print(train.head(2).to_string())
