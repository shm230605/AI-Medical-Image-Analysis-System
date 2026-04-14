# 🧠 AI Medical Image Analysis System

## 🚀 Overview
This project uses Deep Learning (CNN) to detect Pneumonia from chest X-ray images.

## 🏥 Problem Statement
Manual diagnosis of X-rays is slow and error-prone. This AI system helps assist doctors by automatically classifying images.

## 🧰 Tech Stack
- Python
- TensorFlow / Keras
- OpenCV
- Matplotlib
- NumPy

## 📂 Dataset
Chest X-ray dataset (Kaggle):
- NORMAL
- PNEUMONIA

## 🧠 Model
- Convolutional Neural Network (CNN)
- Binary classification (Normal vs Pneumonia)

## 🚀 How to Run
```bash
python src/train.py
python show_pneumonia.py
```
📁  PROJECT STRUCTURE

```
AI-Medical-Image-Analysis-System/
│
├── data/
│   ├── train/
│   │    ├── NORMAL/
│   │    └── PNEUMONIA/
│   │
│   ├── test/
│        ├── NORMAL/
│        └── PNEUMONIA/
│
├── models/
│   └── pneumonia_model.h5
│
├── src/
│   ├── train.py
│   ├── predict.py
│   ├── preprocess.py   (optional upgrade)
│
├── outputs/
│   ├── accuracy_plot.png
│   ├── confusion_matrix.png
│
├── images/
│   ├── sample_normal.png
│   ├── sample_pneumonia.png
│
├── notebooks/
│   └── EDA.ipynb   (optional)
│
├── show_pneumonia.py
├── show_image.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── main.py
```
