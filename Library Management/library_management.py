class Book:
    def __init__(self, title, author,_is_checked_out = 0 ):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out
    def __str__(self):
        return(f"Title: {self.title} Author: {self.author}")
    def check_a_book(self):
        if self._is_checked_out == 0:
            self._is_checked_out = 1
        
    def return_book(self):
        if self._is_checked_out == 1:
             self._is_checked_out = 0


class Library:
    def __init__(self):
        self._books = []
        
     

    def add_book(self,newbook):
        if  isinstance(newbook,Book):
            self._books.append(newbook)
        
        
    
    def check_out_book(self,title):
        for book in self._books:
            if book.title == title:
                book.check_a_book()
        
            
    def return_book(self,title):
        for book in self._books:
            if book.title == title:
                book.return_book()
            
    def list_available_books(self):
        for book in self._books:
            if  book._is_checked_out == 0:
                print(book)
          
    

# myBook = Book("The Beast","edward")
# lib = Library()
# print(myBook)
# lib.add_book(myBook)
# lib.list_available_books()
# library = Library()
# library.add_book(Book("Brave New World", "Aldous Huxley"))
# library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
# print("Available books after setup:")
# library.list_available_books()