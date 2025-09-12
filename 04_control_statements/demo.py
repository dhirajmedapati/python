# Control Structures 

# Conditional Statements

# Indentation
if 5 > 2:
# print("Incorrect Indentation")
# IndentationError: expected an indented block after 'if' statement on line 8
    print("Yes thats true")
    print("Correct Indentation")  
#  print("Incorrect Indentation")  
 # IndentationError: unindent does not match any outer indentation level 

if True:
    print("This is Good")
    print("This is also good")
print("This is also also good")

# If Statement
num = 10
if num > 0:
    print("Number is Positive")
    
num = -10
if num > 0:
    print("Number is Positive")

# check if the given number is in the range 10 to 20
num = 25
# 10 to 20
if 10 <= num <=20: # if num >= 10 and num <=20
    print(f"{num} is in range of 10 to 20") 
    
# if else Statement
# if condition:
    # statement
# else:
    # statement       
print("if else")
num = -10
if num > 0:
    print("Number is Positive")
else:
    print("Number is Negative")
    
# voting app
age = 12
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
    
# input() -> take input
variable = input("Enter Something: ")
print(f"You have given this input: {variable}")

name = input("Enter Your Name: ")
print(f"Welcome {name}")

# voting app with input()
# age = input("Enter Your Age: ")
age = int(input("Enter Your Age: "))
if age >= 18: 
    # TypeError: '>=' not supported between instances of 'str' and 'int'
    print("You can vote")
else:
    print("You cannot vote")

# vote app using ternary operator
age = int(input("Enter Your Age: "))
# value_if_true if condition else value_if_false
status = "You can vote" if age >= 18 else "You cannot vote"
print(status)

#elif

marks = int(input("enter your marks "))
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >=60:
    print("C")
else:
    print("fail")
