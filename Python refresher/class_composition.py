class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."
    
class Book:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Book {self.name}"
    
book1 = Book("Roadside Picknick")
book2 = Book("Brothers Karamazov")
book3 = Book("The Idiot")
books = [book1, book2, book3]
bookshelf = BookShelf(*books)

for book in bookshelf.books:
    print(book)
print(bookshelf)