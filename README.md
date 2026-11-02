```markdown
<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=800&size=40&pause=1000&color=0EA5E9&center=true&vCenter=true&width=800&lines=PhotoRestore;Damage+Detection;Deep+Learning+Restoration" alt="Typing SVG" />
  
  <p>
    <img alt="Status" src="https://img.shields.io/badge/Status-Deployment%20Ready-success?style=for-the-badge&logo=appveyor" />
    <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" />
    <img alt="TensorFlow" src="https://img.shields.io/badge/TensorFlow-Keras-orange?style=for-the-badge&logo=tensorflow&logoColor=white" />
    <img alt="UI" src="https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  </p>
</div>

<div align="center" style="background: linear-gradient(135deg, #0f172a, #1e3a8a, #0ea5e9); color: white; padding: 20px 18px; border-radius: 18px; margin: 18px 0; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
  <p style="font-size: 1.2rem; margin: 0; font-weight: 700; text-transform: uppercase; letter-spacing: 2px;">
    ✨ Detect damaged regions • Restore old photos ✨
  </p>
</div>

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">

| 📖 **Overview** |
| :--- |
| PhotoRestore is a lightweight deep-learning application for detecting and restoring damaged old photographs. It combines automatic damage detection with a U-Net-based restoration pipeline to repair scratches, stains, small missing areas, and broken regions while preserving the original image content outside the damaged mask.<br><br>The project is intentionally kept minimal and deployment-friendly so it can run on Streamlit Community Cloud or any similar hosting platform. |

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">

| 🚀 **Features** | 🛠️ **Tech Stack** |
| :--- | :--- |
| <ul><li>**Upload** old/damaged images from the browser</li><li>**Auto-detect** scratches, stains, and damaged regions</li><li>**Targeted Restore:** Fixes broken areas, preserves untouched pixels</li><li>**U-Net CNN:** Uses trained model for reconstruction</li><li>**OpenCV Fallback:** Safe, lightweight repair</li><li>**Compare:** Side-by-side before/after comparison</li><li>**Export:** Download repaired images as PNG</li></ul> | <div align="center"><img src="https://skillicons.dev/icons?i=py,tensorflow,opencv,github&perline=2" /><br><br><b>NumPy • Pillow • Streamlit</b></div> |

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">

### 📁 Project Structure

```text
📦 PhotoRestore
 ┣ 📜 app.py                 # Streamlit web app
 ┣ 📜 config.py              # project configuration
 ┣ 📜 requirements.txt       # Python dependencies
 ┣ 📜 README.md              # project documentation
 ┣ 📜 .gitignore             # git ignore rules
 ┣ 📂 src                    # Source Code
 ┃ ┣ 📜 __init__.py
 ┃ ┣ 📜 detect.py            # damage detection
 ┃ ┣ 📜 enhance.py           # enhancement / post-processing
 ┃ ┗ 📜 restore.py           # repair pipeline
 ┣ 📂 models                 # Trained Models
 ┃ ┗ 📜 photorevive_unet.keras
 ┣ 📂 data                   # Image Datasets
 ┃ ┗ 📂 clean
 ┣ 📂 outputs                # Output artifacts
 ┗ 📂 __pycache__            # local cache

```

| ⚙️ **Installation & Setup** |
| --- |
| **1. Install Dependencies**<br>

<br>`bash`<br>

<br>`python -m venv .venv`<br>

<br>`source .venv/bin/activate`<br>

<br>`pip install -r requirements.txt`<br>

<br>`bash` |
| **2. Run Locally**<br>

<br>`bash`<br>

<br>`streamlit run app.py`<br>

<br>`bash` |
| **3. Run with Custom Host/Port**<br>

<br>`bash`<br>

<br>`streamlit run app.py --server.address 0.0.0.0 --server.port 8501`<br>

<br>`bash` |

| ☁️ **Streamlit Community Cloud Deployment** |
| --- |
| This repository is organized for deployment on Streamlit Community Cloud:<br>

<br>

<br>1️⃣ **Push** the repository to GitHub<br>

<br>2️⃣ **Connect** the repo to Streamlit Community Cloud<br>

<br>3️⃣ **Set** the app entry file to `app.py`<br>

<br>4️⃣ **Install** dependencies from `requirements.txt`<br>

<br>5️⃣ **Initialize:** The app will load the model from `models/photorevive_unet.keras` |

| 🧠 **Model Behavior** | 🎯 **Expected Output** |
| --- | --- |
| 🔹 Detects damaged areas<br>

<br>🔹 Creates a repair mask<br>

<br>🔹 Reconstructs damaged pixels via U-Net<br>

<br>🔹 Keeps original safe areas completely unchanged<br>

<br>🔹 Improves brightness and visual clarity post-restoration | 📸 Original photo display<br>

<br>🎭 Detected damage mask<br>

<br>✨ Restored photo<br>

<br>🔄 Interactive Before/After slider<br>

<br>📥 Downloadable repaired image |

> [!NOTE]
> **Important Notes:**
> * This project is optimized for practical old-photo restoration, not perfect historical reconstruction.
> * Performance improves with a larger training dataset and GPU training.
> * The app is designed to be simple, compact, and deployable for web use.
> 
>
