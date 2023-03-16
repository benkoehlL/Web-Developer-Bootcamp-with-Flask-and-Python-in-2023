class Student():
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def average_grade(self):
        return sum(self.grades)/len(self.grades)

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return("The person's name is {} and is {} years old".format(self.name, self.age))
    
    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"

class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")
    
    def __str__(self):
        return("ClassTest method")
    
    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method.")
    
class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book '{self.name}', '{self.book_type}', weight {self.weight}g>"
    
    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight +100)
    
    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


student = Student('Rolf', [90,90,93,78,90])
print(student.name)
print(student.grades)
print(student.average_grade())

bob = Person("Bob", 35)
print(bob) # print string representation of object
print(bob.__repr__()) # print __repr__ representation of object when __str__() is defined

test = ClassTest()
test.instance_method()
ClassTest.instance_method(test)
ClassTest.class_method()
ClassTest.static_method()

print(Book.TYPES)
book1 = Book("War and Peace", "hardcover", 1800)
print(book1)
book2 = Book.hardcover("Crime and Punishment", 1800)
print(book2)
book3 = Book.paperback("Anna Karenina", 2000)
print(book3)