# Variables Allow You to

# 			-> Assign Data
# 			-> Retrieve Data
# 			-> Manipulate Data (If Required)

student_age = 30
student_name = "Ravi" 
student_gpa = 9.5
student_passed = True

# output / Retrieve
print(student_age)
print(student_name)
print(student_gpa)
print(student_passed)

# Dynamic Data
dynamic_variable = 30
print(type(dynamic_variable)) # type() : Specifies data type
print(id(dynamic_variable)) # id() : Returns Identity (address)
dynamic_variable = "Ravi" 
print(id(dynamic_variable))
print(type(dynamic_variable))
dynamic_variable = 9.5
print(id(dynamic_variable))
print(type(dynamic_variable))
dynamic_variable = True
print(id(dynamic_variable))
print(type(dynamic_variable))

# Why id()
a = 10
b = 20
c = 10
print(id(a))
print(id(b))
print(id(c))

# complex data List is multiple items - represented using []
list_nums_one = [10,20,30]
list_nums_two = [10,20,30]
print(type(list_nums_one))
print(type(list_nums_two))

print(id(list_nums_one))
print(id(list_nums_two))

print(id(list_nums_one[0]))
print(id(list_nums_two[0]))