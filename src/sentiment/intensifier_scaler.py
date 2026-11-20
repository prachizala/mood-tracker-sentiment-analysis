"""Negation inversion and intensifier word scaling calculation module."""


class IntensifierScaler:
    """Adjusts valence polarity based on modifier tokens (e.g., 'extremely', 'scarcely')."""

    INTENSIFIERS = {
        "extremely": 1.6,
        "very": 1.4,
        "incredibly": 1.5,
        "barely": 0.4,
        "scarcely": 0.3,
        "slightly": 0.5,
    }

    NEGATION_WORDS = {"not", "never", "no", "hardly", "neither"}

    @classmethod
    def apply_modifiers(cls, base_score: float, context_tokens: list[str]) -> float:
        """Applies negation inversion (-0.75x) or intensifier multipliers to sentiment scores."""
        score = base_score
        for token in context_tokens:
            tok = token.lower()
            if tok in cls.NEGATION_WORDS:
                score *= -0.75
            elif tok in cls.INTENSIFIERS:
                score *= cls.INTENSIFIERS[tok]
        return max(-1.0, min(1.0, round(score, 3)))
