"""Classical (non deep-learning) damage detector used to build the mask for real photos.

Thin bright/dark structures (scratches, dust) differ strongly from their median-filtered
version, ordinary edges do not.  It is a heuristic: use the sensitivity slider, or supply a
manual mask / rectangle for large missing areas.
"""
import cv2
import numpy as np


def detect_damage(bgr, sensitivity=0.5, dilate=2, max_coverage=0.12):
    """Return uint8 mask (1 = damaged) of the same HxW as `bgr` (uint8)."""
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    med = cv2.medianBlur(gray, 7)
    diff = cv2.absdiff(gray, med)
    thr = int(np.interp(sensitivity, [0, 1], [70, 20]))
    while True:
        m = (diff > thr).astype(np.uint8)
        if m.mean() <= max_coverage or thr > 200:
            break
        thr += 10
    n, lab, stats, _ = cv2.connectedComponentsWithStats(m, connectivity=8)
    big = np.zeros(n, np.uint8)
    big[1:] = stats[1:, cv2.CC_STAT_AREA] >= 3          # drop isolated single-pixel noise
    keep = big[lab]
    if dilate > 0:
        keep = cv2.dilate(keep, np.ones((2 * dilate + 1, 2 * dilate + 1), np.uint8))
    return keep
