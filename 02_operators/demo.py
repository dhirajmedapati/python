# Arithmetic Operators 
num1 = 3
num2 = 2

print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2) # 1.5 -> round off
print(num1%num2) # modulus 

print(num1 // num2) 
print(num1 ** num2) # 3 ^ 2

# Compound Assignment Operators
num = 10
num = num + 5
print(num)

num = 10
num+=5 # (num + 5)
print(num)

num = 10
num*=5 # (num * 5)
print(num)

# increment means plus by 1 ++ doesn't support in python
# decrement means mins by 1 -- doesn't support in python

num = 10
num+=1 # increment
print(num)

num = 50
num-=1 # decrement
print(num)

# Comparison Operators 
num1 = 3
num2 = 2
num3 = 3

print(num1>num2)
print(num1<num2)
print(num1==num2)
print(num1==num3)

# Logical Operators 
a = 10
b = 5
c = 3
d = 2
 
res_and = a > b and c > d # T and T -> T
print(res_and)

res_or = a < b or c > d # F or T -> T
print(res_or)

res_not = a < b # F
print(not res_not) # T

# Membership Operators 
text ="python is easy"
is_z_present = "z" in text

is_z_present = "z" not in text
print(is_z_present)

list_nums = [10,20,30,40,50]
is_20_present = 20 in list_nums
print(is_20_present)

bank_customer_ids = [1029209,3039303,29202920]

# Identity Operators id() --> 
num1 = 10
num2 = 10
print(num1 is num2)

num1 = [10,20]
num2 = [10,20]
print(num1 is num2)

# Bitwise Operators
a = 5 # 0000000000000101
b = 3 # 0000000000000011
      # 0000000000000001

# & -> Sets each bit to 1 if both bits are 1

resultand = a & b  # 1
print(resultand)

# OR (|)- Sets each bit to 1 if one of bits is 1
a = 5 # 0000000000000101
b = 3 # 0000000000000011
      # 0000000000000111

resultor = a | b  # 7
print(resultor)      

