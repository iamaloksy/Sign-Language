# AI-Powered Sign Language Translator

## Description
This project translates **American Sign Language (ASL) letters** into text and speech in real-time using a webcam.

## Features
- Real-time hand detection using **MediaPipe**
- Gesture classification using **CNN**
- Text and optional speech output
- Clear modular structure

## Requirements
- Python 3.8+
- OpenCV, MediaPipe, TensorFlow, NumPy, Pandas, pyttsx3

## How to Run
1. Download ASL dataset into `asl_dataset/` (folders A-Z)
2. Train model:
    ```
    python train_model.py
    ```
3. Run real-time translator:
    ```
    python app.py
    ```
4. Press **ESC** to quit, **C** to clear sentence.
