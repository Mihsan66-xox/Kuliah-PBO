class Book:
    note = "A class type to represent a book"

print(f"Class Book note: {Book.note}")

book1 = Book()
print(f"Object book1 note: {book1.note}")

class Pencil:

    def __init__(self):
        self.note = "A class type to represent a book"

pencil1 = Pencil()
print(f"Object pencil1 note: {pencil1.note}")