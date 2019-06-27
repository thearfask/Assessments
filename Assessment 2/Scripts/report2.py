import GCV_Engine
import re
import json

file_name__REPORT = 'report2.jpg'

file_op = GCV_Engine.detect_text(file_name__REPORT)

dict_data = {}

with open(file_op, 'r') as f:
	data = f.read().replace('\n', ' ')
	match = re.search(r'Patient Name (.*?) Age', data)
	if match == None:
		dict_data['Name'] = None
	else:
		Name = match.group(1)
		dict_data['Name'] = Name

	match = re.search(r'Age (.*?) Ref', data)
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



	dict_data['HAEMATOLOGY INVESTIGATION'] = []
	match = re.search(r"Neutrophils (.*?) G% ", data)
	if match == None:
		neutrophil = {'Neutrophils': None}
		dict_data['HAEMATOLOGY INVESTIGATION'].append(neutrophil)
	else:
		ne = match.group(1)
		neutrophil = {'Neutrophils': f"{ne} G%"}
		dict_data['HAEMATOLOGY INVESTIGATION'].append(neutrophil)

	match = re.search(r"4000-10 (.*?) Imm3 ", data)
	if match == None:
		tlc = {'Total Leucocyte Count': None}
		dict_data['HAEMATOLOGY INVESTIGATION'].append(tlc)
	else:
		tl = match.group(1)
		tlc = {'Total Leucocyte Count': f"{tl} /mm3"}
		dict_data['HAEMATOLOGY INVESTIGATION'].append(tlc)



	dict_data['SEROLOGICAL INVESTIGATION'] = []
	match = re.search(r"SEROLOGICAL INVESTIGATION (.*?) HBs Ag ", data)
	if match == None:
		hbs = {'HBs Ag': None}
		dict_data['SEROLOGICAL INVESTIGATION'].append(hbs)
	else:
		hbs = match.group(1)
		hb = {'HBs Ag': f"{hbs}"}
		dict_data['SEROLOGICAL INVESTIGATION'].append(hb)

	match = re.search(r"HBs Ag (.*?) HCV ", data)
	if match == None:
		hbs = {'HCV': None}
		dict_data['SEROLOGICAL INVESTIGATION'].append(hbs)
	else:
		hbs = match.group(1)
		hb = {'HBs Ag': f"{hbs}"}
		dict_data['SEROLOGICAL INVESTIGATION'].append(hb)



	dict_data['RENAL PROFILE'] = []
	match = re.search(r"mg/d (.*?) Blood Urea ", data)
	if match == None:
		hbs = {'Blood Urea': None}
		dict_data['RENAL PROFILE'].append(hbs)
	else:
		hbs = match.group(1)
		hb = {'Blood Urea': f"{hbs}"}
		dict_data['RENAL PROFILE'].append(hb)

	match = re.search(r"Blood Urea (.*?) Serum Creatinine ", data)
	if match == None:
		hbs = {'Serum Creatinine': None}
		dict_data['RENAL PROFILE'].append(hbs)
	else:
		hbs = match.group(1)
		hb = {'RENAL PROFILE': f"{hbs}"}
		dict_data['RENAL PROFILE'].append(hb)


with open('../JSON_DATA/result2.json', 'w') as fp:
    json.dump(dict_data, fp)