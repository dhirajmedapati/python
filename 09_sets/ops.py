# Set Operations

# add() : add element to set
s1 = {10,20,30,40,50}
print(s1)
# s1.add() # TypeError: set.add() takes exactly one argument (0 given)
s1.add(60)
print(s1)

# s1.add(70,80,"b") # TypeError: set.add() takes exactly one argument (3 given)
s1.add("b")
print(s1)

# update() : add multiple elements to set
s1 = {10,20,30,40,50}
print(s1)
s1.update([60,70,80])
print(s1)

# remove() : remove element, if not found error
s1 = {10,20,30,40,50}
print(s1)
# s1.remove() # TypeError: set.remove() takes exactly one argument (0 given)
s1.remove(20)
print(s1)

s1 = {10,20,30,40,50}
print(s1)
# s1.remove(60) # KeyError
print(s1)

# discard() : remove element, if not found no error
s1 = {10,20,30,40,50}
print(s1)
# s1.discard() # TypeError: set.discard() takes exactly one argument (0 given)
s1.discard(20)
s1.discard(60)
print(s1)

# pop() : removes random element 
s1 = {10,20,30,40,50}
print(s1)
s1.pop()
print(s1)

# clear() : empties set
s1 = {10,20,30,40,50}
print(s1)
s1.clear()
print(s1)

# NOTE : Sets are Mutable (add, clear)

# copy() : create a shallow copy
s1 = {10,20,30,40,50}
print(s1)
backup = s1.copy()
backup.add(60)
print(s1)
print(backup)

# soft copy 
s1 = {10,20,30,40,50}
print(s1)
backup = s1
print(backup)
backup.add(60)
print(s1)
print(backup)

# set related math ops
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

# union() : combines elements from both sets
print(s1.union(s2))
print(s1 | s2)

# intersection() : get common elements 
print(s1.intersection(s2))
print(s1 & s2)
print(s1)
print(s2)

# intersection_update() : get common elements, also update calling set 
print(s1.intersection_update(s2))
print(s1)
print(s2)

s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

# difference() : removes elements which also occur in other sets
print(s1.difference(s2))
print(s1-s2)
print(s2-s1)
print(s1)
print(s2)

# difference_update() : removes elements which also occur in other sets and update calling set
print(s1.difference_update(s2))
print(s1)
print(s2)

# symmetric_difference() : removes elements and takes the combined elements left in both sets
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

print(s1.symmetric_difference(s2))
print(s1 ^ s2)
print(s1)
print(s2)

# symmetric_difference_update() : removes elements and takes the combined elements left in both sets, updates calling set
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

print(s1.symmetric_difference_update(s2))
print(s1)
print(s2)

# issubset() : check if given set is subset of another set
s1 = {10,20,30,40,50}
s2 = {40,50}
s3 = {60,70,80}

print(s2.issubset(s1))
print(s2.issubset(s3))

# issuperset() : check if given set is superset of another set
print(s1.issuperset(s2))
print(s2.issuperset(s3))

# isdisjointset() : checks if two sets no common elements 
s1 = {10,20,30,40,50}
s2 = {40,50}
s3 = {80,90}

print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))

my_data = {10,20,30,40}
readable_only = tuple(my_data)
print(type(readable_only))
print(readable_only)

# fronzenset
fs = frozenset({10,20,30,40})
print(type(fs))
print(dir(fs))