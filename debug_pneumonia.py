import os

folder = "data/train/PNEUMONIA"

print("Checking:", folder)

if not os.path.exists(folder):
    print("❌ Folder NOT found")
else:
    print("✅ Folder exists")

    files = os.listdir(folder)
    print("Total files:", len(files))

    print("First 5 files:", files[:5])