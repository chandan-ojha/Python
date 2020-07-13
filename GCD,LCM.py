num1=int(input("Enter Number1: "))
num2=int(input("Enter Number2: "))
while num2!=0:
     reminder=num1%num2
     num1=num2
     num2=reminder
gcd=num1
lcd=(num1*num2)//gcd
print("GCD: ",gcd)
print("LCD: ",lcd)
