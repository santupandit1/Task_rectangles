# 🔢 Rectangle Numbering by Internal Line Length

This Python script detects rectangles in an image and ranks them **based on the length of the longest internal line strictly inside each rectangle**, then numbers them from shortest to longest.

---

## 📸 Input

- A single image file named `rectangles.png` containing multiple rectangles with internal lines.

---

## 🖼️ Output

- An annotated image named `ranked_rectangles_by_internal_line_length.png`, where:
  - Each rectangle is numbered from **1 (shortest internal line)** to **N (longest)**.
  - The longest internal line in each rectangle is optionally drawn in **blue**.
  
---

## ⚙️ Requirements

- Python 3.x
- OpenCV
- NumPy

Install dependencies using:

```bash
pip install opencv-python numpy
********************************************************
🚀 How to Run
Place your image as rectangles.png in the project directory.

Run the script:

bash
Copy
Edit
python rectangle_numbering.py
The output image ranked_rectangles_by_internal_line_length.png will be saved and displayed.

🧠 How It Works
1. Edge & Contour Detection
Converts the image to grayscale and detects edges using Canny.

Finds external contours and filters out non-rectangles using polygon approximation.

2. Line Detection
Uses the Hough Line Transform (cv2.HoughLinesP) to detect all lines in the image.

Calculates each line's center point and length.

3. Match Lines to Rectangles
For each rectangle, it finds the longest internal line, defined as:

Line center lies strictly inside the rectangle (5+ pixels from edge using cv2.pointPolygonTest).

Among valid lines, the longest one is selected.

4. Ranking and Labeling
Rectangles are sorted by the length of their best internal line.

Each is labeled from 1 to N using cv2.putText near its bottom center.


