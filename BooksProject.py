book_stack = ["Book A", "Book B", "Book C", "Book D"]
desired_book = input("Enter book title: ")
#desired_book in book_stack
if desired_book in book_stack:
    print("book found")
else: 
    print("book not found")