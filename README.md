# 🖐 Hand Gesture Recognition using MediaPipe & XGBoost

> A real-time hand gesture recognition system that extracts hand landmarks using **MediaPipe** and classifies them using an optimized **XGBoost** model — deployed live via webcam with **OpenCV**.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Important: Python Version Requirement](#important-python-version-requirement)
- [Setup Instructions](#setup-instructions)
- [Model Training](#model-training)
- [Evaluation Metrics](#evaluation-metrics)
- [Project Structure](#project-structure)

---

## Overview

This project implements a real-time hand gesture recognition system using computer vision and machine learning. Hand landmarks are extracted using **MediaPipe** and classified using an optimized **XGBoost** model.

The system captures hand keypoints from a webcam feed and predicts gesture classes in real time.

---

## Tech Stack

| Library | Purpose |
|---|---|
| **Python 3.12** | Core language |
| **MediaPipe** | Hand landmark detection |
| **OpenCV** | Video capture and frame processing |
| **XGBoost** | Gesture classification |
| **Scikit-learn** | Model evaluation |
| **NumPy & Pandas** | Data manipulation |

---

## ⚠️ Important: Python Version Requirement

**This project requires Python 3.12.**

MediaPipe is currently not compatible with Python 3.14. Attempting to install or run MediaPipe on Python 3.14 will result in import errors.

To avoid compatibility issues, a virtual environment was created using Python 3.12 specifically for this project.

---

## Setup Instructions

### 1. Create Virtual Environment (Python 3.12 Required)

Make sure Python 3.12 is installed on your system.

**Mac/Linux:**
```bash
python3.12 -m venv venv
```

**Windows:**
```bash
py -3.12 -m venv venv
```

---

### 2. Activate the Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the Application

```bash
python test.py
```

---

## Model Training

The following models were evaluated and compared during development:

| Model | Notes |
|---|---|
| Support Vector Machine (SVM) | Baseline |
| Logistic Regression | Baseline |
| Random Forest | Ensemble method |
| K-Nearest Neighbors (KNN) | Distance-based |
| AdaBoost | Boosting method |
| **XGBoost** | ✅ **Selected — best overall performance** |

**XGBoost** achieved the best performance across all evaluation metrics and was selected as the final model.

The trained model is saved as `model.pkl` and loaded at inference time by `test.py`.

---

## Evaluation Metrics

The model was evaluated using the following metrics:

- **Accuracy** — Overall fraction of correct predictions
- **Precision** — Of all predicted positives, how many were correct
- **Recall** — Of all true positives, how many were correctly identified
- **F1-Score** — Harmonic mean of precision and recall

Full evaluation details and per-class breakdowns are available in `Hand_project.ipynb`.

---

## Project Structure

```
├── test.py                # Real-time webcam inference script
├── sgb_hand_gesture_model.pkl              # Trained XGBoost model
├── requirements.txt       # Python dependencies
├── Hand_project.ipynb     # Training, evaluation, and analysis notebook
└── label_encoder.pkl      # For Labels output 
└── README.md
```

---

<p align="center">Made by <a href="https://github.com/Mahmouuuddd">Mahmoud</a></p>