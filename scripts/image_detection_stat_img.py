from ultralytics import YOLO
import glob
import os
import cv2

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Paths
image_folder = "C:/Users/H/Desktop/robot-ai/images/*.jpg"
output_folder = "C:/Users/H/Desktop/robot-ai/output/img"
output_folder_no_detections = "C:/Users/H/Desktop/robot-ai/output/no_detections"

os.makedirs(output_folder, exist_ok=True)
os.makedirs(output_folder_no_detections, exist_ok=True)

# Get all image paths
image_paths = glob.glob(image_folder)

# Loop through images
idx = 1
for img_path in image_paths:
    results = model(img_path)
    orig_img = cv2.imread(img_path)  # BGR

    if len(results[0].boxes) == 0:
        save_path = os.path.join(output_folder_no_detections, f"Iexample{idx}-out-no-det.jpg")
        cv2.imwrite(save_path, orig_img)
        os.remove(img_path)  # Delete original image
        print(f"No detections: saved original image to {save_path}")
    else:
        # Get annotated image (already BGR)
        annotated_img = results[0].plot()

        # Save directly
        save_path = os.path.join(output_folder, f"Iexample{idx}-out.jpg")
        cv2.imwrite(save_path, annotated_img)
        print(f"Saved annotated image: {save_path}")
    idx += 1