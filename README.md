# Hotel Review Sentiment Analysis

This project is a **Streamlit web application** that performs **sentiment analysis** on customer reviews of hotels in **Greensboro, NC**. Users can select a hotel, give a star rating, enter a review, and get an instant prediction about whether the sentiment is **happy** or **not happy**.

---

##  Features

- Sentiment analysis using a trained Logistic Regression model (TF-IDF + NLP)
- Hotel selection from 10 Greensboro-based properties
- Star rating input (1–5)
- Natural language review input
- Sentiment prediction (happy or not happy)

---

## Tools

- **Python**
- **Streamlit**
- **scikit-learn**
- **NLTK** (for text preprocessing)
- **Joblib** (model serialization)
- **Pandas & NumPy**

---

##  Model Details

- **Algorithm**: Logistic Regression
- **Vectorizer**: TF-IDF with bi-grams (`ngram_range=(1,2)`)
- **Preprocessing**: Lowercasing, punctuation removal, lemmatization
- **Evaluation**:
  - Accuracy: 91%
  - F1 Score: 91%
  - AUC: 0.94

> Logistic Regression outperformed Naive Bayes and Random Forest on this dataset.

---
