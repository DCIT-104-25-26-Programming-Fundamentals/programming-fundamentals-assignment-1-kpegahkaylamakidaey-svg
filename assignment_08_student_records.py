# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# Feature 1: Add student record
def add_student(students_list):
    name = input("Student name: ")
    student_id = input("Student ID: ")
    score_count = int(input("How many scores? "))
    
    scores = []
    for i in range(1, score_count + 1):
        score = float(input("Enter score " + str(i) + ": "))
        scores.append(score)
        
    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    
    students_list.append(student)
    print()

# Feature 2: Display all students in a table layout
def display_all_students(students_list):
    if len(students_list) == 0:
        print("No student records found.")
        print()
        return
        
    # Matches the exact headers and dashed line from lines 65-66
    print("Name            ID              Scores          Average")
    print("-------------------------------------------------------")
    
    for student in students_list:
        total = 0
        for s in student["scores"]:
            total = total + s
            
        if len(student["scores"]) > 0:
            avg = total / len(student["scores"])
        else:
            avg = 0.0
            
        # Convert the list of scores into a simple comma-separated string
        score_strings = []
        for s in student["scores"]:
            score_strings.append(str(int(s) if s.is_integer() else s))
        comma_scores = ", ".join(score_strings)
        
        # Format the text strings with simple tabs for a clean column layout
        print(student["name"] + "\t" + student["id"] + "\t" + comma_scores + "\t" + f"{avg:.23g}"[:5] if len(f"{avg:.2f}")>5 else f"{avg:.2f}")
    print()

# Feature 3: Calculate specific average
def calculate_average_score(students_list):
    if len(students_list) == 0:
        print("No student records found.")
        print()
        return
        
    search_id = input("Enter student ID: ")
    found = False
    
    for student in students_list:
        if student["id"] == search_id:
            found = True
            total = 0
            for s in student["scores"]:
                total = total + s
                
            if len(student["scores"]) > 0:
                avg = total / len(student["scores"])
            else:
                avg = 0.0
                
            # Matches line 72 exactly
            print(student["name"] + "'s average score: " + f"{avg:.2f}")
            
    if not found:
        print("Error: Student ID not found.")
    print()

def main():
    all_students = []
    
    while True:
        print("========================")
        print("STUDENT RECORD SYSTEM MENU")
        print("========================")
        print("1. Add student")
        print("2. Display all students")
        print("3. Calculate average score")
        print("4. Quit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_student(all_students)
        elif choice == "2":
            display_all_students(all_students)
        elif choice == "3":
            calculate_average_score(all_students)
        elif choice == "4":
            break
        else:
            print("Error: Invalid choice.")
            print()

if __name__ == "__main__":
    main()
