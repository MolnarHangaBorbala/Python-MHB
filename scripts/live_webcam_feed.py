from ultralytics import YOLO
import cv2
import os

# Load YOLOv8 model
model = YOLO("yolov8n.pt")  # You can change to yolov8s.pt, etc.

# Output folders
output_folder = "C:/Users/H/Desktop/robot-ai/output/webcam_detections"
os.makedirs(output_folder, exist_ok=True)

# Initialize webcam (0 = default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

frame_idx = 1
print("Press 'q' to quit...")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Run YOLO inference on the frame
    results = model(frame)

    # Annotated frame
    annotated_frame = results[0].plot()

    # Display frame
    cv2.imshow("YOLOv8 Webcam Detection", annotated_frame)

    # Optionally save detections
    save_path = os.path.join(output_folder, f"frame_{frame_idx}.jpg")
    cv2.imwrite(save_path, annotated_frame)
    frame_idx += 1

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
print("Webcam detection stopped.")