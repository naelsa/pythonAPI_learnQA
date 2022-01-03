import json

string_as_json_format = '{"answer": "Hello, User"}'
obj = json.loads(string_as_json_format)
print(obj['answer'])

#KeyError
#string_as_json_format = '{"answer": "Hello, User"}'
#obj_2 = json.loads(string_as_json_format)
#print(obj_2['answer2'])

#Улучшаем читаемость
string_as_json_format = '{"answer": "Hello, User"}'
obj_3 = json.loads(string_as_json_format)

key = "answer2"

if key in obj_3:
    print(obj_3[key])
else:
    print(f"Кдюч {key} в JSON отсутствует")
