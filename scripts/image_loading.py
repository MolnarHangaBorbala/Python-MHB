import cv2

# Load an image
img = cv2.imread("C:/Users/H/Desktop/robot-ai/images/Iexample1.jpg")

# Show the image in a window
cv2.imshow("My Image", img)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()




# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Grayscale", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()




# Edge Detection
edges = cv2.Canny(gray, 100, 200)

cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Detects contours/edges
# Plays a huge role in early robotics vision tasks




# Draw a rectangle
cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 3)  # green rectangle, 3px thick

# Draw a circle
cv2.circle(img, (300, 300), 50, (255, 0, 0), -1)  # filled blue circle

# Add text
cv2.putText(img, "Hello Robot!", (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

cv2.imshow("Drawings", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
