import re
pattern =r"[A-Z][a-z][0-9]"

if re.match(pattern,"Ag0ggggggggggggjk"):
    print("Matched")
else:
    print("Not Matched")