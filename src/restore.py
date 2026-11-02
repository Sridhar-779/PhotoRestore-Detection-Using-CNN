"""Simplified U-Net restoration pipeline for the PhotoRevive app."""
from dataclasses import dataclass
from typing import Optional, Tuple

import cv2
import numpy as np

import config
from src.detect import detect_damage
from src.enhance import enhance


@dataclass
class RestoreOptions:
    remove_damage: bool = True
    sensitivity: float = 0.5
    manual_mask: Optional[np.ndarray] = None
    region: Optional[Tuple[float, float, float, float]] = None
    model_strength: float = 0.6
    do_enhance: bool = True
    contrast: float = 1.5
    sharpen: float = 0.5
    denoise: float = 0.0


class Restorer:
    def __init__(self, model_path=config.MODEL_PATH):
        self.model = None
        if model_path and model_path.exists():
            try:
                from tensorflow import keras
                self.model = keras.models.load_model(model_path, compile=False)
            except Exception as e:  # pragma: no cover
                print("Could not load U-Net:", e)

    @property
    def has_model(self):
        return self.model is not None

    @staticmethod
    def _fit(bgr, max_side=config.MAX_INFER_SIDE):
        h, w = bgr.shape[:2]
        s = max_side / max(h, w)
        if s < 1:
            bgr = cv2.resize(bgr, (int(w * s), int(h * s)), interpolation=cv2.INTER_AREA)
        return bgr

    def reconstruct(self, bgr, mask, model_strength=0.6):
        """Repair only the damaged pixels. Keep all non-damaged pixels exactly unchanged."""
        h, w = bgr.shape[:2]
        if not self.has_model:
            if mask.any():
                return cv2.inpaint(bgr, mask.astype(np.uint8), 3, cv2.INPAINT_TELEA)
            return bgr

        rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB).astype(np.float32) / 255.0
        ph, pw = (-h) % 16, (-w) % 16
        x = np.concatenate([rgb, mask[..., None].astype(np.float32)], -1)
        x = np.pad(x, ((0, ph), (0, pw), (0, 0)), mode="reflect")
        pred = self.model(x[None], training=False).numpy()[0][:h, :w]

        mask_f = mask.astype(np.float32)
        blend = mask_f[..., None]

        # Smooth blue-channel artifacts caused by damaged-region reconstruction.
        pred = pred.copy()
        blue = pred[..., 0]
        green = pred[..., 1]
        red = pred[..., 2]
        strong_blue = (blue > green + 0.12) | (blue > red + 0.12)
        if np.any(strong_blue):
            blue[strong_blue] = np.minimum(blue[strong_blue], np.maximum(green[strong_blue], red[strong_blue]) + 0.08)
            pred[..., 0] = blue

        # Preserve the original image outside the damaged area. Only the damaged pixels are filled.
        out = rgb * (1.0 - blend) + pred * blend
        out = np.clip(out, 0, 1)
        return cv2.cvtColor((out * 255).astype(np.uint8), cv2.COLOR_RGB2BGR)

    def restore(self, bgr, opts: RestoreOptions = None):
        opts = opts or RestoreOptions()
        img = self._fit(bgr)
        h, w = img.shape[:2]
        mask = np.zeros((h, w), np.uint8)

        if opts.remove_damage:
            mask |= detect_damage(img, opts.sensitivity)
        if opts.manual_mask is not None:
            m = cv2.resize(opts.manual_mask.astype(np.uint8), (w, h), interpolation=cv2.INTER_NEAREST)
            mask |= (m > 0).astype(np.uint8)
        if opts.region is not None:
            x, y, rw, rh = opts.region
            mask[int(y * h):int((y + rh) * h), int(x * w):int((x + rw) * w)] = 1

        out = self.reconstruct(img, mask, opts.model_strength)
        if opts.do_enhance:
            out = enhance(out, opts.contrast, opts.sharpen, opts.denoise)

        return {"input": img, "restored": out, "mask": mask * 255, "used_unet": self.has_model}
