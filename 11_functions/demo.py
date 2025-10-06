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