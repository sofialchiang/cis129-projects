#Sofia Chiang (Arroyo)
#05/05/2024, CIS 129
#(9.1) This code allows you to store any number of grades into a 'grades.txt' plain text file

# Open the grades.txt file in write mode
with open("grades.txt", "w") as file:
    # Prompt the user to enter grades
    print("Enter the grades (type 'done' when finished):")
    
    # Accepting grades until the user enters 'done'
    while True:
        grade = input("Grade: ")
        
        # If the user enters 'done', break out of the loop
        if grade.lower() == 'done':
            break
        
        # Write the grade to the file
        file.write(grade + "\n")

print("Grades have been saved to grades.txt.")

#(9.2) This code displays the individual grades from the previous code and displays total, count, and the average

# Open the grades.txt file in read mode
with open("grades.txt", "r") as file:
    # Read all lines from the file
    lines = file.readlines()
    
    # Initialize variables for total, count, and grades list
    total = 0
    count = 0
    grades = []
    
    # Iterate over each line in the file
    for line in lines:
        # Convert the line to an integer grade
        grade = int(line.strip())
        
        # Add the grade to the total and increment the count
        total += grade
        count += 1
        
        # Append the grade to the grades list
        grades.append(grade)

# Display individual grades
print("Individual Grades:")
for grade in grades:
    print(grade)

# Display total, count, and average
print("\nTotal:", total)
print("Count:", count)
print("Average:", total / count)