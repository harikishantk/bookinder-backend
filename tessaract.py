import tesserocr
from PIL import Image
import isbnlib

print(tesserocr.tesseract_version())  # print tesseract-ocr version
print(tesserocr.get_languages())  # prints tessdata path and list of available languages

image = Image.open('static/images/isbn2.jpeg')
text = tesserocr.image_to_text(image)
print(tesserocr.image_to_text(image))  # print ocr text from image
# or
# print(tesserocr.file_to_text('static/images/isbn.jpeg'))

isbn = isbnlib.get_isbnlike(text, level='normal')
print(isbn)