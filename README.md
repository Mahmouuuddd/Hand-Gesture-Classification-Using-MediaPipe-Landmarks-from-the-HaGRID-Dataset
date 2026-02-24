# 🖐 Hand Gesture Recognition using MediaPipe & XGBoost

> A real-time hand gesture recognition system that extracts hand landmarks using **MediaPipe** and classifies them using an optimized **XGBoost** model — deployed live via webcam with **OpenCV**. All experiments are tracked using **MLflow**.

---

## 🎬 Demo

https://github.com/user-attachments/assets/b1265bed-a123-487b-aa20-f466c937cc2d


---

## 📌 Table of Contents

- [Overview](#overview)
- [Branches](#branches)
- [Tech Stack](#tech-stack)
- [Important: Python Version Requirement](#important-python-version-requirement)
- [Setup Instructions](#setup-instructions)
- [Model Training](#model-training)
- [MLflow Experiment Tracking](#mlflow-experiment-tracking)
- [Evaluation Metrics](#evaluation-metrics)
- [Project Structure](#project-structure)

---

## Overview

This project implements a real-time hand gesture recognition system using computer vision and machine learning. Hand landmarks are extracted using **MediaPipe** and classified using an optimized **XGBoost** model.

The system captures hand keypoints from a webcam feed and predicts gesture classes in real time. Multiple models were trained and compared — all experiments are logged and visualized using **MLflow**.

---

## Branches

| Branch | Purpose |
|---|---|
| `main` | Stable production code — real-time inference with the final XGBoost model |
| `research` | MLflow experiment tracking — all 6 models trained, logged, and compared |

> 💡 The MLflow integration and full model comparison live in the [`research`](../../tree/research) branch. Switch to it to explore all experiment runs and metrics.

---

## Tech Stack

| Library | Purpose |
|---|---|
| **Python 3.12** | Core language |
| **MediaPipe** | Hand landmark detection |
| **OpenCV** | Video capture and frame processing |
| **XGBoost** | Gesture classification |
| **Scikit-learn** | Model evaluation |
| **MLflow** | Experiment tracking and model logging (`research` branch) |
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

> 📊 Full experiment comparisons across all 6 models are available in the [`research`](../../tree/research) branch via the MLflow dashboard.

---

## MLflow Experiment Tracking

> 🔬 This section applies to the [`research`](../../tree/research) branch.

All training runs are tracked using **MLflow**, allowing full comparison of every model across all metrics in a visual dashboard.

### Switch to the research branch

```bash
git checkout research
```

### Launch the MLflow UI

After running `Hand_project.ipynb`, start the tracking server from your terminal:

```bash
mlflow ui
```

Then open your browser at:

```
http://127.0.0.1:5000
```

You will see a dashboard comparing all runs side by side:

| Run | Model | Accuracy | F1 Score | Precision | Recall |
|---|---|---|---|---|---|
| 1 | XGBoost | ✅ best | ✅ best | ✅ best | ✅ best |
| 2 | Random Forest | — | — | — | — |
| 3 | AdaBoost | — | — | — | — |
| 4 | SVM | — | — | — | — |
| 5 | Logistic Regression | — | — | — | — |
| 6 | KNN | — | — | — | — |

### What is logged per run

- **Parameters** — model name and hyperparameters
- **Metrics** — accuracy, F1 score, precision, recall
- **Artifact** — the trained model saved and versioned by MLflow

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

**`main` branch:**
```
├── test.py                # Real-time webcam inference script
├── model.pkl              # Trained XGBoost model
├── requirements.txt       # Python dependencies
├── Hand_project.ipynb     # Training, evaluation, and analysis notebook
└── README.md
```

**`research` branch:**
```
├── test.py                # Real-time webcam inference script
├── model.pkl              # Trained XGBoost model
├── requirements.txt       # Python dependencies (includes mlflow)
├── Hand_project.ipynb     # Training, evaluation, and MLflow tracking notebook
├── mlruns/                # MLflow experiment logs (auto-generated, not committed)
└── README.md
```

---

<p align="center">Made by <a href="https://github.com/Mahmouuuddd">Mahmoud</a></p>


