<div align="center">
  <h1>PhotoRestore</h1>
  <h3>Old Photo Damage Detection and Restoration Using Deep Learning</h3>
  <p>
    <img alt="Status" src="https://img.shields.io/badge/Status-Deployment%20Ready-success" />
    <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-blue" />
    <img alt="TensorFlow" src="https://img.shields.io/badge/TensorFlow-Keras-orange" />
    <img alt="UI" src="https://img.shields.io/badge/UI-Streamlit-FF4B4B" />
  </p>
</div>

<div align="center" style="background: linear-gradient(135deg, #0f172a, #1e3a8a, #0ea5e9); color: white; padding: 20px 18px; border-radius: 18px; margin: 18px 0;">
  <p style="font-size: 1.1rem; margin: 0; font-weight: 600;">Detect damaged regions • Restore old photos • Deploy on Streamlit Community Cloud</p>
</div>

## Overview
PhotoRestore is a lightweight deep-learning application for detecting and restoring damaged old photographs. It combines automatic damage detection with a U-Net-based restoration pipeline to repair scratches, stains, small missing areas, and broken regions while preserving the original image content outside the damaged mask.

The project is intentionally kept minimal and deployment-friendly so it can run on Streamlit Community Cloud or any similar hosting platform.

## Features
- Upload old or damaged images from the browser
- Automatically detect scratches, stains, and damaged regions
- Restore only the broken areas while preserving untouched pixels
- Use a trained U-Net model for reconstruction when available
- Provide a safe OpenCV fallback for lightweight repair
- Side-by-side before/after comparison in the app
- Download the repaired image as a PNG file

## Tech stack
- Python 3.10+
- TensorFlow / Keras
- U-Net CNN
- OpenCV
- NumPy
- Pillow
- Streamlit

## Current project structure
```text
PhotoRestore/
├── app.py                     # Streamlit web app
├── config.py                  # project configuration
├── requirements.txt           # Python dependencies
├── README.md                  # project documentation
├── .gitignore                 # git ignore rules
├── src/
│   ├── __init__.py
│   ├── detect.py              # damage detection
│   ├── enhance.py             # enhancement / post-processing
│   ├── restore.py             # repair pipeline
│   └── __init__.py
├── models/
│   └── photorevive_unet.keras # trained model checkpoint
├── data/                      # image dataset folder
│   └── clean/
├── outputs/                   # output artifacts
└── __pycache__/               # local cache
```

## Installation
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run locally
```bash
streamlit run app.py
```

## Run with custom host/port
```bash
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

## Streamlit Community Cloud deployment
This repository is organized for deployment on Streamlit Community Cloud:

1. Push the repository to GitHub
2. Connect the repo to Streamlit Community Cloud
3. Set the app entry file to `app.py`
4. Install dependencies from `requirements.txt`
5. The app will load the model from `models/photorevive_unet.keras`

## Model behavior
The app does the following:
- detects damaged areas
- creates a repair mask
- reconstructs the damaged pixels using the trained model
- keeps the original non-damaged areas unchanged
- improves brightness and visual clarity after restoration

## Expected output
After uploading an old photograph, the app displays:
- original photo
- detected damage mask
- restored photo
- before/after comparison
- downloadable repaired image

## Notes
- This project is optimized for practical old-photo restoration, not perfect historical reconstruction.
- Performance improves with a larger training dataset and GPU training.
- The app is designed to be simple, compact, and deployable for web use.

## License
Educational and research-oriented use.
