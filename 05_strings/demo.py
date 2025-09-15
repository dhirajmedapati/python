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

# Slicing 