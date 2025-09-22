import streamlit as st
import requests
from PIL import Image
import io

# --- Page Config ---
st.set_page_config(page_title="Sign Language Recognition", layout="wide")

# --- Header ---
st.markdown("""
<div style='background-color:#1E3A8A;padding:20px;border-radius:10px;text-align:center;'>
<h1 style='color:#FFD700;'>🤟 Sign Language Recognition</h1>
</div>
""", unsafe_allow_html=True)

st.write("Upload an image **or** use your camera to detect gestures and alphabet signs:")

# --- Tabs: Upload Image or Camera ---
tab1, tab2 = st.tabs(["Upload Image", "Use Camera"])

# --- Function to send image to backend ---
def predict_gesture(file_bytes, filename="image.jpg"):
    files = {"file": (filename, file_bytes, "image/jpeg")}
    try:
        response = requests.post("http://localhost:8000/predict", files=files)
        if response.status_code == 200:
            result = response.json()
            st.info(
                f"Predicted Gesture/Letter: **{result['gesture']}**  "
                f"| Accuracy: **{result['accuracy']}%**"
            )
        else:
            st.error(f"❌ Backend error: {response.status_code}")
    except Exception as e:
        st.error(f"⚠️ Connection failed: {e}")

# --- Tab 1: Upload Image ---
with tab1:
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
        with col2:
            st.success("✅ Image uploaded successfully!")
            # Send to backend
            predict_gesture(uploaded_file.getvalue(), uploaded_file.name)

# --- Tab 2: Use Camera ---
with tab2:
    camera_image = st.camera_input("Take a picture")
    if camera_image is not None:
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(camera_image, caption="Captured Image", use_container_width=True)
        with col2:
            st.success("✅ Image captured successfully!")
            # Send to backend
            predict_gesture(camera_image.getvalue(), "camera.jpg")
    