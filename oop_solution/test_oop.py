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

print("=" * 60)
print("LIBRARY MANAGEMENT SYSTEM - COMPREHENSIVE TEST")
print("=" * 60)

lp = lo.Library()
# Test 1: Add Books
print("\n--- TEST 1: Adding Books ---")
lp.add_book(1, "Python Crash Course", "Eric Matthes", 3)
lp.add_book(2, "Clean Code", "Robert Martin", 2)
lp.add_book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1)
lp.add_book(4, "Design Patterns", "Gang of Four", 2)

# Test 2: Add Members
print("\n--- TEST 2: Registering Members ---")
lp.add_member(101, "Alice Smith", "alice@email.com")
lp.add_member(102, "Bob Jones", "bob@email.com")
lp.add_member(103, "Carol White", "carol@email.com")

# Test 3: Display Available Books
print("\n--- TEST 3: Display Available Books ---")
lp.display_available_books()

# Test 4: Successful Book Borrowing
print("\n--- TEST 4: Successful Borrowing ---")
lp.borrow_book(101, 1)  # Alice borrows Python Crash Course
lp.borrow_book(101, 2)  # Alice borrows Clean Code
lp.borrow_book(102, 1)  # Bob borrows Python Crash Course

# Test 5: Display Member's Borrowed Books
print("\n--- TEST 5: Display Member's Books ---")
lp.display_member_books(101)  # Alice's books
lp.display_member_books(102)  # Bob's books
lp.display_member_books(103)  # Carol's books (none)

# Test 6: Display Available Books After Borrowing
print("\n--- TEST 6: Available Books After Borrowing ---")
lp.display_available_books()

# Test 7: Borrow Last Available Copy
print("\n--- TEST 7: Borrowing Last Copy ---")
lp.borrow_book(103, 3)  # Carol borrows the only copy of Pragmatic Programmer
lp.display_available_books()

# Test 8: Try to Borrow Unavailable Book
print("\n--- TEST 8: Attempting to Borrow Unavailable Book ---")
lp.borrow_book(102, 3)  # Bob tries to borrow unavailable book

# Test 9: Borrowing Limit Test
print("\n--- TEST 9: Testing Borrowing Limit (3 books max) ---")
lp.borrow_book(101, 4)  # Alice's 3rd book
lp.display_member_books(101)
lp.borrow_book(101, 3)  # Alice tries to borrow 4th book (should fail)

# Test 10: Return Books
print("\n--- TEST 10: Returning Books ---")
lp.return_book(101, 1)  # Alice returns Python Crash Course
lp.return_book(102, 1)  # Bob returns Python Crash Course
lp.display_member_books(101)
lp.display_available_books()

# Test 11: Try to Return Book Not Borrowed
print("\n--- TEST 11: Attempting Invalid Return ---")
lp.return_book(102, 2)  # Bob tries to return book he didn't borrow

# Test 12: Return and Borrow Again
print("\n--- TEST 12: Return and Re-borrow ---")
lp.return_book(103, 3)  # Carol returns Pragmatic Programmer
lp.borrow_book(102, 3)  # Bob borrows it
lp.display_member_books(102)

# Test 13: Error Cases - Non-existent Member/Book
print("\n--- TEST 13: Error Handling ---")
lp.borrow_book(999, 1)  # Non-existent member
lp.borrow_book(101, 999)  # Non-existent book
lp.return_book(999, 1)  # Non-existent member
lp.display_member_books(999)  # Non-existent member

# Test 14: Final Status
print("\n--- TEST 14: Final Library Status ---")
print("\nAll Borrowed Books:")
for transaction in lp.transactions:
    print(f"  {transaction['member_name']} has '{transaction['book_title']}'")

print("\nAll Members and Their Books:")
for member in lp.members:
    print(f"\n{member.name} ({member.id}):")
    if member.borrowed_books:
        for book in member.borrowed_books:
            print(f"  - {book.title}")
    else:
        print("  (No books borrowed)")

lp.display_available_books()

print("\n" + "=" * 60)
print("TEST COMPLETE")
print("=" * 60)