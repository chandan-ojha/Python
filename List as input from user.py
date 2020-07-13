"""
n=input("Enter a text of numbers: ")
#10 20 30 40
list =n.split() #10,20,30,40
sum=0
for num in list:
    sum=sum+int(num)
print(sum)

"""
# find number of words, number of letters,number of digit
numOfWords=0
numOfLetters=0
numOfDigits=0
text=input("Enter a text of numbers: ") #My name is 123

for x in text:
    x=x.lower()
    if x>='a' and x<='z':
        numOfLetters=numOfLetters+1

    elif x >= '0' and x <= '9':
        numOfDigits = numOfDigits + 1

    elif x==' ':
        numOfWords = numOfWords + 1

print("Number Of Letters: ",numOfLetters)
print("Number Of Digits: ",numOfDigits)
print("Number Of Words: ",numOfWords+1)

