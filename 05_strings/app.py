# Enhanced Student Tracker 

print("=" * 50)
print("         Enhanced Student Tracker")
print("=" * 50)

# Student ID
student_id_valid = False
while not student_id_valid:
    student_id = input("Enter Your ID: ")
    # check valid id 
        # checking for negative number
    if student_id.startswith("-") and student_id[1:].isdigit():
        print("Enter Positive Numbers only")
        # checking for zero 
    elif student_id.isdigit():
        student_id = int(student_id)
        
        # above zero then non-zero
        if student_id > 0:
            student_id_valid = True
        else:
            print("Zero not allowed") 
    else:
        print("ID should numbers only") 
               
# once id is valid format EDIFY-PYTHON-101
formatted_id =  "EDIFY-PYTHON-" + str(student_id)   
print("System Generated ID: "+ formatted_id)