# Lists 

# empty list
empty_list = []
print(type(empty_list))
print(empty_list)

# store data 
num_list = [10,20,30,40,50]
print(num_list)

string_list = ["one","two","three"]
print(string_list)

mixed_data = [10,20,"one","two",3.5,9.0,True]
print(mixed_data)

single_value = [10]
print(single_value)

# Indexing

num_list = [10,20,30,40,50]
print(num_list)

print(num_list[0])
print(num_list[2])

print(num_list[-1])
print(num_list[-3])

# print(num_list[10]) # IndexError: list index out of range

# Slicing 
print(num_list[:])
print(num_list[::])
print(num_list[1:3:1])
print(num_list[1:5:2])

# access using for
num_list = [10,20,30,75,40,50]
print(num_list)

for num in num_list:
    print(num)
    
# perform operations on list elements
for num in num_list:
    if num % 2 == 0:
        print(num)

# operators
num_list = [10,20,30,40,50]
print(num_list)

for num in num_list:
    print(num * 5)
    

# using list class
empty_list = list()
print(type(empty_list))
print(empty_list)


num_list = list([10,20,30,40,50])
print(num_list)

num_list = [10,20,30,10,40,50,10]
print(num_list)

print(dir(num_list))