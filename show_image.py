import cv2
import matplotlib.pyplot as plt
import os

# Folder for pneumonia images
folder = "data/train/PNEUMONIA"

# Check folder exists
if not os.path.exists(folder):
    print("❌ Folder not found:", folder)
    exit()

# Get all image files
images = os.listdir(folder)
images = [f for f in images if f.endswith(('.jpeg', '.jpg', '.png'))]

import os

folder = "data/train/PNEUMONIA"

print("Checking folder:", folder)

if not os.path.exists(folder):
    print("❌ Folder does NOT exist!")
else:
    print("✅ Folder exists")

    files = os.listdir(folder)
    print("Total files found:", len(files))

    print("First 10 files:", files[:10])