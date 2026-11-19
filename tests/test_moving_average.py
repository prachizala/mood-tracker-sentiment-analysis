"""Unit tests for moving average emotional trajectory."""
import unittest

class TestMovingAverage(unittest.TestCase):
    def test_simple_moving_average(self):
        window = [0.2, 0.4, 0.6, 0.8]
        sma = sum(window) / len(window)
        self.assertAlmostEqual(sma, 0.5, places=5)

if __name__ == '__main__':
    unittest.main()
