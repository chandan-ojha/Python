subjects=["C","Design Pattern","Java","Data Structure","Algorithom"]
print(len(subjects))
# append function
subjects.append("TOC")
print(subjects)

#insert function
subjects.insert(0,"QBasic64")
print(subjects)

#remove function
subjects.remove("Algorithom")
print(subjects)

#sorting
subjects.sort()
print(subjects)


subjects1=[10,5,40,30,25]
subjects1.sort()
print(subjects1)

#reverse function
subjects1.reverse()
print(subjects1)

#pop function
subjects1.pop()
subjects1.pop()
print(subjects1)

#clear function
""" 
subjects1.clear()
print(subjects1)
"""

#coppy function
subjects2=subjects1.copy()
print(subjects2)

#index function
pos=subjects2.index(25)
print(pos)

#count function
count_no=subjects2.count(25)
print(count_no)
