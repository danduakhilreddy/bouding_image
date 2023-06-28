import cv2
import json
import pytesseract

# Load the image
image = cv2.imread('img.png')

# Load the JSON file
with open('akhil.json', 'r') as json_file:
    data = json.load(json_file)
# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform OCR on the grayscale image
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
result = pytesseract.image_to_data(gray_image, output_type=pytesseract.Output.DICT)

# Iterate over the text entries in the JSON data
for entry in data["text"]:
    text = entry
    print(text)
    # Search for the text in the OCR result
    for i in range(len(result['text'])):
        if result['text'][i].strip() == text.strip():
            # Extract the coordinates of the corresponding OCR result
            x, y, width, height = result['left'][i], result['top'][i], result['width'][i], result['height'][i]

            # Draw the bounding box on the image
            cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)
            break

# Display the image with bounding boxes
cv2.imshow('Image with Bounding Boxes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("image_with_marked_words.jpg", image)
   
