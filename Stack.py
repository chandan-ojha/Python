books =[]
books.append("Learn c")
books.append("Learn java")
books.append("Learn python")
print(books)

books.pop()
print("Now the top book is: ",books[-1])

books.pop()
print("Now the top book is: ",books[-1])

books.pop()
if not books:
    print("No books left")