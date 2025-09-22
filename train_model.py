# import tensorflow as tf
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras import layers, models
# import os

# # Paths
# DATA_DIR = "dataset"
# IMG_SIZE = (128, 128)
# BATCH_SIZE = 32

# # Data Augmentation
# datagen = ImageDataGenerator(
#     rescale=1./255,
#     validation_split=0.2,
#     rotation_range=20,
#     width_shift_range=0.2,
#     height_shift_range=0.2,
#     horizontal_flip=True
# )

# train_gen = datagen.flow_from_directory(
#     DATA_DIR,
#     target_size=IMG_SIZE,
#     batch_size=BATCH_SIZE,
#     subset="training"
# )

# val_gen = datagen.flow_from_directory(
#     DATA_DIR,
#     target_size=IMG_SIZE,
#     batch_size=BATCH_SIZE,
#     subset="validation"
# )

# # CNN Model
# model = models.Sequential([
#     layers.Conv2D(32, (3,3), activation="relu", input_shape=(128,128,3)),
#     layers.MaxPooling2D(2,2),
#     layers.Conv2D(64, (3,3), activation="relu"),
#     layers.MaxPooling2D(2,2),
#     layers.Conv2D(128, (3,3), activation="relu"),
#     layers.MaxPooling2D(2,2),
#     layers.Flatten(),
#     layers.Dense(128, activation="relu"),
#     layers.Dropout(0.3),
#     layers.Dense(len(train_gen.class_indices), activation="softmax")
# ])

# model.compile(optimizer="adam",
#               loss="categorical_crossentropy",
#               metrics=["accuracy"])

# history = model.fit(
#     train_gen,
#     validation_data=val_gen,
#     epochs=15
# )

# # Save the model
# model.save("sign_language_model.h5")
# print("✅ Model saved as sign_language_model.h5")












# import tensorflow as tf
# from tensorflow.keras.preprocessing.image import ImageDataGenerator

# # Paths
# train_dir = "dataset/train"  # folder containing class subfolders
# val_dir = "dataset/val"

# # Data Augmentation
# train_datagen = ImageDataGenerator(
#     rescale=1./255,
#     rotation_range=15,
#     width_shift_range=0.1,
#     height_shift_range=0.1,
#     zoom_range=0.1,
#     horizontal_flip=True
# )

# val_datagen = ImageDataGenerator(rescale=1./255)

# train_generator = train_datagen.flow_from_directory(
#     train_dir,
#     target_size=(128,128),
#     batch_size=32,
#     class_mode="categorical"
# )

# val_generator = val_datagen.flow_from_directory(
#     val_dir,
#     target_size=(128,128),
#     batch_size=32,
#     class_mode="categorical"
# )

# # CNN Model
# model = tf.keras.Sequential([
#     tf.keras.layers.Conv2D(32, (3,3), activation="relu", input_shape=(128,128,3)),
#     tf.keras.layers.MaxPooling2D(2,2),
#     tf.keras.layers.Conv2D(64, (3,3), activation="relu"),
#     tf.keras.layers.MaxPooling2D(2,2),
#     tf.keras.layers.Flatten(),
#     tf.keras.layers.Dense(128, activation="relu"),
#     tf.keras.layers.Dense(4, activation="softmax")  # 4 classes
# ])

# model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# # Train
# history = model.fit(
#     train_generator,
#     validation_data=val_generator,
#     epochs=20
# )

# # Save Model
# model.save("sign_language_model.h5")






import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# --- Dataset paths ---
train_dir = "dataset/train"
val_dir = "dataset/val"

# --- Define classes ---
GESTURE_CLASSES = ["Hello", "I Love You", "Yes", "No"]
ALPHABET_CLASSES = ["A", "B", "C", "D", "E", "F", "G"]  # Only A to G
CLASS_NAMES = GESTURE_CLASSES + ALPHABET_CLASSES

# --- Data augmentation ---
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=15,
    width_shift_range=0.1,
    height_shift_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True
)

val_datagen = ImageDataGenerator(rescale=1./255)

train_gen = train_datagen.flow_from_directory(
    train_dir,
    target_size=(128,128),
    batch_size=32,
    class_mode="categorical"
)

val_gen = val_datagen.flow_from_directory(
    val_dir,
    target_size=(128,128),
    batch_size=32,
    class_mode="categorical"
)

# --- CNN Model ---
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation="relu", input_shape=(128,128,3)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation="relu"),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(len(CLASS_NAMES), activation="softmax")  # Output layer
])

# --- Compile ---
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# --- Train ---
history = model.fit(train_gen, validation_data=val_gen, epochs=30)

# --- Save model ---
model.save("sign_language_model.h5")

print("✅ Model trained and saved successfully!")
print(f"Classes: {CLASS_NAMES}")
