"""
Apply the try and except statements to the student grades program and keep it from crashing.
"""
data_valid = False
while not data_valid:
    grade1 = input("type the grade of the first test: ")
    try:
        grade1 = float(grade1)
    except:
        print("Invalid input. Only numbers are accepted. Decimmals should be separated with a dot.")
        continue

    if grade1 < 0 or grade1 > 10:
        print("Grade should be between 0 and 10")
    else:
        data_valid = True

data_valid = False
while not data_valid:
    grade2 = input("type the grade of the second test: ")
    try:
        grade2 = float(grade2)
    except:
        print("Invalid input. Only numbers are accepted. Decimmals should be separated with a dot.")
        continue

    if grade2 < 0 or grade2 > 10:
        print("Grade should be between 0 and 10")
    else:
        data_valid = True

data_valid = False
while not data_valid:
    total_classes = input("Type the total number of classes: ")
    try:
        total_classes = int(total_classes)
    except:
        print("Invalid input. Only numbers are accepted. Decimmals should be separated with a dot.")
        continue

    if total_classes <= 0:
        print("The number of classes can't zero or less")
    else:
        data_valid = True

data_valid = False
while not data_valid:
    absences = input("Type the total number of absences: ")
    try:
        absences = int(absences)
    except:
        print("Invalid input. Only numbers are accepted. Decimmals should be separated with a dot.")
        continue

    if absences < 0 or absences > total_classes:
        print("The number of absences can't zero or greater than the number of total classes.")
    else:
        data_valid = True

avg_grade = (grade1 + grade2) / 2
attendance = (total_classes - absences) / total_classes

print("Average grade: ", round(avg_grade, 2))
print("Attendance rate: ", str(round((attendance * 100), 2)) + " %")

if avg_grade >= 6 and attendance >= 0.8:
    print("The student has apporved.")
elif avg_grade < 6 and attendance < 0.8:
    print("The sttudent has failed due to an average grade lower than 6.0 and an attandance rate lower than 80%.")
elif attendance >= 0.8:
    print("The student has failed due to an average grade lower than 6.0.")
else:
    print("The student has failed due to an average grade lower than 80%.")
