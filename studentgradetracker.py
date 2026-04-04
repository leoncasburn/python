students = {
    "Arthur": [85, 92, 78, 90],
    "Dutch": [70, 65, 80, 75],
    "John": [95, 98, 92, 100],
}

print("Student Average Grades:")

for name, grade in students.items():
    average = sum(grade) / len(grade)
    print(f"{name}: {round(average, 2)}")

while True:
    student_selector = input("Enter a student's name to see their grades (q to quit): ").capitalize()
    if student_selector == "Q":
        break
    if student_selector in students:
        print(f"{student_selector}'s grades: {students[student_selector]}")
    else:
        print("Student is not on file")
    

