import re
pattern =r"colour"
text="My Favourite colour is red."
match=re.search(pattern,text)

if match:
    print(match.start())
    print(match.end())
    print(match.span())

