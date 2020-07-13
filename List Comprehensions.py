num=[1,2,3,4,5]
#result=list(map(lambda x:x*x,num))
result1=[x*x for x in num]
print(result1)

#result=list(filter(lambda x: x%2==0,num))
result2=[x for x in num if x%2==0]
print(result2)