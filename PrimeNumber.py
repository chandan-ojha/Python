#check prime number or not
num=int(input("Enter any positive number: "))

for x in range(2,num):
    if num%x==0:
        print(num,"Not Prime Number")
        break
else:
    print("Prime Number")



# Python Program to Print all Prime Numbers in an Interval
lower=int(input("Enter Lower Number: "))
upper=int(input("Enter Upper Number: "))
print("Prime numbers between", lower, "and", upper, "are:")
for num1 in range(lower,upper+1):
    if num1>1:
        for i in range(2,num1):
            if num1%i==0:
                break
        else:
         print(num1)