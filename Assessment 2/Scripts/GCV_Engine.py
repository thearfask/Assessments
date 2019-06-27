import io
import os

from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()

def detect_text(filename):
	#Output file
	OP_textfile = f"{filename}"
	OP_textfile = f'../TEXT_OP/{OP_textfile}.txt'
	OP_charread = f"../Input/{filename}"

	file_op = open(OP_textfile, 'w+')
	with io.open(OP_charread, 'rb') as image_file:
		content = image_file.read()
		image = vision.types.Image(content=content)
		response = client.text_detection(image=image)
		texts = response.text_annotations
		for text in texts:
			file_op.write(text.description)
	file_op.close()
	return OP_textfile