import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

image_path = "/Users/ellenhart/Desktop/University of Richmond/Research AI/image1.jpg"
img = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# OCR (extract text)
text = pytesseract.image_to_string(gray)

# Edge detection (for lines, bars, etc.)
edges = cv2.Canny(gray, 50, 150)

# Show extracted text
print("Text in graph image:")
print(text)
