try:
  list =[20,0,30]
  result=list[0]/list[3]
  print(result)
  print("Done")
except ZeroDivisionError:
  print("Dividing by zero is not possible")
except IndexError:
    print("Index error")
#finally:
print("Successful")


