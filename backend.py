# from fastapi import FastAPI, File, UploadFile
# from fastapi.middleware.cors import CORSMiddleware
# import numpy as np
# from PIL import Image
# import io
# import tensorflow as tf

# app = FastAPI()

# # Allow frontend
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Load Model & Classes
# model = tf.keras.models.load_model("sign_language_model.h5")
# CLASS_NAMES = ["Hello", "I Love You", "Yes", "No"]  # same as your dataset folder names

# @app.get("/")
# def root():
#     return {"message": "Sign Language API is running ✅"}

# @app.post("/predict")
# async def predict(file: UploadFile = File(...)):
#     # Read image
#     contents = await file.read()
#     img = Image.open(io.BytesIO(contents)).convert("RGB")
#     img = img.resize((128, 128))
#     img_array = np.array(img) / 255.0
#     img_array = np.expand_dims(img_array, axis=0)

#     # Predict
#     predictions = model.predict(img_array)
#     index = np.argmax(predictions[0])
#     accuracy = float(np.max(predictions[0]) * 100)

#     return {
#         "gesture": CLASS_NAMES[index],
#         "accuracy": round(accuracy, 2)
#     }

# from fastapi import FastAPI, File, UploadFile
# from fastapi.middleware.cors import CORSMiddleware
# import numpy as np
# from PIL import Image
# import io
# import tensorflow as tf

# app = FastAPI()

# # Allow frontend connections
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Load model & class names
# MODEL_PATH = "sign_language_model.h5"
# model = tf.keras.models.load_model(MODEL_PATH)
# CLASS_NAMES = ["Hello", "I Love You", "Yes", "No"]  # Make sure this matches your dataset folders

# @app.get("/")
# def root():
#     return {"message": "Sign Language API is running ✅"}

# @app.post("/predict")
# async def predict(file: UploadFile = File(...)):
#     # --- Read and preprocess image ---
#     contents = await file.read()
#     try:
#         img = Image.open(io.BytesIO(contents)).convert("RGB")
#     except Exception as e:
#         return {"error": f"Cannot read image: {e}"}

#     img = img.resize((128, 128))
#     img_array = np.array(img) / 255.0
#     img_array = np.expand_dims(img_array, axis=0)

#     # --- Predict ---
#     predictions = model.predict(img_array)
#     index = int(np.argmax(predictions[0]))
#     accuracy = float(np.max(predictions[0]) * 100)

#     # --- Debugging prints ---
#     print("Predictions array:", predictions)
#     print("Predicted class index:", index, "->", CLASS_NAMES[index])

#     return {
#         "gesture": CLASS_NAMES[index],
#         "accuracy": round(accuracy, 2)
#     }


from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from PIL import Image
import io
import tensorflow as tf

app = FastAPI()

# Allow frontend
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

# Load model & classes
model = tf.keras.models.load_model("sign_language_model.h5")
GESTURE_CLASSES = ["Hello", "I Love You", "Yes", "No"]
ALPHABET_CLASSES = [chr(i) for i in range(65, 91)]  # A-Z
CLASS_NAMES = GESTURE_CLASSES + ALPHABET_CLASSES

@app.get("/")
def root():
    return {"message": "Sign Language API is running ✅"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    img = Image.open(io.BytesIO(contents)).convert("RGB")
    img = img.resize((128, 128))
    img_array = np.expand_dims(np.array(img)/255.0, axis=0)

    predictions = model.predict(img_array)
    index = int(np.argmax(predictions[0]))
    accuracy = float(np.max(predictions[0]) * 100)

    return {
        "gesture": CLASS_NAMES[index],
        "accuracy": round(accuracy, 2)
    }
