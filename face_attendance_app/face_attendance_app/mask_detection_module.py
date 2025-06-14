"""Placeholder mask detection using a TensorFlow model."""

import tensorflow as tf
import numpy as np
from PIL import Image

MODEL = None


def load_model(path: str):
    global MODEL
    MODEL = tf.keras.models.load_model(path)


def detect_mask(image_bytes: bytes) -> bool:
    """Return True if a mask is detected on the face."""
    if MODEL is None:
        return True
    img = Image.open(image_bytes).resize((224, 224))
    img = np.array(img) / 255.0
    preds = MODEL.predict(img.reshape(1, 224, 224, 3))
    return bool(preds[0] > 0.5)
