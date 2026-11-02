"""Central configuration for PhotoRevive."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data" / "clean"
MODEL_DIR = ROOT / "models"
MODEL_PATH = MODEL_DIR / "photorevive_unet.keras"
COLOR_DIR = MODEL_DIR / "colorization"
OUTPUT_DIR = ROOT / "outputs"

PATCH_SIZE = 256          # training crop size
MAX_INFER_SIDE = 1024     # larger uploads are downscaled to this (longest side)
IMG_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff", ".webp"}

for _d in (MODEL_DIR, COLOR_DIR, OUTPUT_DIR, DATA_DIR):
    _d.mkdir(parents=True, exist_ok=True)
