# Library Management System - Object Oriented Style

class Book:
    def __init__(self, id = 000, title = 'test', author = 'test', available_copies = 999):
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
    def __init__(self, id = 111, name = 'member_test', email = 'member_test@gmail.com'):
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
        
class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = []
    
    def add_book(self, book_id, title, author, available_copies):
        """Add a new book to the library"""
        book = Book(book_id, title, author, available_copies)
        self.books.append(book)
        print(f"Book '{title}' added successfully!")
    
    def add_member(self, member_id, name, email):
        """Register a new library member"""
        member = Member(member_id, name, email)
        self.members.append(member)
        print(f"Member '{name}' registered successfully!")
    
    def find_book(self, book_id):
        """Find a book by ID"""
        for book in self.books:
            if book.id == book_id:
                return book
        return None
    
    def find_member(self, member_id):
        """Find a member by ID"""
        for member in self.members:
            if member.id == member_id:
                return member
        return None

    def borrow_book(self, member_id, book_id):
        """Process a book borrowing transaction"""
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        
        if not member:
            print("Error: Member not found!")
            return False
        
        if not book:
            print("Error: Book not found!")
            return False
        
        ret = member.borrow_book(book)
        if 'borrowed' not in ret:
            print(ret)
            return False
        else:
            transaction = {
                'member_id': member_id,
                'book_id': book_id,
                'member_name': member.name,
                'book_title': book.title
            }
            self.transactions.append(transaction)
            print(ret)
            return True
    
    def return_book(self, member_id, book_id):
        """Process a book return transaction"""
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        
        if not member or not book:
            print("Error: Member or book not found!")
            return False
        for i, transaction in enumerate(self.transactions):
            if transaction['member_id'] == member_id and transaction['book_id'] == book_id:
                self.transactions.pop(i)
                break
        print(member.return_borrowed_books(book))
        return True

    def display_available_books(self):
        """Display all books with available copies"""
        print("\n=== Available Books ===")
        for book in self.books:
            if book.available_copies > 0:
                print(book.book_info())
    
    def display_member_books(self, member_id):
        """Display books borrowed by a specific member"""
        member = self.find_member(member_id)
        if not member:
            print("Error: Member not found!")
            return
        
        print(f"\n=== Books borrowed by {member.name} ===")
        if not member.borrowed_books:
            print("No books currently borrowed")
        else:
            for book in member.borrowed_books:
                print(f"- {book.title} by {book.author}")