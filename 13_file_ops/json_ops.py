# Working with JSON Data 

student = {
   "id": 101,
   "name": "Ravi",
   "course": "Python Full Stack",
   "skills": ["Python", "Git", "AWS"],
   "score": 89.5
}

print(type(student))

# Write the Data to JSON file 
import json

with open("13_file_ops/student.json","w") as file_data:
    json.dump(student,file_data)
    
# Write the Data to JSON file with indentation
import json
with open("13_file_ops/student.json","w") as file_data:
    json.dump(student,file_data,indent=4)
    
# Reading the Data from JSON file 
import json
with open("13_file_ops/student.json","r") as file_data:
    json_reader = json.load(file_data)
print(json_reader)
print(type(json_reader))
print(json_reader["name"])

# check with condition
if json_reader["score"] >= 75:
    print(f"{json_reader["name"]} Passed")
else:
    print(f"{json_reader["name"]} Failed")
    
    
student = {
   "id": 101,
   "name": "Ravi",
   "course": "Python Full Stack",
   "skills": ["Python", "Git", "AWS"],
   "score": 89.5
}

print(type(student))

python_object = json.dumps(student)
print(python_object)

json_string = '{"id": 101, "name": "Ravi", "course": "Python Full Stack", "skills": ["Python", "Git", "AWS"], "score": 89.5}'
print(type(json_string))

python_dict = json.loads(json_string)
print(python_dict)
print(type(python_dict))

# Working with user api
# https://dummyjson.com/users
import urllib.request
url = "https://dummyjson.com/users"

response = urllib.request.urlopen(url)

print(response)
print(type(response))

data = response.read()
print(data)
print(type(data))

parsed_data = json.loads(data)
print(parsed_data)
print(type(parsed_data))

# Extract users 
users = parsed_data["users"]
print(users)

for user in users:
    print(user["username"])
print("==============")    
for user in users:
    if user["age"] < 25:
        print(user["username"])