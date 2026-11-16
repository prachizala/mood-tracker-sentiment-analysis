# MindPulse: Mood Tracker & Sentiment Analysis

[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Unit Tests](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](tests/)

An interactive natural language processing (NLP) dashboard and student emotional health tracker. It evaluates reflective journal entries, computes compound sentiment polarity using valence lexicons with negation and intensifier handling, and visualizes 60-day emotional wellness trajectories.

---

## 📌 Features

- **Rule-Based NLP Sentiment Engine**: Evaluates journal entries using a balanced valence lexicon (-4.0 to +4.0 scale).
- **Negation & Intensifier Support**: Inverts polarity for phrases like *"not happy"* (-0.75x) and boosts weights for intensifiers like *"extremely"* (1.6x) and *"very"* (1.4x).
- **VADER-Style Polarity Normalization**: Normalizes scores into a bounded continuous spectrum between `[-1.0, +1.0]` using:
  $$\text{Compound} = \frac{x}{\sqrt{x^2 + 15}}$$
- **Categorization & Guidance**: Automatically classifies reflections into *Joyful/Accomplished*, *Calm/Content*, *Balanced*, *Stressed/Fatigued*, and *Anxious/Overwhelmed*, offering actionable wellness advice.
- **Interactive 60-Day Trajectory**: Rolling 7-day mood moving averages and emotion distribution charts built with Streamlit and Pandas.
- **Historical Journal Log**: Filter and inspect prior reflections with tags, sentiment scores, and self-reported ratings.
- **CSV Reflection Export**: Built-in 1-click export button (`st.download_button`) allowing users to download their complete 60-day reflection log with timestamps, mood ratings, and NLP polarity metrics.

---

## 🏗️ System Architecture

```text
+-----------------------+
|  User Journal Entry   |  -->  "Finished building our dashboard! Feeling very happy."
+-----------+-----------+
            |
            v
+-----------------------+
|   NLP Sentiment       |  1. Regex Tokenization & Cleaning
|       Engine          |  2. Valence Lexicon Scoring
|                       |  3. Intensifier Multiplier & Negation Inversion
+-----------+-----------+  4. Continuous Formula Normalization: [-1.0, +1.0]
            |
            v
+-----------------------+
|  Streamlit Dashboard  |  -->  Compound Polarity Metric (+0.762)
|   & Trajectory UI     |  -->  Emotion: Joyful / Accomplished
+-----------------------+  -->  60-Day Rolling Moving Average Trendlines
```

---

## 📂 Project Structure

```text
mood-tracker-sentiment-analysis/
├── app.py                      # Streamlit dashboard and visual analytics
├── sentiment_engine.py         # Lexicon scoring, negation handling, & normalization
├── generate_sample_data.py     # Synthesizes 60-day historical journal dataset
├── data/
│   └── mood_journal_sample_data.csv
├── tests/
│   └── test_sentiment.py       # Unit tests (tokenization, negations, intensifiers)
├── requirements.txt            # Project dependencies
├── .gitignore
└── README.md
```

---

## 🚀 Quickstart Guide

### 1. Clone the Repository
```bash
git clone https://github.com/prachizala/mood-tracker-sentiment-analysis.git
cd mood-tracker-sentiment-analysis
```

### 2. Set Up Virtual Environment (Recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`.

---

## 🧪 Running Unit Tests

The test suite validates sentiment calculations, edge cases, and score boundaries using Python's built-in `unittest` framework:

```bash
python -m unittest discover -s tests
```

Expected output:
```text
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s

OK
```

---

## 👩‍💻 Author

**Prachi Zala**  
- Bachelor of Computer Applications (BCA) Student, Ahmedabad, Gujarat, India  
- GitHub: [@prachizala](https://github.com/prachizala)  
- Focus: Python, Data Analytics, and Applied Machine Learning
