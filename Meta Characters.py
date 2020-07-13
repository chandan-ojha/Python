# dot meta characters
import re
pattern1 =r"colo..r"

if re.match(pattern1,"coloubr"):
    print("Matched")


# ^ $
pattern2 =r"^colo..r$"

if re.match(pattern2,"coloubr"):
    print("Matched")


# *(0 or more)
pattern3 =r"(ab)*"

if re.match(pattern3,"coloubr"):
    print("Matched")


# +(1 or more)
pattern4 =r"(a*b)+"

if re.match(pattern4,"abcoloubr"):
    print("Matched")
else:
    print("Not matched")


# ?(0 or 1)
pattern5 =r"ice(-)?cream"

if re.match(pattern5,"ice-cream"):
    print("Matched")
else:
    print("Not matched")

# {and}
pattern6 =r"a{1,3}$"

if re.match(pattern6,"aaaa"):
    print("Matched")
else:
    print("Not matched")