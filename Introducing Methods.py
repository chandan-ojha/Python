class Student:
    roll = " "
    gpa = " "

    def set_value(self,roll,gpa):
        self.roll=roll
        self.gpa=gpa
    def display(self):
        print(f"Roll : {self.roll}, GPA: {self.gpa}")


rahim = Student()
karim = Student()
print(isinstance(rahim, Student))

rahim.set_value(101,3.7)
rahim.display()

karim.set_value(102,3.5)
karim.display()


