import cv2
import numpy as np

# Load image
img = cv2.imread("rectangles.png")
if img is None:
    raise FileNotFoundError("Image 'rectangles.png' not found or path incorrect.")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 300, 450, apertureSize=3)

# Step 1: Detect rectangles
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
rectangles = []
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
    if len(approx) == 4 and cv2.contourArea(cnt) > 1000:
        rectangles.append(cnt)

print(f"Detected {len(rectangles)} rectangles")

# Step 2: Detect all lines
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=80, minLineLength=30, maxLineGap=10)
line_info = []
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        length = np.hypot(x2 - x1, y2 - y1)
        cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
        line_info.append({'length': length, 'center': (cx, cy), 'points': (x1, y1, x2, y2)})
else:
    print("No lines detected.")

print(f"Detected {len(line_info)} lines")

# Step 3: For each rectangle, find the longest internal line strictly inside (not on edges)
rect_line_pairs = []
for rect in rectangles:
    best_line = None
    max_len = 0
    for line in line_info:
        x1, y1, x2, y2 = line['points']
        center_x, center_y = (x1 + x2) / 2, (y1 + y2) / 2
        # Signed distance from center point to contour edge
        dist = cv2.pointPolygonTest(rect, (float(center_x), float(center_y)), True)
        # Accept lines whose center is at least 5 pixels inside polygon
        if dist > 5:
            if line['length'] > max_len:
                best_line = line
                max_len = line['length']
    if best_line is not None:
        rect_line_pairs.append({'rect': rect, 'line': best_line, 'line_length': max_len})

print(f"Rectangles with internal lines: {len(rect_line_pairs)}")

# Step 4: Sort rectangles by longest internal line length (shortest to longest)
sorted_pairs = sorted(rect_line_pairs, key=lambda x: x['line_length'])

# Optional: Draw the longest internal line on each rectangle for debugging
for pair in sorted_pairs:
    x1, y1, x2, y2 = pair['line']['points']
    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)  # Blue line for longest internal line

# Step 5: Label each rectangle based on ranking (1–4)
for i, pair in enumerate(sorted_pairs):
    rect_cnt = pair['rect']

    # Get rotated bounding box for accurate label position
    rot_rect = cv2.minAreaRect(rect_cnt)
    box = cv2.boxPoints(rot_rect)
    box = box.astype(int)

    # Sort box points by Y descending to get bottom points
    box = sorted(box, key=lambda p: p[1], reverse=True)
    bottom_pts = box[:2]
    bottom_center = np.mean(bottom_pts, axis=0)

    label_pos = (int(bottom_center[0] - 10), int(bottom_center[1] + 25))
    cv2.putText(img, str(i + 1), label_pos, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)

# Step 6: Save and show result
cv2.imwrite("ranked_rectangles_by_internal_line_length.png", img)
cv2.imshow("Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
