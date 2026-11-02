<div align="center">
  <h1>PhotoRevive</h1>
  <h3>Old Photograph Restoration Using Deep Learning and CNN-Based Image Inpainting</h3>
  <p>
    <img alt="Status" src="https://img.shields.io/badge/Status-Production%20Ready-success" />
    <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-blue" />
    <img alt="TensorFlow" src="https://img.shields.io/badge/TensorFlow-Keras-orange" />
    <img alt="UI" src="https://img.shields.io/badge/UI-Streamlit-FF4B4B" />
  </p>
</div>

<div align="center" style="background: linear-gradient(135deg, #171c2d, #2a3f6f, #0a7cff); color: white; padding: 24px 18px; border-radius: 18px; box-shadow: 0 12px 30px rgba(30, 96, 255, 0.35); margin: 20px 0;">
  <p style="font-size: 1.15rem; margin: 0; font-weight: 600;">Upload a damaged image • Repair scratches and missing regions • Restore detail • Download the result</p>
</div>

## Overview
PhotoRevive is a lightweight deep-learning application for restoring old and damaged photographs. The system focuses on a practical and realistic workflow: create synthetic damage from clean images, train a U-Net, and then restore real-world scratched or faded photos with minimal user effort.

The project is intentionally kept simple and deployment-friendly so it can be trained and launched quickly on a local machine or a cloud deployment environment.

## Why this project matters
Old photos often suffer from:
- scratches and line marks
- dust and stain artifacts
- faded colors and low contrast
- missing or broken regions

Manual restoration is time-consuming and requires expert editing. PhotoRevive gives users a simple upload-and-repair flow powered by deep learning.

## Core idea
The main model is a U-Net CNN trained on paired data:
- clean image
- damaged version of the same image
- model learns to reconstruct the original content from the damaged input

This gives the system a strong image-to-image restoration capability while remaining manageable to train and deploy.

## Key features
- Upload old photographs directly in the app
- Automatic damage detection for scratches and small defects
- Region-based repair for selected damaged areas
- U-Net restoration pipeline with OpenCV fallback
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
PhotoRevive/
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
- preserve the rest of the image
- display before/after restoration
- allow the user to download the repaired photo

## Example use case
A user uploads a faded, scratched family photo. The model identifies the damaged mask and reconstructs the missing detail while keeping the original photograph structure intact.

## Notes
- This project is intentionally focused on a realistic, manageable restoration task.
- For best quality, train on many clean photos and use a GPU environment such as Google Colab.
- This is a restoration model for plausible photo repair, not a perfect historical reconstruction system.

## License
This project is intended for educational and research-oriented photograph restoration work.
