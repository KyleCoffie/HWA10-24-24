    # `2. Python Data Structure Challenges in Real-World Scenarios
    # Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.

    # Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

    # Existing Library Data:


def add_book (library):
    while True:
        title = input ("what is the book title?")
        author = input ("Who is the books' author?")
        if title not in library:
            library.append((title,author))
            print(library)
        else:
            print("Book already in library!!")
            
        more_books = input("Would you like to add another?   y/n ").lower()
        if more_books != "y":
            break
            
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
add_book(library)
    # - Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.`
    