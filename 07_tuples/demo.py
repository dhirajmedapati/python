# tuples 

# empty tuple
empty_tuple = ()
print(type(empty_tuple))
print(empty_tuple)

empty_tuple = tuple()
print(type(empty_tuple))
print(empty_tuple)



# store data 
num_tuple = (10,20,30,40,50)
print(num_tuple)

string_tuple = ("one","two","three")
print(string_tuple)

mixed_data = (10,20,"one","two",3.5,9.0,True)
print(mixed_data)

single_value = (10)
print(single_value)

# Indexing

num_tuple = (10,20,30,40,50)
print(num_tuple)

print(num_tuple[0])
print(num_tuple[2])

print(num_tuple[-1])
print(num_tuple[-3])

# print(num_tuple[10]) # IndexError: tuple index out of range

# Slicing 
print(num_tuple[:])
print(num_tuple[::])
print(num_tuple[1:3:1])
print(num_tuple[1:5:2])

# access using for
num_tuple = (10,20,30,75,40,50)
print(num_tuple)

for num in num_tuple:
    print(num)
    
# perform operations on tuple elements
for num in num_tuple:
    if num % 2 == 0:
        print(num)

# operators
num_tuple = (10,20,30,40,50)
print(num_tuple)

for num in num_tuple:
    print(num * 5)
    

# using tuple class
empty_tuple = tuple()
print(type(empty_tuple))
print(empty_tuple)


num_tuple = tuple((10,20,30,40,50))
print(num_tuple)

num_tuple = (10,20,30,10,40,50,10)
print(num_tuple)

print(dir(num_tuple))

num_list = (10,20,30,40,50,10,80,10)
print(num_list)
count = num_list.count(10)
print(count)

# index() : returns index position of specified value
num_list = (10,20,30,40,50)
print(num_list)
position = num_list.index(30)
print(position)