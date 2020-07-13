n=int(input("Enter a number to calculate its factorial: "))
fac=1
for x in range(1,n+1,1):
    fac=fac*x
print(fac)