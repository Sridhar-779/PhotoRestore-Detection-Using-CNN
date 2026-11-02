"""Classical enhancement: denoise, auto-levels, CLAHE contrast, unsharp sharpening."""
import cv2
import numpy as np


def enhance(bgr, contrast=1.5, sharpen=0.5, denoise=0.0, auto_levels=True):
    out = bgr.copy()
    if denoise > 0:
        out = cv2.fastNlMeansDenoisingColored(out, None, 10 * denoise, 10 * denoise, 7, 21)
    lab = cv2.cvtColor(out, cv2.COLOR_BGR2LAB)
    L = lab[:, :, 0]
    if auto_levels:
        lo, hi = np.percentile(L, (1, 99))
        if hi - lo > 10:
            L = np.clip((L.astype(np.float32) - lo) * 255.0 / (hi - lo), 0, 255).astype(np.uint8)
    if contrast > 0:
        L = cv2.createCLAHE(clipLimit=float(contrast), tileGridSize=(8, 8)).apply(L)
    lab[:, :, 0] = L
    out = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
    if sharpen > 0:
        blur = cv2.GaussianBlur(out, (0, 0), 1.5)
        out = cv2.addWeighted(out, 1 + sharpen, blur, -sharpen, 0)

    # Increase brightness slightly for old-photo restoration output without producing blue artifacts.
    out = cv2.convertScaleAbs(out, alpha=1.12, beta=16)
    return out
