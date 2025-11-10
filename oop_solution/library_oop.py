# Library Management System - Object Oriented Style

class Book:
    def __init__(self, id, title, author, available_copies):
        self.id = id
        self.title = title
        self.author = author
        self.total_copies = available_copies
        self.available_copies = available_copies

    def display_info(self):
        print(f"{self.title} by {self.author} - {self.available_copies} copies available")
    
    def take_book(self):
        if self.available_copies <= 0:
            print("Error: No copies available!")
        else:
            self.available_copies -= 1
    
    def return_book(self):
        if self.available_copies >= self.total_copies:
            print("Error: Return more than total copies!")
        else:
            self.available_copies += 1