# Strings 
s1 = 'hello' # single line string 
print(s1)

s2 = "hello" # single line string
print(s2)

s3 = '''hello'''
print(s3)

s4 = """hello"""
print(s4)

# multi line string we use ''' or """
# multi_line = "line one
# line two
# line three"
# print(multi_line)

multi_line = '''line one
line two
line three'''
print(multi_line)

multi_line = """line one
line two
line three"""
print(multi_line)

# how to use single or double quote within string
question = "how are you ?"
# answer = 'i'm fine'
answer = "i'm fine"
print(answer)

answer = 'i"m fine'
print(answer)

answer = """ i'm fine i"m fine """
print(answer)

# access whole string
text  = "python"
print(text)

# access first character in string
print(text[0])
print(text[2])
print(text[-4])

# access index that is out of range
# print(text[10]) # IndexError: string index out of range

# length of string
print(len(text))

# range(start, stop, step)

# Slicing : extract portion of string
# slice[start:stop:step]
text = "python"
print(text[:]) # python
print(text[::]) # python
print(text[1:3]) # yt
print(text[2:]) # ython
print(text[:4]) # pyth
print(text[0:3:1]) # pyt  start:stop:step
print(text[0:5:2]) # pto

    #  0  1  2   3  4  5 (Positive Index)
	#  p  y  t   h  o  n
	# -6 -5  -4 -3  -2 -1 (Negative Index)

print(text[-4:-1]) # tho
print(text[-4:-1:1]) # tho
print(text[-4:-1:-1]) # empty
print(text[-4:-6:-1]) # ty

# string repetition
laugh = "HaHa"
print(laugh)
hard_laugh = "HaHaHaHaHaHaHaHaHaHaHaHaHaHaHaHa"
print(hard_laugh)

hard_laugh = laugh * 10
print(hard_laugh)

# String Concatenation
first_name = "Ravi"
last_name = "Krishna"
full_name = first_name + last_name
print(full_name)

# String Methods 

# simulate gmail like functionality
email = input("Enter Your Email ID: ")
format_email = email.lower() + "@gmail.com"
print("User Given ID: "+email)
print("Gmail Auto Format ID: "+format_email)

# simulate PAN functionality
pan = input("Enter Your PAN ID: ")

if pan.isalnum():
    format_pan = pan.upper()
    print("User Given PAN: "+pan)
    print("Formatted PAN: "+format_pan)
else:
    print("User Given PAN is Invalid: "+pan)
    
# validate email : ravi@gmail.com --> ravigmail.com
email = input("Enter Your Email ID: ")
if email.find("@") != -1:
    print("valid email")
else:
    print("invalid email")
    
if "@" in email:
    print("valid email")
else:
    print("invalid email")
    
# redirect operator based on country code
phone_number = input("Enter Phone Number with IS Code: ")
if phone_number.startswith("+1"):
    print("Call Connected To USA")
elif phone_number.startswith("+91"):
    print("Call Connected To India")
else:
    print("ISD available only to USA & India")
    
# check if email sync is possible

