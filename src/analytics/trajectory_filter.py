"""Exponential moving average (EMA) emotional trajectory smoothing filter."""


class MoodTrajectoryFilter:
    """Computes smoothed emotional trends from noisy daily journal scores."""

    @staticmethod
    def compute_exponential_moving_average(scores: list[float], alpha: float = 0.3) -> list[float]:
        """Calculates exponential moving average trajectory."""
        if not scores:
            return []

        smoothed = [scores[0]]
        for val in scores[1:]:
            prev = smoothed[-1]
            curr_ema = (alpha * val) + ((1.0 - alpha) * prev)
            smoothed.append(round(curr_ema, 3))
        return smoothed
