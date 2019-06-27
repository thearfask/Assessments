import GCV_Engine
import re


file_name__REPORT =  'report1.jpg'

file_op = GCV_Engine.detect_text(file_name__REPORT)

dict_data = {}

with open(file_op, 'r') as f:
	data = f.read().replace('\n', ' ')
	match = re.search(r'Name (.*?) Collected', data)
	if match == None:
		dict_data['Name'] = None
	else:
		Name = match.group(1)
		dict_data['Name'] = Name

	match = re.search(r'Age: (.*?) Gender', data)
	if match == None:
		dict_data['Age'] = None
	else:
		Age = match.group(1)
		dict_data['Age'] = Age
	

	match = re.search(r'Gender (.*?) Final', data)
	if match == None:
		dict_data['Gender'] = None
	else:
		Gender = match.group(1)
		dict_data['Gender'] = Gender
	

print(dict_data)