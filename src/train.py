import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# -------------------------
# LOAD DATA
# -------------------------

train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

train_data = train_datagen.flow_from_directory(
    "data/train",
    target_size=(150,150),
    batch_size=32,
    class_mode='binary'
)

test_data = test_datagen.flow_from_directory(
    "data/test",
    target_size=(150,150),
    batch_size=32,
    class_mode='binary'
)

# -------------------------
# BUILD MODEL
# -------------------------

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(150,150,3)),
    tf.keras.layers.MaxPooling2D(2,2),

    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),

    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# -------------------------
# TRAIN MODEL
# -------------------------

model.fit(
    train_data,
    validation_data=test_data,
    epochs=3
)

# -------------------------
# SAVE MODEL
# -------------------------

model.save("models/pneumonia_model.h5")

print("✅ Training complete!")