import os, glob

folder_path = "C:/Users/H/Desktop/robot-ai/output/img"

# Step 1: Temporary rename
jpg_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".jpg")]
for idx, filename in enumerate(jpg_files, start=1):
    old_path = os.path.join(folder_path, filename)
    temp_path = os.path.join(folder_path, f"temp_{idx}.jpg")
    os.rename(old_path, temp_path)

# Step 2: Sequential rename
temp_files = sorted([f for f in os.listdir(folder_path) if f.startswith("temp_")])
for idx, filename in enumerate(temp_files, start=1):
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, f"Iexample{idx}-out.jpg")
    os.rename(old_path, new_path)