# 🖐 Hand Gesture Classification Using MediaPipe Landmarks from the HaGRID Dataset

> Real-time hand gesture recognition system using **MediaPipe** for 3D landmark extraction and **XGBoost** for robust multi-class classification — with live webcam deployment via **OpenCV**.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Pipeline](#pipeline)
- [Preprocessing](#preprocessing)
- [Model](#model)
- [Evaluation](#evaluation)
- [Real-Time Deployment](#real-time-deployment)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [License](#license)

---

## Overview

This project implements an end-to-end pipeline for classifying hand gestures in real time. Instead of processing raw image pixels, the system leverages **MediaPipe Hands** to extract 21 3D hand landmarks per frame, which are then normalized and fed into a trained **XGBoost** classifier. The resulting model is lightweight, fast, and accurate enough for live webcam inference.

**Key highlights:**
- Landmark-based (not pixel-based) approach — compact, interpretable, and hardware-efficient
- Translation and scale normalization for position-invariant features
- Multi-class classification across 18 gesture categories from the HaGRID dataset
- Real-time deployment with bounding box and label overlay via OpenCV

---

## Dataset

The project uses the [**HaGRID**](https://github.com/hukenovs/hagrid) (HAnd Gesture Recognition Image Dataset), one of the largest publicly available gesture datasets.

| Property | Value |
|---|---|
| Gesture classes | 18 |
| Subjects | 34,730+ |
| Image resolution | Up to 1920×1080 |
| Backgrounds | Diverse real-world environments |
| Hand types | Left, right, and two-handed |

**Gesture classes included:**

`call` · `dislike` · `fist` · `four` · `like` · `mute` · `ok` · `one` · `palm` · `peace` · `peace_inverted` · `rock` · `stop` · `stop_inverted` · `three` · `three2` · `two_up` · `two_up_inverted`

> **Note:** MediaPipe landmark extraction is run as a preprocessing step on the HaGRID images to produce the feature dataset used for training.

---

## Pipeline

```
┌──────────────┐    ┌──────────────────┐    ┌───────────────────┐    ┌─────────────┐    ┌──────────────┐
│  HaGRID      │───▶│  MediaPipe Hands │───▶│  Normalization    │───▶│  XGBoost    │───▶│  Prediction  │
│  Images /    │    │  21 Landmarks    │    │  (translation +   │    │  Classifier │    │  + Overlay   │
│  Webcam Feed │    │  (x, y, z) each  │    │   scale)          │    │             │    │              │
└──────────────┘    └──────────────────┘    └───────────────────┘    └─────────────┘    └──────────────┘
```

---

## Preprocessing

Raw landmark coordinates vary depending on hand position and distance from the camera. To make features **position- and scale-invariant**, the following normalization is applied before training and inference:

**1. Translation normalization** — Subtract the wrist landmark (landmark 0) from all other landmarks, centering the hand at the origin:

```python
landmarks = landmarks - landmarks[0]  # wrist becomes (0, 0, 0)
```

**2. Scale normalization** — Divide by the maximum absolute coordinate value, bounding all values to [−1, 1]:

```python
landmarks = landmarks / np.max(np.abs(landmarks))
```

The result is a **63-dimensional feature vector** (21 landmarks × 3 axes: x, y, z) that is consistent regardless of where in the frame the hand appears.

---

## Model

**Classifier:** XGBoost (`XGBClassifier`)

XGBoost was selected for its strong performance on tabular data, fast inference, and robustness to feature interactions — making it well-suited to the structured landmark feature vectors.

**Key hyperparameters (tunable):**

| Parameter | Description |
|---|---|
| `n_estimators` | Number of boosting rounds |
| `max_depth` | Maximum tree depth |
| `learning_rate` | Boosting step size |
| `subsample` | Row subsampling ratio |
| `colsample_bytree` | Feature subsampling ratio |
| `objective` | `multi:softmax` for multi-class |

---

## Evaluation

The model is evaluated using the following metrics, reported both per-class and as weighted averages:

| Metric | Description |
|---|---|
| **F1 Score** | Harmonic mean of precision and recall |
| **Precision** | Fraction of predicted positives that are correct |
| **Recall** | Fraction of true positives correctly identified |
| **Confusion Matrix** | Full class-by-class breakdown |

Evaluation is performed on a held-out test split to ensure unbiased reporting.

---

## Real-Time Deployment

The inference script streams video from a webcam using **OpenCV**, runs MediaPipe detection per frame, normalizes the landmarks, and passes them to the trained XGBoost model. The predicted gesture label is rendered directly onto the live video feed.

```
Webcam Frame
    │
    ▼
MediaPipe Hands → 21 landmarks (x, y, z)
    │
    ▼
Normalize (translate + scale)
    │
    ▼
XGBoost.predict() → class index
    │
    ▼
cv2.putText() → display label on frame
```

---

## Project Structure

```
Hand-Gesture-Classification/
│
├── data/
│   └── landmarks.csv            # Extracted landmark features + labels
│
├── notebooks/
│   ├── 01_extraction.ipynb      # MediaPipe landmark extraction from HaGRID
│   ├── 02_preprocessing.ipynb   # Normalization & feature engineering
│   ├── 03_training.ipynb        # XGBoost training & hyperparameter tuning
│   └── 04_evaluation.ipynb      # Metrics, confusion matrix, class analysis
│
├── models/
│   └── gesture_model.json       # Saved XGBoost model
│
├── inference.py                 # Real-time webcam inference script
├── requirements.txt
└── README.md
```

---

## Installation

**Requirements:** Python 3.8+

```bash
# Clone the repository
git clone https://github.com/Mahmouuuddd/Hand-Gesture-Classification-Using-MediaPipe-Landmarks-from-the-HaGRID-Dataset.git
cd Hand-Gesture-Classification-Using-MediaPipe-Landmarks-from-the-HaGRID-Dataset

# Install dependencies
pip install -r requirements.txt
```

**`requirements.txt`**

```
mediapipe
xgboost
opencv-python
numpy
pandas
scikit-learn
matplotlib
seaborn
```

---

## Usage

### 1. Extract Landmarks from HaGRID

Run the extraction notebook or script to process HaGRID images with MediaPipe and save the landmark CSV.

```bash
jupyter notebook notebooks/01_extraction.ipynb
```

### 2. Train the Model

```bash
jupyter notebook notebooks/03_training.ipynb
```

The trained model is saved to `models/gesture_model.json`.

### 3. Evaluate

```bash
jupyter notebook notebooks/04_evaluation.ipynb
```

### 4. Run Real-Time Inference

```bash
python inference.py
```

Press `q` to quit the webcam window.

---

## Results

> Replace the table below with your actual results after training.

| Metric | Score |
|---|---|
| Weighted F1 Score | — |
| Weighted Precision | — |
| Weighted Recall | — |
| Test Accuracy | — |

Per-class F1 scores and the full confusion matrix are available in `notebooks/04_evaluation.ipynb`.

---

## License

This project is released under the [MIT License](LICENSE).

The HaGRID dataset is subject to its own [license terms](https://github.com/hukenovs/hagrid#license). Please review them before commercial use.

---

<p align="center">Made by <a href="https://github.com/Mahmouuuddd">Mahmoud</a></p>