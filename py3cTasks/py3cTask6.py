name = input("Student name: ")
subjects = []
grades = []

for i in range(1, 6):
    subject = input(f"Enter subject {i}: ")
    grade = int(input(f"Enter grade {i}: "))
    subjects.append(subject)
    grades.append(grade)

average = sum(grades) / len(grades)

if average >= 90:
    letter = "A"
elif average >= 80:
    letter = "B"
elif average >= 70:
    letter = "C"
elif average >= 60:
    letter = "D"
else:
    letter = "F"

print("\nREPORT CARD")
print("Student:", name)
for i in range(5):
    print(subjects[i], "grade is", grades[i])

print("Average grade:", round(average, 1))
print("Letter grade:", letter)
