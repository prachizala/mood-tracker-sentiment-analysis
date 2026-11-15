"""Mood Tracker with Sentiment Analysis - Streamlit Web Dashboard.

Provides natural language sentiment scoring, emotional trajectory trendlines,
and personalized cognitive wellness recommendations.
"""

import os
import streamlit as st
import pandas as pd
from datetime import date

from sentiment_engine import analyze_sentiment

st.set_page_config(
    page_title="Mood Tracker & Sentiment Analysis",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "mood_journal_sample_data.csv")

st.markdown("""
<style>
    .main-title { font-size: 2.2rem; font-weight: 700; color: #4338CA; margin-bottom: 0.2rem; }
    .sub-title { font-size: 1.05rem; color: #4B5563; margin-bottom: 1.5rem; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🧠 MindPulse: Mood Tracker & Sentiment NLP</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Natural Language Emotional Polarity Tracking & Trajectory Analytics | Built by Prachi Zala</div>', unsafe_allow_html=True)

with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/brain.png", width=120)
    st.subheader("⚙️ Analysis Settings")
    st.info("Uses VADER-normalized valence scoring with negation and intensifier support.")
    st.markdown("---")
    st.markdown("### 👩‍💻 Developer")
    st.markdown("**Prachi Zala**  \nBCA Student, Ahmedabad  \n[GitHub Profile](https://github.com/prachizala)")

tab1, tab2, tab3 = st.tabs([
    "✍️ Daily Journal Sentiment Analyzer",
    "📈 60-Day Emotional Trajectory",
    "📚 Historical Reflections Log"
])

# -----------------------------------------------------------------------------
# TAB 1: DAILY JOURNAL & SENTIMENT ANALYZER
# -----------------------------------------------------------------------------
with tab1:
    st.subheader("Write Today's Reflection")
    col_input, col_results = st.columns([1.2, 1])

    with col_input:
        user_text = st.text_area(
            "What's on your mind today? (Reflect on college, coding, or life):",
            height=140,
            value="Finished building the new machine learning dashboard today! Feeling very happy and accomplished with our project progress."
        )

        manual_rating = st.select_slider(
            "Self-Reported Mood Scale:",
            options=[1, 2, 3, 4, 5],
            value=5,
            format_func=lambda x: {1: "1 - Exhausted / Very Low", 2: "2 - Stressed / Low", 3: "3 - Neutral / Balanced", 4: "4 - Good / Calm", 5: "5 - Great / Energized"}[x]
        )

        analyze_btn = st.button("🚀 Analyze Sentiment & Log Entry", type="primary", use_container_width=True)

    with col_results:
        st.subheader("NLP Sentiment Breakdown")
        result = analyze_sentiment(user_text)

        m1, m2 = st.columns(2)
        m1.metric("Compound Polarity", f"{result['compound']:+.3f}")
        m2.metric("Primary Emotion", result["primary_emotion"])

        st.progress(float((result["compound"] + 1.0) / 2.0))
        st.caption(f"Polarity Spectrum: Negative (-1.0) to Positive (+1.0)")

        st.markdown(f"**Positivity:** `{result['pos']*100:.0f}%` | **Neutrality:** `{result['neu']*100:.0f}%` | **Negativity:** `{result['neg']*100:.0f}%`")

        if result["sentiment_label"] == "Positive":
            st.success(result["wellness_advice"])
        elif result["sentiment_label"] == "Neutral":
            st.info(result["wellness_advice"])
        else:
            st.warning(result["wellness_advice"])

# -----------------------------------------------------------------------------
# TAB 2: 60-DAY EMOTIONAL TRAJECTORY
# -----------------------------------------------------------------------------
with tab2:
    st.subheader("60-Day Sentiment & Polarity Trends")

    if os.path.exists(DATA_PATH):
        df_history = pd.read_csv(DATA_PATH)
        df_history["date"] = pd.to_datetime(df_history["date"])
        df_history = df_history.sort_values("date")

        # Rolling 7-day average
        df_history["7-Day Moving Avg"] = df_history["compound_score"].rolling(window=7, min_periods=1).mean()

        st.line_chart(df_history.set_index("date")[["compound_score", "7-Day Moving Avg"]])

        col_c1, col_c2 = st.columns(2)
        with col_c1:
            st.markdown("#### Sentiment Distribution")
            sentiment_counts = df_history["sentiment_label"].value_counts()
            st.bar_chart(sentiment_counts)

        with col_c2:
            st.markdown("#### Mood Rating vs Compound Polarity")
            st.scatter_chart(df_history, x="mood_rating", y="compound_score")
    else:
        st.info("Sample historical dataset not found.")

# -----------------------------------------------------------------------------
# TAB 3: HISTORICAL REFLECTIONS LOG
# -----------------------------------------------------------------------------
with tab3:
    st.subheader("Archived Journal Entries")
    if os.path.exists(DATA_PATH):
        df_log = pd.read_csv(DATA_PATH)
        filter_sent = st.selectbox("Filter by Sentiment Category:", ["All", "Positive", "Neutral", "Negative"])
        if filter_sent != "All":
            df_log = df_log[df_log["sentiment_label"] == filter_sent]

        st.dataframe(df_log[["date", "journal_text", "mood_rating", "sentiment_label", "compound_score"]], use_container_width=True)
