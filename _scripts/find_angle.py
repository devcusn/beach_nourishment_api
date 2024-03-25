import cv2
import numpy as np
import math

# Load image
image = cv2.imread('triangle2.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Preprocess (if necessary)

# Edge detection
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Find contours
contours, _ = cv2.findContours(
    edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter contours based on area or other criteria if necessary

# Iterate through contours
for contour in contours:
    # Approximate the contour to a polygon
    epsilon = 0.04 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    # If the contour has 3 vertices (triangle), calculate angles
    if len(approx) == 3:
        # Calculate angles between the lines connecting the vertices
        pts = approx.reshape(3, 2)
        angles = []
        for i in range(3):
            # Calculate the cosine of the angle using dot product
            v1 = pts[(i + 1) % 3] - pts[i]
            v2 = pts[(i + 2) % 3] - pts[i]
            cosine_angle = np.dot(v1, v2) / \
                (np.linalg.norm(v1) * np.linalg.norm(v2))
            angle = np.arccos(cosine_angle)
            # Convert angle to degrees
            angle_deg = np.degrees(angle)
            angles.append(angle_deg)

        # Print angles
        print("Angles of the triangle:", angles)

        # Visualize the triangle and angles (optional)
        cv2.drawContours(image, [approx], 0, (0, 255, 0), 3)
        for i in range(3):
            cv2.putText(image, str(round(angles[i], 2)), tuple(
                pts[i]), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

# Show the image
cv2.imshow('Triangle with Angles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
