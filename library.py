
class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = "Available"


books = []


def add_book():

    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    book = Book(book_id, title, author)

    books.append(book)

    print("Book added successfully!")


def view_books():

    if len(books) == 0:
        print("No books available.")
        return

    print("\nLibrary Books")

    for book in books:
        print("--------------------")
        print("Book ID :", book.book_id)
        print("Title   :", book.title)
        print("Author  :", book.author)
        print("Status  :", book.status)


def search_book():

    book_id = input("Enter Book ID: ")

    for book in books:

        if book.book_id == book_id:
            print("\nBook Found")
            print("Book ID :", book.book_id)
            print("Title   :", book.title)
            print("Author  :", book.author)
            print("Status  :", book.status)
            return

    print("Book not found.")


def issue_book():

    book_id = input("Enter Book ID to issue: ")

    for book in books:

        if book.book_id == book_id:

            if book.status == "Available":
                book.status = "Issued"
                print("Book issued successfully.")
            else:
                print("Book is already issued.")

            return

    print("Book not found.")


def return_book():

    book_id = input("Enter Book ID to return: ")

    for book in books:

        if book.book_id == book_id:

            if book.status == "Issued":
                book.status = "Available"
                print("Book returned successfully.")
            else:
                print("Book is already available.")

            return

    print("Book not found.")


def delete_book():

    book_id = input("Enter Book ID to delete: ")

    for book in books:

        if book.book_id == book_id:

            books.remove(book)
            print("Book deleted successfully.")
            return

    print("Book not found.")


while True:

    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        issue_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        delete_book()

    elif choice == "7":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
