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

# variables
x = "python "
y = "is "
z = "easy"

# o/p - python is easy
# print(xyz) # NameError: name 'xyz' is not defined
print(x+y+z) # Concatenation : Joining Strings

x = 10
y = 20
z = 30
print(x+y+z) 

# req : combine multiple types of data
name = "Ravi"
age = 20
# o/p - My name is Ravi and my age is 20
# print("My name is "+name+ " and my age is "+age) # TypeError: can only concatenate str (not "int") to str
# print("My name is ",name +" and my age is ",age, +" and after 5 years my age is ", age+5) # TypeError: bad operand type for unary +: 'str'
print(f"My name is {name} and my age is {age}") # Interpolation new style python
print(f"My name is {name} and my age is {age} and after 5 years my age is  {age+5}") # Interpolation new style python


x,y,z = 10,20,30
print(x)
print(y)
print(z)

# LHS = RHS
# x,y,z = 10,20,30,40 # ValueError: too many values to unpack (expected 3)
print(x)
print(y)
print(z)

# multiple values assigned
a = 10
b = 20
c = 10
d = 10

a = c = d = 10
print(a)
print(c)
print(d)