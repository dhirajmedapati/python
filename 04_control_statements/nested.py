# Nested Conditionals

age = int(input("enter age "))
has_id = input("do you have an id yes/no ")

if age >=18:
    if has_id == "yes":
        print("you can vote ")
    else:
        print("you need an ID to vote ")
else:
    print("you are too young to vote ")