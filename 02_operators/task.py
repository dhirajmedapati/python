# TASK
# Student Management System

Student_ID = 1
Student_Name = "Dhiraj"
Student_Age = 32
Quiz_score = 95
Assignment_score = 90
Exam_score = 85
Student_Attendance = 95

Total_score = Quiz_score + Assignment_score + Exam_score 
Average_score = (Quiz_score + Assignment_score + Exam_score ) / 3
student_pass = Average_score >= 75
Student_Attendance +=1
Award = Student_Attendance > 90 and Average_score >= 75

print("Student name is " + Student_Name)
print(f"Student age is {Student_Age}")
print(f"The Total score is {Total_score}")
print(f"The Average score is {Average_score}")
print(f"Did the student pass {student_pass}")
print(f"Eligible for award {Award}")

Student_ID = 2
Student_Name = "Medapati"
Student_Age = 31
Quiz_score = 90
Assignment_score = 80
Exam_score = 75
Student_Attendance = 80

Total_score = Quiz_score + Assignment_score + Exam_score 
Average_score = (Quiz_score + Assignment_score + Exam_score ) / 3
student_pass = Average_score >= 75
Student_Attendance +=1
Award = Student_Attendance > 90 and Average_score >= 75

print("Student name is " + Student_Name)
print(f"Student age is {Student_Age}")
print(f"The Total score is {Total_score}")
print(f"The Average score is {Average_score}")
print(f"Did the student pass {student_pass}")
print(f"Eligible for award {Award}")

# Display results
#     Student Information Section: ID, Name, Age
#     Academic Performance Section: Individual scores, total, and average
#     Status Section: Passing status and award eligibility

