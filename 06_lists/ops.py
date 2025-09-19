# List Methods : List Operations

num_list = [10,20,30,40,50]
print(num_list)

# append() : adds an element to end of the list 
# num_list.append() # TypeError: list.append() takes exactly one argument (0 given)
num_list.append(60)
print(num_list)

num_list.append([70,80,90])
print(num_list)

# extend() : takes an iterable and adds individually
num_list = [10,20,30,40,50]
print(num_list)

# num_list.extend(60) # TypeError: 'int' object is not iterable
num_list.extend([60,70,80,90])
print(num_list)

# insert() : allows you to insert element at specific position
num_list = [10,20,40,50]
print(num_list)
num_list.insert(2,30)
print(num_list)


num_list.insert(10,[60,70,80])
print(num_list)

num_list[0] = 5
print(num_list)

# pop() : removes an element at last by default
num_list = [10,20,30,40,50]
print(num_list)
num_list.pop()
print(num_list)

num_list.pop(2)
print(num_list)

# num_list.pop(10) # IndexError: pop index out of range
print(num_list)

# remove() : removes an element based on value not index 
num_list = [10,20,30,40,50]
print(num_list)

# num_list.remove(0) # ValueError: list.remove(x): x not in list
num_list.remove(10)
print(num_list)

num_list = [10,20,30,40,10,50,10]
print(num_list)

for num in num_list:
    if num == 10:
        num_list.remove(num)
    print(num_list)

num_list = [10,20,30,40,10,50,10]
print(num_list)
while 10 in num_list:
    num_list.remove(10)
print(num_list)

# clear() : removes all elements nad empties list
num_list = [10,20,30,40,50]
print(num_list)
num_list.clear()
print(num_list)

# NOTE : with above methods we can say Lists can be modified (Lists are Mutable)

# index() : returns index position of specified value
num_list = [10,20,30,40,50]
print(num_list)
position = num_list.index(30)
print(position)

# position = num_list.index(80) # ValueError: 80 is not in list
print(position)

# count() : gives the count how many times a element is repeated
num_list = [10,20,30,40,50,10,80,10]
print(num_list)
count = num_list.count(10)
print(count)

# reverse() : reversed the elements 
num_list = [10,20,30,40,50]
print(num_list)
num_list.reverse()
print(num_list)

# sort() : sorts the elements 
num_list = [10,30,20,50,40]
print(num_list)
num_list.sort() # default is ascending
print(num_list)

num_list.sort(reverse=True) # descending order 
print(num_list)

test_list = ["apple","f","car","e"]
test_list.sort()
print(test_list)

# copy() : make a backup/shallow copy
num_list = [10,30,20,50,40]
print(num_list)

backup_num_list = num_list.copy()
print(backup_num_list)

backup_num_list.append(60)
print(num_list)
print(backup_num_list)

# soft copy(=) 
num_list = [10,30,20,50,40]
print(num_list)

backup_num_list = num_list
print(backup_num_list)

backup_num_list.append(60)
print(num_list)
print(backup_num_list)