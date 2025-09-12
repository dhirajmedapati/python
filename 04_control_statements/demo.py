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


# using elif
# elif ladder style
age = 25

if age == 0 or age == 1 or age == 2 or age == 3 or age == 4:
   category = "Toddler"
elif age == 5 or age == 6 or age == 7 or age == 8 or age == 9 or age == 10 or age == 11 or age == 12:
   category = "Child"
elif age == 13 or age == 14 or age == 15 or age == 16 or age == 17 or age == 18 or age == 19:
   category = "Teenager"
elif age == 20 or age == 21 or age == 22 or age == 23 or age == 24 or age == 25 or age == 26:
   category = "Young Adult"
else:
   category = "Adult"

print(category) 

# match case style
age = int(input("Enter Age "))

match age:
   case 0 | 1 | 2 | 3 | 4:
       category = "Toddler"
   case 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12:
       category = "Child"
   case 13 | 14 | 15 | 16 | 17 | 18 | 19:
       category = "Teenager"
   case 20 | 21 | 22 | 23 | 24 | 25 | 26:
       category = "Young Adult"
   case _:
       category = "Adult"

print(category)