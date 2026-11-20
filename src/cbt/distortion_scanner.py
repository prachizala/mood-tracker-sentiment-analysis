"""Cognitive Behavioral Therapy (CBT) distortion pattern scanner."""


class CognitiveDistortionScanner:
    """Scans reflection entries for cognitive bias markers (e.g. catastrophizing, all-or-nothing)."""

    DISTORTION_PATTERNS = {
        "ALL_OR_NOTHING": ["always", "never", "everyone", "nobody", "ruined completely"],
        "CATASTROPHIZING": ["disaster", "nightmare", "unbearable", "worst thing ever"],
        "SHOULD_STATEMENTS": ["must", "should", "ought to", "have to"],
    }

    @classmethod
    def scan_text(cls, reflection_text: str) -> list[str]:
        """Returns detected cognitive distortion types found within journal reflection."""
        lowered = reflection_text.lower()
        detected = []
        for distortion, markers in cls.DISTORTION_PATTERNS.items():
            if any(marker in lowered for marker in markers):
                detected.append(distortion)
        return detected
