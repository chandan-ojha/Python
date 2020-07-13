#multiple inheritance
class A:
    def display1(self):
        print("I am inside A class")
class B:
    def display2(self):
        print("I am inside B class")
class C(A,B):
       def display3(self):
        super().display1()
        super().display2()
        print("I am inside c class")

obj=C()
obj.display3()


