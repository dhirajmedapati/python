# Datatypes

# Numeric Types
data = 10
print(type(data))
data = 10.5
print(type(data))
data = 3 + 5j
print(type(data))

# Text Type is String
data = "Hello"
print(type(data))

# Boolean Type
data = True
print(type(data))

# Complex Data Types (can hold multiple values)

# List (homogeneous)
emp_ids = [101,102,103,104]
print(type(emp_ids))

# Tuple (heterogenous)
emp = (101,"Ravi",30,"Hyd")
print(type(emp))

# Set 
emp_ids = {101,102,103,104}
print(type(emp_ids))

# Dictionary
emp_info = {"name":"Ravi", "age":25, "city":"hyd"}
print(type(emp_info))

# None type
x = None
print(type(x))

# User defined Datatype
class Student:
    pass
edify_student = Student()
print(type(edify_student))

# Type Conversion
a = 10 # int 
b = 3.5 # float 
c = a + b # float
print(type(c))

# Type Casting
pi = 3.14 # float 
print(type(pi))
pi_round_int = int(pi) 
print(pi_round_int)
print(type(pi_round_int))

rating = "5" # String
rating_int = int(rating)
# print(rating+5)
print(rating_int+5)

# incompatible conversion 
# rating = "five"
# rating_int = int(rating) # ValueError: invalid literal for int() with base 10: 'five'
