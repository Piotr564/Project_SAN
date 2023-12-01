import random


class Book:
    def __init__(self, name, author):
        self.id = random.randrange(100, 1000)
        self.name = name
        self.author = author
        self.status = 'available'


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, name, author):
        book = Book(name, author)
        self.books.append(book)
        return book.id

    def borrow_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                if book.status == 'available':
                    book.status = 'borrowed'
                    return True
                else:
                    return False
        return False

    def return_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                if book.status == 'borrowed':
                    book.status = 'available'
                    return True
        return False

    def show_books(self):
        print("Books in library:")
        for book in self.books:
            print(f"ID: {book.id} Name: {book.name} Author: {book.author} Status: {book.status}")

    def run(self):
        while True:
            print("\n1. Add book\n2. Borrow book\n3. Return book\n4. View books\n5. Exit")
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                name = input("\nEnter book name: ")
                author = input("Enter book author: ")
                book_id = self.add_book(name, author)
                print(f"Book added with ID: {book_id}")
            elif choice == 2:
                book_id = int(input("Enter book ID you want to borrow: "))
                if self.borrow_book(book_id):
                    print("Book borrowed successfully")
                else:
                    print("Book is not available or ID invalid")
            elif choice == 3:
                book_id = int(input("Enter ID of book you want to return: "))
                if self.return_book(book_id):
                    print("Book returned successfully")
                else:
                    print("Invalid book ID")
            elif choice == 4:
                self.show_books()
            elif choice == 5:
                break
            else:
                print("Please choose a valid option")


if __name__ == "__main__":
    library = Library()
    library.run()
