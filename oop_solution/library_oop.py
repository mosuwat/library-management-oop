# Library Management System - Object Oriented Style

class Book:
    def __init__(self, id = '000', title = 'test', author = 'test', available_copies = 999):
        self.id = id
        self.title = title
        self.author = author
        self.total_copies = available_copies
        self.available_copies = available_copies

    def book_info(self):
        return f"{self.title} by {self.author} - {self.available_copies} copies available"
    
    def take_book(self):
        if self.available_copies <= 0:
            return False
        else:
            self.available_copies -= 1
            return True
    
    def return_book(self):
        if self.available_copies >= self.total_copies:
            return False
        else:
            self.available_copies += 1
            return True

class Member:
    def __init__(self, id = '111', name = 'member_test', email = 'member_test@gmail.com'):
        self.id = id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            return "Error: Member has reached borrowing limit!"
        elif book.take_book():
            self.borrowed_books.append(book)
            return f"{self.name} borrowed '{book.title}'"
        else:
            return "Error: No copies available!"
    
    def return_borrowed_books(self, book):
        if book in self.borrowed_books:
            if book.return_book():
                self.borrowed_books.remove(book)
                return f"{self.name} returned '{book.title}'"
            else:
                return f"Error: Return more than total copies!"
        else:
            return "Error: This member hasn't borrowed this book!"