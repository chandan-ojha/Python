#xxargs like tupples
def student(*details):
    print(details)
    #print(details[0])
student(101,"Chandan")
student("101","Chandan",3.7)

def add(*numbers):
    sum=0
    for num in numbers:
        sum=sum+num
    print(sum)
add(10,20)
add(1,2,3)
add(1,2,3,4,5)

#xxxargs
def student1(**details1):
    print(details1)
student1(id="181-35-2425",name="Chandan Ojha")