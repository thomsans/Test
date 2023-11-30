student_grades = {}

while True:
    add_student = input("Would you like to add a student? (Y/N): ").lower()
    if add_student == 'y':
        name = input("Enter student name: ")
        subject_qty = int(input("How many subjects?: "))
        grade_list = []
        for i in range(subject_qty):
            grade = int(input(f"Enter grade for subject {i+1}: "))
            grade_list.append(grade)
        
        student_grades[name] = grade_list
    
    elif add_student == 'n':
        break

for item in student_grades.items():
    print(item)

while True:
    see_average = input("See Average? (Y/N): ").upper()
    if see_average == 'Y':
        name = input("Enter student name: ")
        grade_list = student_grades.get(name)
        print(f"Average of {name} is: {sum(grade_list)/len(grade_list)}")
    elif see_average == 'N':
        break


