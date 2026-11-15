"""NLP Sentiment Analysis and Emotion Categorization Engine.

Implements rule-based and lexicon sentiment scoring with negation handling,
intensifiers, and emotional categorization for student mental wellness tracking.
"""

import math
import re
from typing import Dict, Any, List

# Core sentiment lexicon with valence ratings (-4.0 to +4.0)
VALENCE_LEXICON = {
    # Positive
    "happy": 3.0, "joy": 3.5, "great": 3.1, "peaceful": 2.8, "relaxed": 2.9,
    "excited": 3.2, "accomplished": 3.0, "proud": 2.9, "wonderful": 3.4,
    "good": 2.0, "calm": 2.5, "productive": 2.7, "confident": 2.8, "success": 3.2,
    "recharged": 2.6, "fun": 2.8, "love": 3.2, "hopeful": 2.4, "motivated": 2.9,
    
    # Negative
    "sad": -2.8, "tired": -2.0, "exhausted": -3.0, "anxious": -2.9, "stressed": -2.8,
    "overwhelmed": -3.1, "angry": -3.2, "frustrated": -2.7, "annoyed": -2.4,
    "worried": -2.6, "hopeless": -3.5, "depressed": -3.6, "bad": -2.2, "drained": -2.8,
    "failed": -3.2, "fog": -1.8, "burnout": -3.4, "nervous": -2.3, "lonely": -2.9
}

NEGATION_TOKENS = {"not", "never", "no", "cannot", "hardly", "barely", "neither", "scarcely"}
INTENSIFIERS = {"very": 1.4, "really": 1.3, "extremely": 1.6, "deeply": 1.4, "so": 1.25}


def clean_text(text: str) -> List[str]:
    """Tokenizes text and strips punctuation."""
    cleaned = re.sub(r"[^\w\s]", " ", text.lower())
    return [t.strip() for t in cleaned.split() if t.strip()]


def analyze_sentiment(text: str) -> Dict[str, Any]:
    """Evaluates text sentiment, compound polarity score, and primary emotion."""
    tokens = clean_text(text)
    if not tokens:
        return {
            "compound": 0.0,
            "sentiment_label": "Neutral",
            "pos": 0.0,
            "neu": 1.0,
            "neg": 0.0,
            "primary_emotion": "Neutral",
            "wellness_advice": "Log a detailed reflection to receive personalized wellness guidance."
        }

    valence_sum = 0.0
    pos_count = 0
    neg_count = 0

    for i, token in enumerate(tokens):
        if token in VALENCE_LEXICON:
            val = VALENCE_LEXICON[token]

            # Check for intensifier directly preceding
            if i > 0 and tokens[i - 1] in INTENSIFIERS:
                val *= INTENSIFIERS[tokens[i - 1]]

            # Check for negation in 2 preceding tokens
            is_negated = any(tokens[j] in NEGATION_TOKENS for j in range(max(0, i - 2), i))
            if is_negated:
                val *= -0.75

            valence_sum += val
            if val > 0:
                pos_count += 1
            elif val < 0:
                neg_count += 1

    # Standard VADER-style normalization formula: x / sqrt(x^2 + 15)
    alpha = 15.0
    compound = valence_sum / math.sqrt((valence_sum ** 2) + alpha)
    compound = round(max(-1.0, min(1.0, compound)), 3)

    total_matched = pos_count + neg_count + 1
    pos_ratio = round(pos_count / total_matched, 2)
    neg_ratio = round(neg_count / total_matched, 2)
    neu_ratio = round(max(0.0, 1.0 - (pos_ratio + neg_ratio)), 2)

    # Classify Primary Emotion and Status
    if compound >= 0.45:
        sentiment_label = "Positive"
        primary_emotion = "Joyful / Accomplished"
        wellness_advice = "🌟 Keep this positive momentum! Write down 3 specific things that contributed to today's success."
    elif compound >= 0.10:
        sentiment_label = "Positive"
        primary_emotion = "Calm / Content"
        wellness_advice = "🌿 Steady state. A 10-minute quiet evening walk will help preserve your mental clarity."
    elif compound > -0.15:
        sentiment_label = "Neutral"
        primary_emotion = "Balanced / Reflective"
        wellness_advice = "📖 Good balance today. Ensure you disconnect from screens at least 30 minutes before sleep."
    elif compound > -0.50:
        sentiment_label = "Negative"
        primary_emotion = "Stressed / Fatigued"
        wellness_advice = "☕ Academic load is heavy. Practice 5 minutes of 4-7-8 breathing and tackle one small task at a time."
    else:
        sentiment_label = "Negative"
        primary_emotion = "Anxious / Overwhelmed"
        wellness_advice = "💙 Be gentle with yourself. Step away from study desks, speak to a friend, or take a restorative rest break."

    return {
        "compound": compound,
        "sentiment_label": sentiment_label,
        "pos": pos_ratio,
        "neu": neu_ratio,
        "neg": neg_ratio,
        "primary_emotion": primary_emotion,
        "wellness_advice": wellness_advice
    }
