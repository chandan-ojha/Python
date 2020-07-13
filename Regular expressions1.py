import re
# match function
pattern1 =r"Colour"
if re.match(pattern1,"Colour is a colour,I love red colour"):
    print("Matche")
else:
    print("Not Matched")

# search function
pattern2 =r"Colour"
if re.search(pattern2,"Red is a Colour,I love red colour"):
    print("Matche")
else:
    print("Not Matched")

# find all function
pattern3 =r"Colour"
print(re.findall(pattern3,"Red is a Colour,I love red Colour"))
