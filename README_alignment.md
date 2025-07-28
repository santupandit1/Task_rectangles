# Task_rectangles
# 🧾 Rectangle Alignment Tool

This Python script detects rotated rectangles in an image and realigns them to 0 degrees (upright), maintaining their original positions in the image. It’s useful for preprocessing images where rectangular objects need to be standardized for further analysis or visualization.

---

## 📸 Input

- A single image file named `rectangles.png` containing multiple rotated rectangles (with or without internal lines).

---

## 🎯 Output

- A new image `clean_upright_rectangles.png` with the same dimensions as the input.
- Each rectangle is:
  - Detected using contour approximation.
  - Rotated to a horizontal (0°) position.
  - Cropped and pasted back at its original location on a clean white background.

---

## 🔧 Requirements

- Python 3.x
- OpenCV
- NumPy

Install dependencies using:

```bash
pip install opencv-python numpy
*****************************************************************************************
🚀 Usage
Clone the repository and navigate into the project folder.

bash
Copy
Edit
git clone https://github.com/your-username/Task_rectangles.git
cd Task_rectangles
Add your input image as rectangles.png in the project directory.

Run the script:

bash
Copy
Edit
python rectangle_alignment.py
The output image will be saved as clean_upright_rectangles.png and displayed in a window.

⚙️ How the Code Works
1) Load the Image
The script reads the input image (rectangles.png) using OpenCV.

2)Edge Detection
The image is converted to grayscale and passed through a Canny edge detector to identify prominent edges.

3)Contour Detection

External contours are identified using cv2.findContours.

The script filters out non-rectangular shapes by approximating contours and checking for four corners and sufficient area.

4)Rectangle Rotation & Cropping
For each detected rectangle:

The minimum-area bounding box and its angle are found using cv2.minAreaRect().

If the rectangle is not horizontal, it is rotated using an affine transformation (cv2.getRotationMatrix2D and cv2.warpAffine).

The rotated rectangle is cropped from the image.

It is then pasted onto a white background image in the same position as the original.

5)Output Generation
The result is written to a new image file (clean_upright_rectangles.png) and displayed using OpenCV.

