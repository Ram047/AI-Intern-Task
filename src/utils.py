import cv2
import numpy as np
import mediapipe as mp
import math

# -------- Angle Calculation --------
def calculate_angle(a, b, c):
    """
    Calculates angle at point b formed by a-b-c.
    a, b, c are (x, y) tuples.
    """
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    ba = a - b
    bc = c - b

    cosine = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc) + 1e-6)
    angle = np.degrees(np.arccos(np.clip(cosine, -1.0, 1.0)))
    return angle


# -------- Smoothing (simple moving average) --------
def smooth_keypoints(buffer, new_point, max_len=5):
    buffer.append(new_point)
    if len(buffer) > max_len:
        buffer.pop(0)
    return np.mean(buffer, axis=0)
