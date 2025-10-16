# Working with csv module 

with open("13_file_ops/students.csv","r") as file_data:
    print(file_data.read())
print("="*50)
    
# now working with csv module
import csv
with open("13_file_ops/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        print(row)

print("="*50)

# Assume we have 10k customers
# Requirement : Fetch me customers by location field
search_by_city = "pune"
with open("13_file_ops/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        if row[-1] == search_by_city:
            print(row)
print("="*50)

# reader is good for index based
# Using DictReader -> dict works on key based 
search_by_city = "pune"
with open("13_file_ops/students.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    # print(csv_reader.fieldnames)
    for row in csv_reader:
        print(row)
print("="*50)

# Requirement : Fetch me customers by location field
search_by_city = "hyderabad"
with open("13_file_ops/students.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        if row['address'] == search_by_city:
            print(row)
print("="*50)    

# Write the Data to csv file 
with open("13_file_ops/employee.csv","w") as file_data:
    csv_writer = csv.writer(file_data)
    csv_writer.writerow(['name','email','mobile','address'])
    csv_writer.writerow(['krishna', 'krishna@gmail.com', '998998998', 'hyderabad'])
    csv_writer.writerows([['ravi', 'ravi@gmail.com', '998998998', 'hyderabad'],
['ramu', 'ramu@outlook.com', '998998998', 'bangalore'],
['suresh', 'suresh@gmail.com', '998998998', 'pune']])
    
# Write the Data to csv file using DictWriter
fieldnames = ['name', 'email', 'mobile', 'address']
with open("13_file_ops/employee.csv","w") as file_data:
    csv_writer = csv.DictWriter(file_data,fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerow({'name': 'krishna', 'email': 'krishna@gmail.com', 'mobile': '998998998', 'address': 'hyderabad'})
    csv_writer.writerows([{'name': 'suresh', 'email': 'suresh@gmail.com', 'mobile': '998998998', 'address': 'pune'},
{'name': 'mahesh', 'email': 'mahesh@yahoo.com', 'mobile': '998998998', 'address': 'chennai'}])