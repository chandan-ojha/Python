#multilevel inheritance
class A:
    def display1(self):
        print("I am inside A class")
class B(A):
    def display2(self):
        print("I am inside B class")
class C(B):
    def display3(self):
        super().display1()
        super().display2()
        print("I am inside C class")
obj=C()
obj.display3()


