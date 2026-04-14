import cv2
import numpy as np
import tensorflow as tf

# Load model
model = tf.keras.models.load_model("models/pneumonia_model.h5")

def predict_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (150,150))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)[0][0]

    if prediction > 0.5:
        print("🔴 Pneumonia Detected")
    else:
        print("🟢 Normal")

# TEST IMAGE
predict_image("data/test/NORMAL/sample.jpeg")