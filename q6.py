class Library_book:
    def __init__(self, book_name, author):
        self.__book_name = book_name
        self.__author = author
        self.__available = True
    
    def get_book(self):
        return self.__book_name

    def get_author(self):
        return self.__author
    
    def get_status(self):
        return self.__available
    

    # Borrowing a book    

    def borrow(self):
        if self.__available:
            self.__available = False
            print(f"The book {self.__book_name} by {self.__author} has been borrowed.")
        else:
            print(f"Sorry the book {self.__book_name} by {self.__author} is not available.")


    # Returning a book
    def returning(self):
        if self.__available == False:
            self.__available = True
            print(f"The book {self.__book_name} by {self.__author} has been returned.")
        else:
            print(f"The book {self.__book_name} already exists")

    def display_info(self):
        print(f"Name: {self.__book_name}")
        print(f"Author: {self.__author}")
        availability = "Available" if self.__available else "Not Available"
        print(f"Availablity: {availability}")


if __name__ == '__main__':
    book1 = Library_book("Can't hurt me","David Goggins")
    book2 = Library_book("The Alchemist","Paulo Coelho")

    # Display info
    book1.display_info()
    book2.display_info()

    # Borrow book
    book1.borrow()

    book1.borrow() # borrowing more than once for checking wheter the method is correct
    
    book1.display_info()

    # returning the book

    book1.returning()

    # Displaying the updated records
    book1.display_info()




