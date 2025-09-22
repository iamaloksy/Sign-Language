import cv2
import os

# Classes to capture
CLASSES = ["Hello", "I Love You", "Yes", "No"]
NUM_IMAGES = 300  # per class

# Create directories
os.makedirs("dataset", exist_ok=True)
for c in CLASSES:
    os.makedirs(f"dataset/{c}", exist_ok=True)

cap = cv2.VideoCapture(0)

for gesture in CLASSES:
    print(f"Collecting images for {gesture}...")
    count = 0
    while count < NUM_IMAGES:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Capture Gesture", frame)

        # Save frame every few milliseconds
        if cv2.waitKey(1) & 0xFF == ord('s'):  # Press 's' to save
            img_path = f"dataset/{gesture}/{count}.jpg"
            cv2.imwrite(img_path, frame)
            count += 1
            print(f"Saved {img_path}")

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit early
            break

cap.release()
cv2.destroyAllWindows()
