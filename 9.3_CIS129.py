#Sofia Chiang (Arroyo)
#05/05/2024, CIS129
#(9.3) This program allows instructors to enter each student’s first and last name as strings and the student’s three exam grades as integers

import csv

# Prompt the instructor to enter student information
def enter_student_info():
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    exam1_grade = int(input("Enter student's exam 1 grade: "))
    exam2_grade = int(input("Enter student's exam 2 grade: "))
    exam3_grade = int(input("Enter student's exam 3 grade: "))
    return (first_name, last_name, exam1_grade, exam2_grade, exam3_grade)

# Write student information to grades.csv
def write_to_csv(file_name, student_info):
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(student_info)

# Main function to run the program
def main():
    while True:
        student_info = enter_student_info()
        write_to_csv('grades.csv', student_info)
        choice = input("Would you like to continue? (y/n): ").lower()
        if choice != 'y':
            break
    print("Student records have been written to grades.csv.")

# Call the main function to start the program
if __name__ == "__main__":
    main()