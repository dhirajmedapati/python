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
    
# Nested Loops - Math Table 
for outer in range(1,4):
    for inner in range(1,4):
        print(f"{outer} X {inner} = {outer * inner}")
    print("-----------")

outer = 1
while outer < 4:
    inner = 1
    while inner < 4:
        print(f"{outer} X {inner} = {outer * inner}")
        inner+=1
    print("-----------")
    outer+=1
        
    
    