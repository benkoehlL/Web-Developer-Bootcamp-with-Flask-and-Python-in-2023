from typing import List

def list_avg(sequence : List) -> float:
    return sum(sequence)/len(sequence)

    
class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: TYPES, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book '{self.name}', '{self.book_type}', weight {self.weight}g>"
    
    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return Book(name, Book.TYPES[0], page_weight +100)
    
    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)

class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"BookShelf with {len(self.books)} books."
