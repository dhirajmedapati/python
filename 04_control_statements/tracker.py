# # Student Grade Tracker 

# -> Collect Following Info From Student

#     -> Student ID
#     -> Student Name
#     -> Attendance
#     -> Total Score 
student_id = int(input("enter student ID "))
student_name = input("enter student name ")
attendance = int(input("enter student attendance "))
#score = int(input("Enter score "))
no_of_subjects = 1
additional_score = "yes"
total_score = 0 
while additional_score == "yes" :
    current_score = int(input("Enter score "))
    additional_score = str(input("Do you want to enter another score? yes/no "))
    no_of_subjects +=1
    total_score = current_score + total_score
    # if additional_score == "yes":
    #     additional_score = int(input("Enter score "))
    # else:
    #     print(f"total no of scores entered is {no_of_subjects}")
average_score = total_score/no_of_subjects
print(total_score)
print(average_score)
print(no_of_subjects)
    


# -> Ask Student To enter Score 

# -> Repeatedly ask student to enter scores, till he says no 

#     Do you want to enter another score ? (yes/no)

# -> Calculate Total Scores (score1 + score 2 + .... yes)

# -> Give me the average score 

# -> Based On above average score Calculate Performance

#     -> 85 and above Excellent 
#     -> 70 to 84 Good
#     -> 50 to 69 Average 
#     -> Below 50 Fail

# -> Check Attendance Criteria 
#     -> Attendance less than 75 : WARNING LOW ATTENDANCE 
#                                  OK GOOD ATTENDANCE


# -> Finally display 

#     -> Student ID
#     -> Student Name
#     -> Attendance
#     -> Total score
#     -> Average Score 
#     -> Number Of Subjects 
#     -> Performance
#     -> Attendance Status 