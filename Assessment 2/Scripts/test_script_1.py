import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name =  '../Input/report1.jpg'
# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
    image = vision.types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    for text in texts:
    	print(text.description)


# Performs label detection on the image file
# response = client.label_detection(image=image)
# labels = response.label_annotations
# print('Labels:')
# for label in labels:
#     print(label.description)