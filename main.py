import json


# Load JSON data from file
with open('akhil.json', 'r') as json_file:
    data = json.load(json_file)

# Extract the value of the desired key
key_value = data['text']
import cv2

# Load the given image
image = cv2.imread('img.png')
# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

import pytesseract
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
# Perform text detection
text = pytesseract.image_to_string(gray_image)
import re

# Find the bounding box coordinates for the words matching the key value
for key in key_value:
    matches = re.finditer(r'\b{}\b'.format(re.escape(key)), text, flags=re.IGNORECASE)




bounding_boxes = []
for match in matches:
    start = match.start()
    end = match.end()

    # Perform word tokenization to get the position of the matched words
    words = text[:start].split()
    word_positions = sum(len(word) for word in words) + len(words)

    # Find the bounding box coordinates based on the word positions
    (x, y, width, height), _ = pytesseract.image_to_boxes(gray_image)
    x_start, y_start, x_end, y_end = _, _, _, _
    for i, (x_pos, y_pos) in enumerate(zip(x, y)):
        if i == word_positions:
            x_start, y_start = x_pos, y_pos
        elif i == word_positions + len(key_value):
            x_end, y_end = x_pos, y_pos
            break

    bounding_boxes.append((x_start, y_start, x_end, y_end))
# Mark the bounding boxes on the original image
for (x_start, y_start, x_end, y_end) in bounding_boxes:
    cv2.rectangle(image, (x_start, y_start), (x_end, y_end), (0,0,255), 2)
# Display the marked image
cv2.imshow("Image with Marked Words", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the marked image
cv2.imwrite("image_with_marked_words.jpg", image)
