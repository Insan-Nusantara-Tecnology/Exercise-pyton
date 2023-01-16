"""

"""
data_valid = False

while data_valid == False:
    grade1 = float(input("type the grade of the first test: "))
    if grade1 < 0 and grade1 > 10:
        print("Grade should be between 0 and 10")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:
    grade2 = float(input("type the grade of the second test: "))
    if grade2 < 0 and grade2 > 10:
        print("Grade should be between 0 and 10")
        continue
    else:
        data_valid = True

absences = int(input("Type the total number of classes: "))
total_classes = int(input("Type the total number of classes: "))

avg_grade = (grade1 + grade2) / 2
attendance = (total_classes - absences) / total_classes

print("Average grade: ", round(avg_grade, 2))
print("Attendance rate: ", str( round((attendance * 100), 2)) + "%")

if 6 <= avg_grade >= 0.8:
    print("The student has apporved.")
elif 6 > avg_grade < 0.8:
    print("The sttudent has failed due to an average grade lower than 6.0 and an attandance rate lower than 80%.")
elif attendance >= 0.8:
    print("The student has failed due to an average grade lower than 6.0.")
else:
    print("The student has failed due to an average grade lower than 80%.")


