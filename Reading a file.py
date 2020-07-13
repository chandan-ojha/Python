file=open("student.txt","r+")
#print(file.readable())
"""
text=file.read()
print(text)
"""

"""
text1=file.readlines()[0]
print(text1)
"""

for line in file:
    print(line)

"""
size=len(text)
print(size)
"""
file.close()