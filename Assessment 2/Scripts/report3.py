import GCV_Engine
import re
import json

file_name__REPORT = 'report3.jpg'

file_op = GCV_Engine.detect_text(file_name__REPORT)
# file_op = '/home/arfaa/Downloads/AllSpartHealthLabs/Assessments/Assessment 2/TEXT_OP/report3.jpg.txt'
dict_data = {}

with open(file_op, 'r') as f:
	data = f.read().replace('\n', ' ')
	print(data)
	match = re.search(r'Patient Name (.*?) ECHS', data)
	if match == None:
		dict_data['Name'] = None
	else:
		Name = match.group(1)
		dict_data['Name'] = Name

	match = re.search(r'Age (.*?) Patient Name ', data)
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

	match = re.search(r'Ref By (.*?) Report', data)
	if match == None:
		dict_data['Ref By'] = None
	else:
		RefBy = match.group(1)
		dict_data['Ref By'] = RefBy

	dict_data['Blood Sugar'] = []

	match = re.search(r'BLOOD SUGAR (.*?) FASTING', data)
	if match == None:
		fasting = {'Fasting':None}
		dict_data['Blood Sugar'].append(fasting)
	else:
		BS = match.group(1)
		fasting = {'Fasting':BS}
		dict_data['Blood Sugar'].append(fasting)
	
	match = re.search(r'POSTPRANDIAL (.*?) RAMDOM', data)
	if match == None:
		POSTPRANDIAL = {'POSTPRANDIAL':None}
		dict_data['Blood Sugar'].append(POSTPRANDIAL)
	else:
		BS = match.group(1)
		POSTPRANDIAL = {'POSTPRANDIAL':BS}
		dict_data['Blood Sugar'].append(POSTPRANDIAL)


with open('../JSON_DATA/result3.json', 'w') as fp:
    json.dump(dict_data, fp)
