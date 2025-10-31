from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Path to your video file
video_path = "C:/Users/H/Desktop/robot-ai/videos/Vexample2.mp4"

# Run detection on the video
results = model(video_path)

# Show/save the results
for r in results:
    r.show()      # shows each frame with detections

# VERY VERY SLOW