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

for entry in data["text"]:
    # Extract the text
    text = entry

    # Split the text into individual words
    words = text.split()

    # Initialize the bounding box coordinates for the entire text
    min_x, min_y, max_x, max_y = float('inf'), float('inf'), 0, 0

    # Search for each word in the OCR result
    for word in words:
        for i in range(len(result['text'])):
            if result['text'][i].strip() == word.strip():
                # Extract the coordinates of the corresponding OCR result
                x, y, width, height = result['left'][i], result['top'][i], result['width'][i], result['height'][i]
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                max_x = max(max_x, x + width)
                max_y = max(max_y, y + height)
                break

            # Draw the bounding box on the image
    cv2.rectangle(image, (min_x, min_y), (max_x, max_y), (0, 255, 0), 2)



# Iterate over the text entries in the JSON data


# Display the image with bounding boxes
cv2.imshow('Image with Bounding Boxes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("image_with_marked_words.jpg", image)
   
