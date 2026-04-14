import cv2
import matplotlib.pyplot as plt
import os

# Path to pneumonia images
folder = "data/train/PNEUMONIA"

# Get image list
images = os.listdir(folder)

# Pick first image
img_name = images[0]
img_path = os.path.join(folder, img_name)

print("Showing image:", img_name)

# Read image
img = cv2.imread(img_path)

# Convert BGR → RGB (IMPORTANT)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Show image
plt.imshow(img)
plt.title("PNEUMONIA X-Ray")
plt.axis("off")
plt.show()