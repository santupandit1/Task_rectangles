import cv2
import numpy as np

# Load image
img = cv2.imread("rectangles.png")
if img is None:
    raise FileNotFoundError("Image not found or path incorrect.")

output = np.ones_like(img) * 255  # white background
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 300, 450, apertureSize=3)

# Detect rectangles
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
rectangles = []
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
    if len(approx) == 4 and cv2.contourArea(cnt) > 1000:
        rectangles.append(cnt)

# Process each rectangle: rotate upright and paste on clean canvas
for cnt in rectangles:
    rot_rect = cv2.minAreaRect(cnt)
    center, (w, h), angle = rot_rect

    if w < h:
        angle -= 90
        w, h = h, w

    # Get rotation matrix
    M = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Rotate the full image
    rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]), flags=cv2.INTER_CUBIC)

    # Crop the upright rectangle
    x = int(center[0] - w / 2)
    y = int(center[1] - h / 2)
    w, h = int(w), int(h)

    x = max(0, x)
    y = max(0, y)
    if x + w > rotated.shape[1]: w = rotated.shape[1] - x
    if y + h > rotated.shape[0]: h = rotated.shape[0] - y

    cropped = rotated[y:y+h, x:x+w]

    # Paste the clean rotated rectangle back onto a blank white image
    output[y:y+h, x:x+w] = cropped

# Save and display
cv2.imwrite("clean_upright_rectangles.png", output)
cv2.imshow("Upright Rectangles Only", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
