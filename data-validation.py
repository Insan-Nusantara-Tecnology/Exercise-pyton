data_valid = False
while not data_valid:
    grade1 = float(input("type the grade of the first test: "))
    if grade1 < 0 or grade1 > 10:
        print("Grade should be between 0 and 10")
    else:
        data_valid = True

data_valid = False
while not data_valid:
    grade2 = float(input("type the grade of the second test: "))
    if grade2 < 0 or grade2 > 10:
        print("Grade should be between 0 and 10")
    else:
        data_valid = True

data_valid = False
while not data_valid:
    total_classes = int(input("Type the total number of classes: "))
    if total_classes <= 0:
        print("The number of classes can't zero or less")
    else:
        data_valid = True

data_valid = False
while not data_valid:
    absences = int(input("Type the total number of absences: "))
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
