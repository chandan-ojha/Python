class Student:
    roll = " "
    gpa = " "


rahim = Student()
karim = Student()
print(isinstance(rahim, Student))
rahim.roll = 101
rahim.gpa = 3.7
print(f"Roll : {rahim.roll}, GPA: {rahim.gpa}")
karim.roll = 103
karim.gpa = 3.8
print(f"Roll : {karim.roll}, GPA: {karim.gpa}")


