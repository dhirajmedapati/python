# Dictionary Operations
dict_data = {1:10,2:20,3:30,4:40}
print(dict_data)

# update() : adds / updates dict 
dict_data.update()
dict_data.update({5:50})
print(dict_data)

dict_data.update({3:300})
print(dict_data)

# pop() : remove item 
dict_data = {1:10,2:20,3:30,4:40}
print(dict_data)
# dict_data.pop() # TypeError: pop expected at least 1 argument, got 0
dict_data.pop(2) 
print(dict_data)

# dict_data.pop(5) # KeyError: 5
print(dict_data)

# popitem() : remove last item 
dict_data = {1:10,2:20,3:30,4:40}
print(dict_data)
dict_data.popitem()
print(dict_data)

# clear() : empties dict 
dict_data = {1:10,2:20,3:30,4:40}
print(dict_data)
dict_data.clear()
print(dict_data)

# get() : used to get value by key 
dict_data = {1:10,2:20,3:30,4:40}
print(dict_data)
print(dict_data[1])
# print(dict_data[5]) # KeyError: 5
print(dict_data.get(1)) # TypeError: get expected at least 1 argument, got 0
print(dict_data.get(5)) # None, no error 

# keys() : returns keys 
dict_data = {1:10,2:20,3:30,4:40}
print(dict_data)
dict_data.keys()
print(dict_data.keys())
keys = dict_data.keys()
for k in keys:
    print(k)
    
# values() : returns values 
dict_data = {1:10,2:20,3:30,4:40}
print(dict_data)
dict_data.values()
print(dict_data.values())
values = dict_data.values()
for v in values:
    print(v)
    
# items() : returns both key & values
dict_data = {1:10,2:20,3:30,4:40}
print(dict_data)
mydata = dict_data.items()
print(dict_data.items())

# fromkeys() : Create a new dictionary with keys from iterable and values set to value.
dict_data = {1:10,2:20,3:30,4:40}
print(dict_data)
dict_data.fromkeys(values)
print(dict_data.fromkeys(values))
print(dict_data.fromkeys(mydata))

# copy() : create shallow copy
dict_data = {1:10,2:20,3:30,4:40}
print(dict_data)
backup = dict_data.copy()
print(backup)


dict_data = {1:10,2:20,3:30,4:40}
updated_key = dict_data.update({5:50})
print(updated_key)
print(dict_data)

# setdefault() : 
dict_data = {1:10,2:20,3:30,4:40}
print(dict_data)
updated_key = dict_data.setdefault(5,50)
print(updated_key)
print(dict_data)