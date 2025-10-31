import cv2

cap = cv2.VideoCapture("C:/Users/H/Desktop/robot-ai/videos/Vexample2.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Video Feed", gray)
    
    edges = cv2.Canny(gray, 100, 200)
    cv2.imshow("Edges", edges)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()