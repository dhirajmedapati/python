# Dictionaries

empty_dict = {}
print(type(empty_dict))
print(empty_dict)

# this is not dict, but a set
dict_data = {1,2,3,4,5}
print(type(dict_data))

# nums 
dict_nums = {1:10,2:20,3:30}
print(type(dict_nums))
print(dict_nums)

dict_text = {"one":"1","two":"two"}
print(dict_text)

dict_mixed = {1:10,2:"two","two":"two"}
print(dict_mixed)

# duplicates 
dict_data = {1:10,2:20,3:30}
print(dict_data)

# key duplicate 
dict_data = {1:10,2:20,3:30,2:200}
print(dict_data)

# value duplicate
dict_data = {1:10,2:20,3:30,4:20}
print(dict_data)

# keys should be immutable only
# dict_data = {[10]:"ten"}
dict_data = {(10):"ten"}
print(dict_data)

# students info / order info / etc
students = {
   "101": {
       "name": "Ravi",
       "email": "ravi@gmail.com",
       "course": "Python"
   },
   "102": {
       "name": "Anjali",
       "email": "anjali@gmail.com",
       "course": "Java"
   },
   "103": {
       "name": "John",
       "email": "john@yahoo.com",
       "course": "DevOps"
   }
}

print(students)

dict_data = {1:10,2:20,3:30,4:40}
print(dict_data)

# accessing 
# print(dict_data[0]) # KeyError: 0
print(dict_data[2])

# print(students[101]) # KeyError: 101
print(students["101"]) 
print(students["101"]["email"]) 

id = "103"
if students[id]["email"].endswith("@gmail.com"):
    print("Using Gmail")
    
# using class
dict_data = dict({1:10,2:20,3:30,4:40})
print(dict_data)

# loops will give only key
for data in dict_data:
    print(data)

for data in dict_data:
    print(dict_data[data])
    
print(dir(dict_data))