import unittest
import sys
import os

# Add parent directory to path so sentiment_engine can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sentiment_engine import analyze_sentiment, clean_text


class TestSentimentEngine(unittest.TestCase):
    """Test suite for sentiment analysis, negation handling, and emotion labeling."""

    def test_clean_text_tokenization(self):
        text = "Hello, World! This is a test... with punctuation?!"
        tokens = clean_text(text)
        self.assertEqual(tokens, ["hello", "world", "this", "is", "a", "test", "with", "punctuation"])

    def test_positive_sentiment(self):
        text = "Today was a wonderful and productive day, feeling very happy and accomplished."
        res = analyze_sentiment(text)
        self.assertGreater(res["compound"], 0.4)
        self.assertEqual(res["sentiment_label"], "Positive")
        self.assertIn("Joyful", res["primary_emotion"])

    def test_negative_sentiment(self):
        text = "I feel so exhausted, anxious and overwhelmed by college exams."
        res = analyze_sentiment(text)
        self.assertLess(res["compound"], -0.3)
        self.assertEqual(res["sentiment_label"], "Negative")
        self.assertIn("Anxious / Overwhelmed", res["primary_emotion"])

    def test_negation_inversion(self):
        # "happy" is positive, but "not happy" should flip negative or neutral
        res_pos = analyze_sentiment("I am happy today.")
        res_negated = analyze_sentiment("I am not happy today.")
        self.assertGreater(res_pos["compound"], 0.0)
        self.assertLess(res_negated["compound"], res_pos["compound"])
        self.assertLess(res_negated["compound"], 0.0)

    def test_intensifier_scaling(self):
        res_normal = analyze_sentiment("I feel happy.")
        res_boosted = analyze_sentiment("I feel extremely happy.")
        self.assertGreater(res_boosted["compound"], res_normal["compound"])

    def test_empty_and_neutral_text(self):
        res_empty = analyze_sentiment("")
        self.assertEqual(res_empty["compound"], 0.0)
        self.assertEqual(res_empty["sentiment_label"], "Neutral")

        res_neutral = analyze_sentiment("I ate rice and vegetables for lunch.")
        self.assertAlmostEqual(res_neutral["compound"], 0.0, places=1)
        self.assertEqual(res_neutral["sentiment_label"], "Neutral")

    def test_score_boundary(self):
        extreme_pos = "happy joy great excited wonderful success calm productive motivated love fun"
        res_pos = analyze_sentiment(extreme_pos)
        self.assertLessEqual(res_pos["compound"], 1.0)
        self.assertGreaterEqual(res_pos["compound"], -1.0)

        extreme_neg = "sad tired exhausted anxious stressed overwhelmed angry hopeless depressed burnout"
        res_neg = analyze_sentiment(extreme_neg)
        self.assertLessEqual(res_neg["compound"], 1.0)
        self.assertGreaterEqual(res_neg["compound"], -1.0)


if __name__ == "__main__":
    unittest.main()
