# oop/library_system.py

from book_class import EBook, PrintBook, Library

def main():
    library = Library()

    ebook = EBook("Python Basics", "John Doe", 500)
    printbook = PrintBook("Learning OOP", "Jane Smith", 300)

    library.add_book(ebook)
    library.add_book(printbook)

    library.show_books()

if __name__ == "__main__":
    main()

