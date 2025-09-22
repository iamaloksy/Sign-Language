# frontend_classy.py
import streamlit as st
import random
from PIL import Image
import cv2
import tempfile

st.set_page_config(page_title="Sign Language Recognition", layout="wide")

# --- Header ---
st.markdown("""
<div style="background-color:#1E3A8A;padding:20px;border-radius:10px;text-align:center;">
<h1 style="color:#FFD700;">🤟 Sign Language Recognition</h1>
<p style="color:#FFFFFF;font-size:18px;">Frontend-only demo with local simulation of predictions.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Image Upload Section ---
st.markdown("<h3 style='color:#1E3A8A;'>Upload Your Hand Gesture Image</h3>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    with col2:
        accuracy = random.uniform(97, 99)
        st.success(f"✅ Image uploaded successfully!")
        st.info(f"Predicted Gesture: 'Hello' (simulated) | Accuracy: {accuracy:.2f}%")

st.markdown("---")

# --- Camera / Live Video Section ---
st.markdown("<h3 style='color:#1E3A8A;'>Capture Using Camera</h3>", unsafe_allow_html=True)
if st.button("Open Camera"):
    st.info("📷 Camera activated (simulated). Capture your gesture below.")
    picture = st.camera_input("Take a picture")

    if picture:
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(picture, caption="Captured Image", use_column_width=True)
        with col2:
            accuracy = random.uniform(97, 99)
            st.success(f"Gesture captured successfully!")
            st.info(f"Predicted Gesture: 'Thank You' (simulated) | Accuracy: {accuracy:.2f}%")

st.markdown("---")

# --- Buttons Section ---
st.markdown("<h3 style='color:#1E3A8A;'>Other Interactions</h3>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Predict Gesture"):
        accuracy = random.uniform(97, 99)
        st.info(f"Predicted Gesture: 'Yes' (simulated) | Accuracy: {accuracy:.2f}%")

with col2:
    if st.button("Clear All"):
        st.experimental_rerun()

with col3:
    if st.button("Help"):
        st.info("Upload an image or capture using the camera to simulate gesture recognition. Accuracy is generated locally for demo purposes.")

# --- Footer ---
st.markdown("""
<div style="background-color:#1E3A8A;padding:15px;border-radius:10px;text-align:center;">
<p style="color:#FFD700;"> Simulation </p>
</div>
""", unsafe_allow_html=True)
