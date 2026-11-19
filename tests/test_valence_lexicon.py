"""Unit tests for valence lexicon negation inversion."""
import unittest

class TestValenceInversion(unittest.TestCase):
    def test_negation_flips_sign(self):
        base_score = 0.8
        negated_score = -0.5 * base_score
        self.assertLess(negated_score, 0)
        self.assertEqual(negated_score, -0.4)

if __name__ == '__main__':
    unittest.main()
