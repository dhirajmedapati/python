# Sets

# empty sets
empty_set = {}
print(type(empty_set))

# empty sets with class
empty_set = set()
print(type(empty_set))
print(empty_set)

# num set (unordered)
num_set = {10,20,30,40,50}
print(num_set) # {50, 20, 40, 10, 30}
text_set = {"one","two","four"}
print(text_set) # {'one', 'two', 'four'}
mixed_set = {10,20,30,40,50,"one","two","four"}
print(mixed_set) # {'two', 'four', 40, 10, 50, 20, 'one', 30}

num_set = {10,20,30,40,50,10,20}
print(num_set) # removed duplicates

# print(num_set[0]) # TypeError: 'set' object is not subscriptable

num_set = {10,20,30,40,50}
print(num_set)
print(num_set)


list_data = list(num_set)
list_data.sort()
print(list_data[-1])

# operation on sets 
num_set = {10,20,74,43,50}
print(num_set)
# see if the element is even 

# loops will work 
for num in num_set:
    if num % 2 == 0:
        print(num)
        
print(dir(num_set))

