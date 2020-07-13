"""
try:
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second  number: "))
    result=num1/num2
    print(result)
except (ValueError,ZeroDivisionError):
    print("you have entered incorrect input")

finally:
    print("thanks")
"""
def voter(age):
    if age<18:
        raise ValueError("Invalid Votter")
    return "you are allowed to vote"
try:
    print(voter(17))
except ValueError as e:
    print(e)

