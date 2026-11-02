<div align="center">
  <h1>PhotoRestore</h1>
  <h3>Old Photo Damage Detection and Restoration Using Deep Learning</h3>
  <p>
    <img alt="Status" src="https://img.shields.io/badge/Status-Production%20Ready-success" />
    <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-blue" />
    <img alt="TensorFlow" src="https://img.shields.io/badge/TensorFlow-Keras-orange" />
    <img alt="UI" src="https://img.shields.io/badge/UI-Streamlit-FF4B4B" />
  </p>
</div>

<div align="center" style="background: linear-gradient(135deg, #171c2d, #2a3f6f, #0a7cff); color: white; padding: 24px 18px; border-radius: 18px; box-shadow: 0 12px 30px rgba(30, 96, 255, 0.35); margin: 20px 0;">
  <p style="font-size: 1.15rem; margin: 0; font-weight: 600;">Detect damaged regions • Restore scratched and broken areas • Recover the best possible image quality</p>
</div>

## Overview
PhotoRestore is a lightweight deep-learning application for detecting and restoring damaged old photographs. The system combines automatic damage detection with a U-Net restoration model to recover scratches, stains, faded spots, and small missing regions while preserving the original content outside the damaged area.

The project is intentionally kept simple and deployment-friendly so it can be trained and launched quickly on a local machine or a cloud deployment environment.

## Why this project matters
Old photos often suffer from:
- scratches and line marks
- dust and stain artifacts
- faded colors and low contrast
- missing or broken regions

Manual restoration is time-consuming and requires expert editing. PhotoRestore gives users a practical upload-and-repair workflow that detects damaged areas and restores them with a deep-learning model.

## Core idea
The system combines two important steps:
- damage detection: identifies damaged regions in the image
- restoration: reconstructs the damaged area using a U-Net CNN

The model is trained on paired data:
- clean image
- damaged version of the same image
- model learns to restore the original structure and texture from the damaged input

This gives the project a strong image-to-image restoration capability while remaining manageable to train and deploy.

## Key features
- Upload old photographs directly in the app
- Automatic damage detection for scratches and small defects
- Region-based repair for selected damaged areas
- U-Net restoration pipeline with OpenCV fallback
- Best-effort recovery of damaged pixels while preserving original image content
- Before/after comparison in the UI
- Download restored output as a PNG image
- Simple project structure for local use and deployment

## Tech stack
- Python 3.10+
- TensorFlow / Keras
- U-Net CNN
- OpenCV
- NumPy
- Pillow
- Streamlit
- scikit-image

## Project architecture
```text
PhotoRestore/
├── app.py                  # Streamlit web app
├── train.py                # training script
├── make_demo_dataset.py    # demo dataset generator
├── config.py               # central project config
├── requirements.txt        # Python dependencies
├── src/
│   ├── damage.py            # synthetic photo damage generation
│   ├── detect.py           # scratch / damage mask detection
│   ├── data.py             # tf.data dataset pipeline
│   ├── enhance.py          # brightness / contrast enhancement
│   ├── losses.py           # training loss function
│   ├── restore.py          # repair pipeline
│   ├── unet.py             # U-Net model definition
│   └── __init__.py
├── tests/
│   └── smoke_test.py       # sanity checks
├── data/
│   └── clean/              # clean training images
├── models/
│   └── photorevive_unet.keras
├── .streamlit/
│   └── config.toml        # deployment config
├── Dockerfile              # container deployment
├── Procfile                # hosting deployment entrypoint
└── README.md
```

## Quick start
```bash
# 1) Create the environment
python -m venv .venv
source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Sanity check the project
python tests/smoke_test.py

# 4) Generate a small demo dataset
python make_demo_dataset.py

# 5) Train the model
python train.py --epochs 30 --batch 8

# 6) Launch the app locally
streamlit run app.py
```

## Training workflow
1. Put clean image data in `data/clean/`
2. Generate damaged/clean paired samples using the synthetic damage pipeline
3. Train the U-Net model in `train.py`
4. Save the best model in `models/photorevive_unet.keras`
5. Load the model in the app to restore new photos

## Deployment-ready setup
This project is prepared for deployment in a simple cloud or container environment.

### Local deployment using Streamlit
```bash
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

### Docker deployment
```bash
docker build -t photorevive .
docker run -p 8501:8501 photorevive
```

### Platform deployment
The repository includes:
- `Dockerfile` for container hosting
- `Procfile` for app-platform deployment
- `.streamlit/config.toml` for production-friendly Streamlit settings

## Expected result
After uploading an old photograph, the app will:
- detect scratches and damaged regions
- reconstruct those regions with the trained model
- preserve the untouched areas of the image
- generate a cleaner, more legible restored version
- display before/after restoration
- allow the user to download the repaired photo

## Example use case
A user uploads a faded, scratched family photo. The model identifies the damaged mask, restores the broken regions, and recovers the most realistic possible version of the photograph while keeping the original structure intact.

## Notes
- This project is designed for practical old-photo repair: damage detection + restoration in one workflow.
- For best quality, train on many clean photos and use a GPU environment such as Google Colab.
- This is a restoration model for plausible photo repair, not a perfect historical reconstruction system.

## License
This project is intended for educational and research-oriented photograph restoration work.
