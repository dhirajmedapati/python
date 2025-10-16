# Working with files

# Syntax - 1
file = open("13_file_ops/file.txt","r")
# print(file)
print(file.closed)
file.close()
print(file.closed)

# Syntax - 2 # recommended 
with open("13_file_ops/file.txt","r") as file_data:
    pass
    # print(file_data) 
print(file_data.closed)   

# Reading the data 
with open("13_file_ops/file.txt","r") as file_data:
    print(file_data.read())
    
# Reading the data -> character wise 
with open("13_file_ops/file.txt","r") as file_data:
    for char in file_data.read():
        print(char)

# Reading the data -> word wise 
with open("13_file_ops/file.txt","r") as file_data:
    for word in file_data.read().split():
        print(word)

# Reading the data -> line wise 
with open("13_file_ops/file.txt","r") as file_data:
    print(file_data.readline().strip())
    print(file_data.readline().strip())

# Reading the data -> read all lines  
with open("13_file_ops/file.txt","r") as file_data:
    print(file_data.readlines())
    
with open("13_file_ops/file.txt","r") as file_data:
    list_lines = file_data.readlines()
    for line in list_lines:
        print(line.strip())

# Write Data -> Create File (Write Mode "w")
with open("13_file_ops/new.txt","w") as file_data:
    print(file_data)

# Write Data -> Add content to file 
with open("13_file_ops/new.txt","w") as file_data:
    file_data.write("hello there")

# Write Data -> Add content to file multiple lines
with open("13_file_ops/new.txt","w") as file_data:
    file_data.writelines(['Hello there\n', 'how are you'])

# Write Data -> Add content to file multiple lines
with open("13_file_ops/new.txt","w") as file_data:
    file_data.writelines(['i"m  good\n', 'thank you\n'])

    
# Append Mode -> Write Data -> Add content to file multiple lines
with open("13_file_ops/new.txt","a") as file_data:
    file_data.writelines(['this is added\n', 'not overwritten'])
    
# Working with Directories / Folders 
import os
folder_name = "13_file_ops/student_data"

# print(os.path.exists(folder_name))
# os.makedirs(folder_name)

if not os.path.exists(folder_name):
   os.makedirs(folder_name)
   print(f"{folder_name} created") 
else:
    print(f"{folder_name} already exists") 
    
# Delete File 
os.remove("13_file_ops/new.txt")

# Delete Folder 
os.rmdir(folder_name)