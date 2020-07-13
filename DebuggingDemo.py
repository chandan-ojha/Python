def add(*numbers):
    sum=0
    for num in numbers:
        sum=sum+num
    return sum
print(add(10,20))