<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=800&size=40&pause=1000&color=0EA5E9&center=true&vCenter=true&width=800&lines=PhotoRestore;Damage+Detection;Deep+Learning+Restoration" alt="Typing SVG" />
  
  <p>
    <img alt="Status" src="https://img.shields.io/badge/Status-Deployment%20Ready-success?style=for-the-badge&logo=appveyor" />
    <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" />
    <img alt="TensorFlow" src="https://img.shields.io/badge/TensorFlow-Keras-orange?style=for-the-badge&logo=tensorflow&logoColor=white" />
    <img alt="UI" src="https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  </p>
</div>

<div align="center" style="background: linear-gradient(135deg, #0f172a, #1e3a8a, #0ea5e9); color: white; padding: 25px 20px; border-radius: 12px; margin: 24px 0; box-shadow: 0 4px 15px rgba(0,0,0,0.25);">
  <h3 style="margin: 0; color: #ffffff; font-weight: 700; text-transform: uppercase; letter-spacing: 2px;">
    ✨ Detect Damaged Regions • Restore Old Photos ✨
  </h3>
  <p style="margin: 8px 0 0 0; opacity: 0.9; font-size: 0.95rem;">
    An elegant, production-ready deep learning pipeline designed to automatically detect and repair photographic degradation.
  </p>
</div>

---

### 📖 Overview

**PhotoRestore** is a lightweight deep-learning application engineered for automated detection and restoration of damaged historical photographs. It seamlessly pairs intelligent flaw segmentation with a dedicated **U-Net architecture** to repair complex surface defects—including deep scratches, chemical stains, missing paper fragments, and structural cracks—while strictly preserving native pixel structures outside the damaged boundaries.

Built with performance and accessibility in mind, the platform features a streamlined deployment footprint perfectly optimized for instant publication across cloud-native environments like **Streamlit Community Cloud**.

---

### 🚀 Core Strengths & Tech Stack

<table width="100%">
<tr>
<td width="65%" valign="top">

#### Key Capabilities
* **Instant In-Browser Processing:** Upload damaged digital formats directly from your web window.
* **Intelligent Defect Localization:** Auto-detects scratches, degradation masks, and fading regions dynamically.
* **Targeted Inpainting Engine:** Reconstructs damaged pixels via a trained neural network while maintaining full original structural integrity elsewhere.
* **Hybrid Processing Pipeline:** Utilizes deep convolutional U-Net architectures backed by high-speed OpenCV recovery mechanics.
* **Interactive Side-by-Side Comparison:** Evaluates results instantly using intuitive visual split views.
* **Lossless Export Formats:** Download finalized restoration assets as transparent, full-fidelity PNG packages.

</td>
<td width="35%" valign="top" align="center">

#### Integrated Technologies
<img src="https://skillicons.dev/icons?i=py,tensorflow,opencv,github&perline=2" width="140px" alt="Skills Stack" />

**Core Libraries:**
`NumPy` • `Pillow` • `Streamlit` • `Keras`

</td>
</tr>
</table>

---

### 📁 Architecture & File Layout

```text
📦 PhotoRestore
 ┣ 📜 app.py                 # Core Streamlit web dashboard application
 ┣ 📜 config.py              # Application settings, neural variables, and hyperparameters
 ┣ 📜 requirements.txt       # Environment manifest mapping exact package dependencies
 ┣ 📜 README.md              # Project onboarding documentation
 ┣ 📜 .gitignore             # Version control filter rules
 ┣ 📂 src                    # Source Execution Modules
 ┃ ┣ 📜 __init__.py          # Target package definition module
 ┃ ┣ 📜 detect.py            # Defect location and mask creation algorithms
 ┃ ┣ 📜 enhance.py           # Post-restoration color balancing and sharpness modules
 ┃ ┗ 📜 restore.py           # Unified restoration model execution pipeline
 ┣ 📂 models                 # Persistent Model Storage Artifacts
 ┃ ┗ 📜 photorevive_unet.keras  # Pre-compiled, production-trained weights
 ┣ 📂 data                   # Evaluation & Training Datasets
 ┃ ┗ 📂 clean                # Anchor ground-truth references
 ┣ 📂 outputs                # Cached exports and generated session assets
 ┗ 📂 __pycache__            # Native interpreter runtime cache strings
```

---

### ⚙️ Local Sandbox Setup

#### 1. Setup Environment & Install Dependencies
Initialize a clean Python virtualization space to safely mount the execution modules without global package contamination:

```bash
# Create and activate execution container environment
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Update core packaging tools and map application prerequisites
pip install --upgrade pip
pip install -r requirements.txt
```

#### 2. Run the Interface Locally
Boot the standard engine runtime instance natively mapped to standard internal network hooks:

```bash
streamlit run app.py
```

#### 3. Enterprise/Custom Host Mapping
Bind performance layers explicitly across targeted routing properties or exposed proxy containers:

```bash
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

---

### ☁️ Cloud Deployment Configuration

This engine is optimized for seamless deployment workflows directly within the **Streamlit Community Cloud ecosystem**:

1. **Synchronize Codebase:** Commit configuration layers and push the managed source branch cleanly onto GitHub.
2. **Bind Application Portal:** Authenticate your platform dashboard and link the target git repository.
3. **Appoint Core Endpoint:** Declare `app.py` as the direct execution target path script.
4. **Environment Generation:** Ensure dependencies are built dynamically from the root `requirements.txt` catalog.
5. **Cold Initialization:** On container initialization, the model weights layer located inside `models/photorevive_unet.keras` will be cached directly into high-speed runtime memory.

---

### 🧠 Operational Topology & Expected Outputs

<table width="100%">
<tr>
<th width="50%">🧬 Pipeline Model Behavior</th>
<th width="50%">🎯 Generated UI Output Matrix</th>
</tr>
<tr>
<td>

* **Dynamic Surface Segmentation:** Explicitly traces pixel inconsistencies to generate anomaly zones.
* **High-Contrast Mask Mapping:** Builds targeted binary arrays blocking safe regions from adjustment.
* **Deep Neural Interpolation:** Passes localized artifacts into a custom-fit U-Net layout to predict missing contextual elements.
* **Preservation Enforcement:** Enforces strict boundary logic locking clean pixels against alterations.
* **Structural Enhancement:** Apples contrast, tint matching, and edge enhancement arrays dynamically post-inpainting.

</td>
<td>

* **Original Photo Canvas:** Full resolution viewport accommodating flexible image uploads.
* **Damage Isolation Overlay:** Informative diagnostic view rendering active pixel masks.
* **Restored Output Stage:** Clean canvas displaying reconstructed, noise-reduced image states.
* **Interactive Compare Slider:** High-precision layout widget providing direct before/after evaluations.
* **One-Click Asset Downloader:** Direct file download utility exporting pristine restored image bundles.

</td>
</tr>
</table>

---

> [!NOTE]
> **Production Guidelines:**
> * This pipeline is engineered for practical old-photo restoration and scratch repair, rather than complete, context-aware historical reconstruction.
> * Inference accuracy scales dynamically with larger, higher-resolution dataset training passes and dedicated GPU resources.
> * The system footprint is tailored to remain compact, responsive, and readily deployable within cloud-hosted server environments.
