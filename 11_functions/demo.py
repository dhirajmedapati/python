# Without Functions

a = 10
b = 5

# math ops
print(a+b)
print(a-b)
print(a*b)
print(a/b)

a = 20
b = 10

print(a+b)
print(a-b)
print(a*b)
print(a/b)

# with function
def math_ops():
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)	

a = 10
b = 5
math_ops()
a = 20
b = 10
math_ops()
a = 200
b = 100
math_ops()

print("="*10)

# functions with parameters
def math_ops(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)	
    
# math_ops() # TypeError: math_ops() missing 2 required positional arguments: 'a' and 'b'
math_ops(10,5)
math_ops(20,10)
math_ops(200,100)

# Positional arguments
def login_fun(username,password):
    if username == "admin" and password == "password":
        print("Login Success")
    else:
        print("Login Failed")
        
login_fun("password","admin")    
login_fun("admin","password")  
# login_fun() # TypeError: login_fun() missing 2 required positional arguments: 'username' and 'password'
# login_fun("password")  # TypeError: login_fun() missing 1 required positional argument: 'password'

# employee info 
def emp_info(emp_name,emp_email,emp_loc):
    print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_loc}")
    
emp_info("hyd","ravi","ravi@gmail.com")
emp_info("krishna","krishna@gmail.com","hyd")

# Keyword arguments

# employee info 
def emp_info(emp_name,emp_email,emp_loc):
    print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_loc}")
    
emp_info(emp_loc="hyd",emp_name="ravi",emp_email="ravi@gmail.com")

# Default arguments

# employee info 
def emp_info(emp_name,emp_email,emp_loc,comp_name="Google"):
    print(f"Hi {emp_name}, your email is {emp_email} working for {comp_name} and work location is {emp_loc}")
    
emp_info(emp_loc="hyd",emp_name="ravi",emp_email="ravi@gmail.com")
emp_info(emp_loc="california",emp_name="john",emp_email="john@gmail.com")

emp_info(emp_loc="berlin",emp_name="suey",emp_email="suey@gmail.com",comp_name="META")

# Arbitrary Positional arguments (*args)

def info(*info):
    print(info)

info("ravi")
info("ravi","ravi@gmail.com")

def add_numbers(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    print(f"Total is {total}")

add_numbers(10)    
add_numbers(10,20)   
add_numbers(10,20,30,40,50)   


# Arbitrary Keyword arguments (**kwargs)
def profile_info(**info):
    print(info)
    
profile_info(name="ravi")
profile_info(name="ravi",email="ravi@gmail.com")

def transactions(**trans):
    print(trans)
    total = 0
    for tran in trans:
        print(tran)

transactions(oct=1000,nov=2000,dec=3000)

# In dict we saw same behavior, only keys by default 

# if we have access to key then we can get values
def transactions(**trans):
    print(trans)
    total = 0
    for tran in trans:
        print(trans[tran])

transactions(oct=1000,nov=2000,dec=3000)

# Using both to build some functional app
def transactions(**trans):
    print(trans)
    total = 0
    for tran in trans:
        # print(trans[tran])
        total = total + trans[tran]
    print(f"You have done {len(trans)} which amounts to a total of {total}")

transactions(oct=1000,nov=2000,dec=3000) 

# Without return 
def add(a,b):
    a+b
    
add(10,20)
print(add(10,20))

# With return 
def add(a,b):
    return a+b

add(10,20)
print(add(10,20))

def sub(c,d,e): # add c&d -> r - e
    return add(c,d) - e

print(sub(3,4,5))

# With return as last statement
def add(a,b):
    return a+b
    print("let's see if the execution reaches here")

print(add(10,20))

# With multiple returns
def math_ops(a,b):
    return a+b
    return a-b
    return a*b

print(math_ops(10,20))

# With multiple returns
def math_ops(a,b,opr):
    if opr == "+":
        return a+b
    elif opr == "-":
        return a-b
    elif opr == "*":
        return a*b
    else:
        return "Invalid Operator"
    
print(math_ops(10,20,"*"))

# Local Scope 
def add():
    # local variables
    la = 10
    lb = 20
    print(la)
    print(lb)
    
add()
# print(la) NameError: name 'la' is not defined. Did you mean: 'a'?

# Local Scope 
def add(la,lb):
    # local variables
    print(la)
    print(lb)
    
add(10,5)
# print(la) NameError: name 'la' is not defined. Did you mean: 'a'?

# global variable
ga = 30

def add(la,lb):
    # local variables
    print(la)
    print(lb)
    print(ga)

add(10,5)    
print(ga)

# global variable
ga = 30

# name conflict
def add(la,lb,ga):
    # local variables
    print(la)
    print(lb)
    print(ga)
    print(globals()['ga'])

add(10,5,2)    


# global variable
count = 0
def increment():
    global count
    count += 1

increment()
print(count)

# without lambda
def add(a,b):
    return a+b
print(add(2,4))

# lambda arguments: expression 
print((lambda a,b: a+b)(2,4))

# without lambda
def is_num_even(num):
    if num % 2 == 0:
        return True 
    else:
        return False

print(is_num_even(5))
print(is_num_even(10))

print((lambda num: num % 2 == 0)(3))

print((lambda num: "Positive" if num > 0 else "Negative" if num < 0 else "Zero")(0))

def emp_info(emp_name,emp_email,emp_loc):
    print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_loc}")
    
emp_info = lambda emp_name,emp_email,emp_loc: print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_loc}")
emp_info("ravi","ravi@gmail.com","hyd")

# without map()
# write a script to take a list of numbers and return square of list of numbers
# [1,2,3,4,5] => [1,4,9,16,25]
def square(nums):
    square_result= []
    for num in nums:
        square_result.append(num*num)
    return square_result

print(square([1,2,3,4,5]))
    

# with map()
# write a script to take a list of numbers and return square of list of numbers
# [1,2,3,4,5] => [1,4,9,16,25]
# map(function, iterable)
print(map(lambda num: num*num, [1,2,3,4,5]))
print(list(map(lambda num: num*num, [1,2,3,4,5])))

# without filter()
# write a script to take a list of numbers and return only even list of numbers
# [1,2,3,4,5,6,7,8,9,10] => [2,4,6,8,10]
def even(nums):
    even_result= []
    for num in nums:
        if num % 2 == 0:
            even_result.append(num)
    return even_result

print(even([1,2,3,4,5,6,7,8,9,10]))


# with filter()
# write a script to take a list of numbers and return only even list of numbers
# [1,2,3,4,5,6,7,8,9,10] => [2,4,6,8,10]
print(filter(lambda num: num%2 == 0, [1,2,3,4,5,6,7,8,9,10]))
print(list(filter(lambda num: num%2 == 0, [1,2,3,4,5,6,7,8,9,10])))


