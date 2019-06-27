import json

def validate_name(name):
    if name.isdigit == True:
        print(f"Elth : {name} can't be a Name ;-D.. Please check and try again")
        return 1
    elif any(char.isdigit() for char in name):
        print(f"Elth : {name} can't be a Name ;-D.. Please check and try again")
        return 1
    else:
        user_registration['Last Name'] = name
        return 0

def get_gender():
    print(f"Elth : {questions[3]['options'][0]} | {questions[3]['options'][1]} ? \r\n ")
    Gender = input(f"You : ")
    if Gender.lower() == "male":
        Gender = "male"
        user_registration['Gender '] = Gender
        return 0
    elif Gender.lower() == "female":
        user_registration['Gender '] = Gender
        Gender = "female"
        return 0
    else:
        return 1

def validate_age(age):
    if age.isdigit()==False:
        print(f"Elth : {questions[5]['text']} \r\n")
        return 1
    elif int(age) > 99:
        print(f"Elth : {questions[5]['text']} \r\n")
        return 1
    else:
        user_registration['Age'] = age
        return 0

with open('JSON/assignment_1_input_1.json') as json_file:
    data = json.load(json_file)
    questions = data['questions']
    user_registration = {}
    while True:
        print(f"Elth : {questions[0]['instruction']} \r\n" )
        print(f"Elth : {questions[1]['text']} \r\n ")
        print(f"Elth : {questions[1]['var']}? \r\n")
        FirstName = input(f"You : ")
        while True:
            response = validate_name(FirstName)
            if response==1:
                FirstName = input(f"You : ")
            else:
                break

        print(f"Elth : {questions[2]['text']}\r\n")
        print(f"Elth : {questions[2]['var']}? \r\n")
        LastName = input(f"You : ")
        while True:
            response = validate_name(LastName)
            if response==1:
                LastName = input(f"You : ")
            else:
                break

        print(f"Elth : {questions[3]['text']} \r\n ")
        while True:
            response = get_gender()
            if response==0:
                break

        print(f"Elth : {questions[4]['text']} \r\n ")
        print(f"Elth : {questions[4]['var']}? \r\n")
        Age = input(f"You : ")
        while True:
            response = validate_age(Age)
            if response==1:
                Age = input(f"You : ")
            elif response == 0:
                break

        break
    print(f"Elth : {questions[6]['instruction']} \r\n")
    print(user_registration)
