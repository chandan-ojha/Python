#(i) 1+2+3+...+n
n=int(input("Enter The Last Number: "))
sum =0

for x in range(1,n+1,1):
    sum=sum+x
print(sum)

#(ii)2+4+6+...+n
n1=int(input("Enter The Last Number: "))
sum1 =0

for x1 in range(2,n1+1,2):
    sum1=sum1+x1
print(sum1)


#(iii)1+3+5+...+n
n2=int(input("Enter The Last Number: "))
sum2 =0

for x2 in range(1,n2+1,2):
    sum2=sum2+x2
print(sum2)


#(iv)1^2+2^2+3^2+...+n^2
n3=int(input("Enter The Last Number: "))
sum3 =0
for x3 in range(1,n2+1,1):
    sum3=sum3+x3*x3
print(sum3)

#(v)1+1/2+1/3....+1/n
n4=int(input("Enter The Last Number: "))
sum4=0
for x4 in range(1,n4+1,1):
    sum4=sum4+1/x4
print(sum4)

#(vi) 1x2x3x4.......x n
n5=int(input("Enter The Last Number: "))
sum5=1
for x5 in range(1,n5+1,1):
    sum5=sum5*x5
print(sum5)




