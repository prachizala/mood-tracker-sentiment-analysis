# Changes Log - Work Package 4: Small Feature Upgrades

## Summary of Changes

### 1. CSV Journal Export Button (`app.py`)
- Integrated `st.download_button` in Tab 3 ("📚 Historical Reflections Log") enabling users to download their 60-day journal history as `mood_journal_history.csv`.
- Configured with UTF-8 byte encoding and `text/csv` MIME type, exporting date, reflection text, self-reported mood rating, sentiment category, and compound polarity score.
- Positioned alongside sentiment category filters for intuitive user experience.

### 2. Documentation (`README.md`)
- Documented the CSV Reflection Export functionality under the Core Features section.

### 3. Automated Test Verification
- Executed unit test suite (`python -m unittest discover -s tests`).
- All 7 tests pass 100% (`Ran 7 tests in 0.001s ... OK`).

## Items Skipped & Rationale
- None.

## Manual Steps Needed
- None. To test the export, launch `streamlit run app.py`, navigate to Tab 3, and click "📥 Download Journal History (CSV)".
