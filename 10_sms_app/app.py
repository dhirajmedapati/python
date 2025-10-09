# Solution for Student/Product/Employee Management System 

# Fixed Data for System Info() => Immutable Data (Tuple)

# System Info
SYSTEM_INFO = ("Edify Student Management Portal","v1","2025","Edify University")
ADMIN_INFO = ("admin@edify.edu","9890383883","201")

# Display System Info at StartUp
print("="*50)
print(f"        Welcome To {SYSTEM_INFO[0]}")
print(f"        Developed By Students at {SYSTEM_INFO[-1]}")
print("="*50)

# store students in dictionary 
students = {}

# Building Menu Based System 
while True:
    print("Choose an option below: ")
    print("1 - Add Student")
    print("2 - Update Student")
    print("3 - Delete Student")
    print("4 - Lists Students")
    print("5 - Exit System")
    
    choice = input("Enter Your Choice (1-5): ")
    
    if choice == "1":
        print("Performing Choice 1 Operation")
        student_id = input("Enter ID: ")
        if student_id in students:
            print("ID Already Exists")
        else:
            name = input("Enter Name: ").title()
            # for scores will use list 
            scores = []
            while True:
                score_input = input("Enter Score or type done: ")
                if score_input == "done":
                    break
                if score_input.isdigit():
                    score = int(score_input)
                    if 0 <= score <=100:
                        scores.append(score)
                    else:
                        print("Score should be in 0-100")
                else:
                    print("Score should be Numbers Only")
                        
            # for skills will use set 
            skills = set()
            while True:
                skill_input = input("Enter Skill or type done: ")
                if skill_input == "done":
                    break
                skills.add(skill_input)
            
            # Save this student to dict students 
            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills
            }
            
            print("Student Added To System")
            
            # for verification 
            print(students)
                    
        
    elif choice == "2":
        print("Performing Choice 2 Operation")    
    elif choice == "3":
        print("Performing Choice 3 Operation")
    elif choice == "4":
        print("Performing Choice 4 Operation")
    elif choice == "5":
        print("Performing Choice 5 Operation")
        break
    else:
        print("Invalid Choice, only (1-5) Operations Supported")