"""PhotoRevive Streamlit app."""
import io

import cv2
import numpy as np
import streamlit as st
from PIL import Image, ImageOps

from src.restore import RestoreOptions, Restorer

st.set_page_config(page_title="PhotoRevive", page_icon="🖼️", layout="wide")


@st.cache_resource(show_spinner="Loading model...")
def get_restorer():
    return Restorer()


def read_upload(f):
    img = ImageOps.exif_transpose(Image.open(f)).convert("RGB")
    return np.array(img)[:, :, ::-1].copy()


def to_pil(bgr):
    return Image.fromarray(cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB))


restorer = get_restorer()

st.title("🖼️ PhotoRevive")
st.caption("Old photograph restoration using a CNN-based U-Net model")

with st.sidebar:
    st.header("Settings")
    if restorer.has_model:
        st.success("Trained U-Net loaded")
    else:
        st.warning("No trained U-Net found. Using OpenCV fallback for now.")

    st.subheader("Damage detection")
    remove = st.checkbox("Auto-detect scratches and spots", True)
    sens = st.slider("Sensitivity", 0.0, 1.0, 0.5, 0.05)
    strength = st.slider("Repair strength", 0.0, 1.0, 0.6, 0.05)

    st.subheader("Missing region")
    use_region = st.checkbox("Restore a selected region")
    rx = st.slider("Left %", 0, 100, 30) / 100
    ry = st.slider("Top %", 0, 100, 30) / 100
    rw = st.slider("Width %", 1, 100, 20) / 100
    rh = st.slider("Height %", 1, 100, 20) / 100
    mask_file = st.file_uploader("Or upload a repair mask", type=["png", "jpg", "jpeg"])

up = st.file_uploader("Upload an old photograph", type=["jpg", "jpeg", "png"])
if not up:
    st.info("Upload a JPG or PNG image to begin.")
    st.stop()

bgr = read_upload(up)
c1, c2 = st.columns(2)
c1.subheader("Original")
prev = bgr.copy()
if use_region:
    h, w = prev.shape[:2]
    cv2.rectangle(prev, (int(rx * w), int(ry * h)),
                  (int(min(rx + rw, 1) * w), int(min(ry + rh, 1) * h)), (0, 0, 255), max(2, w // 200))
c1.image(to_pil(prev), use_container_width=True)

if c2.button("✨ Restore Photograph", type="primary", use_container_width=True):
    manual = None
    if mask_file is not None:
        manual = (np.array(Image.open(mask_file).convert("L")) > 127).astype(np.uint8)

    opts = RestoreOptions(
        remove_damage=remove,
        sensitivity=sens,
        manual_mask=manual,
        region=(rx, ry, rw, rh) if use_region else None,
        model_strength=strength,
    )
    with st.spinner("Restoring image..."):
        st.session_state["result"] = restorer.restore(bgr, opts)

res = st.session_state.get("result")
if res:
    st.divider()
    st.subheader("Result")
    if not res["used_unet"]:
        st.caption("⚠️ Restored using the OpenCV fallback because no trained U-Net model was found.")

    t1, t2, t3 = st.tabs(["Before / After", "Side by side", "Detected damage mask"])
    before, after = to_pil(res["input"]), to_pil(res["restored"])

    with t1:
        try:
            from streamlit_image_comparison import image_comparison
            image_comparison(img1=before, img2=after, label1="Original", label2="Restored",
                             width=800, in_memory=True)
        except Exception:
            st.image([before, after], caption=["Original", "Restored"], use_container_width=True)

    with t2:
        a, b = st.columns(2)
        a.image(before, caption="Original", use_container_width=True)
        b.image(after, caption="Restored", use_container_width=True)

    with t3:
        st.image(res["mask"], caption="White regions were repaired", use_container_width=True)

    buf = io.BytesIO()
    after.save(buf, format="PNG")
    st.download_button("⬇️ Download Restored Image", buf.getvalue(), "restored.png", "image/png")
