"""Placeholder for simple eye blink liveness detection."""

import cv2
import numpy as np


def detect_blink(frame) -> bool:
    """Dummy blink detection returning True for every other frame."""
    # In production, integrate real blink or motion detection.
    return True
