import library_oop as lo

# Test Code for Object Oriented Library System

#TEST book class
book1 = lo.Book('123', "Paruj in the wonderland", "Suwat", 20)
book2 = lo.Book('456', "Piya and the seven drawf", "tatsu", 1)
book3 = lo.Book('222', "Supaporn and the beast", "sutat", 5)

#Test take and return book
print("=== TEST TAKE AND RETURN BOOK ===")
print(book1.book_info())
book1.take_book()
print(book1.book_info())
book1.return_book()
print(book1.book_info())
book1.return_book()
print(book2.book_info())
if not book2.take_book():
    print("ERROR!")
if not book2.take_book():
    print("ERROR!")
print(book2.book_info())
print()

#Test member class
print("=== TEST MEMBER TAKE AND RETURN ===")
member1 = lo.Member('007', 'Alice', 'Alice@gmail.com')
print(member1.borrow_book(book1))
print(member1.return_borrowed_books(book1))
print(member1.borrow_book(book2))
print(member1.borrow_book(book3))
print(member1.borrow_book(book3))
print(member1.borrow_book(book1))
print(member1.return_borrowed_books(book3))
print(member1.return_borrowed_books(book3))
print(member1.return_borrowed_books(book3))