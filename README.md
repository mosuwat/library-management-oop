# Project Overview

This project practice the skill to change a procedural system into an object oriented system and also shows how the testing is done.

## Project Structure

### library-management-oop

- `READEME.md` : This readme file.
- `procedural_version` : The procedural version of this project.
    - `library_procedural.py` : The procedural library code.
    - `test_procedural.py` : Testing file for the procedural version.
- `oop_solution` : The object oriented version of this project.
    - `library_oop` : The object oriented library code.
    - `test_oop` : Testing file for the object oriented version.

## Design Overview

### Book Class

Located in `library_oop.py`, the `Book` class includes:

---

**Attributes**
- `id` (int): The ID of this book.
- `title` (str): Title of the book.
- `author` (str): Author of the book.
- `total_copies` (int): The total copies of this book
- `available_copies` (int): The remaining copies of this book

**Methods**
- `book_info(self)`: Return the information of this book.
- `take_book(self)`: Check if can be borrowed, if `True` reduce `available_copies` by `1` and return `True`, else return `False`
- `return_book(self)`: Check if the returned book is not full, if `True` increase `available_copies` by 1 and return `True`, else return `False`

### Member Class

Located in `library_oop.py`, the `Member` class includes:

---

**Attributes**
- `id` (int): The ID of this member.
- `name` (str): Name of this member.
- `email` (str): Email of this member.
- `borrowed_books` (List[Book]): list of the borrowed book. This cannot exceed 3 books.

**Methods**
- `borrow_book(self, book)`: Borrow the `book` from parameter.
- `return_borrowed_book(self, book)`: return the `book` from parameter.

### Library Class

Located in `library_oop.py`, the **`Library`** class manages the core operations of the library system, including books, members, and borrowing transactions, including:

---

#### **Attributes**

- `books` (List[Book]): A list that stores all `Book` objects available in the library.

- `members` (List[Member]): A list that stores all registered `Member` objects.

- `transactions` (List[Dict]):  
  A list of dictionaries that record all active borrowing transactions.  
  Each transaction includes:
  - `member_id`
  - `book_id`
  - `member_name`
  - `book_title`

#### **Methods**

- `add_book(self, book_id, title, author, available_copies)`: Adds a new `Book` object to the `books`.  

- `add_member(self, member_id, name, email)`: Adds a new `Member` in the library system.  

- `find_book(self, book_id)`: Searches for and returns a `Book` object by its ID.  

- `find_member(self, member_id)`: Searches for and returns a `Member` object by its ID.  

- `borrow_book(self, member_id, book_id)`
  Handles the process of borrowing a book:  
  - Checks if the member and book exist.  
  - Ensures the member can borrow (via `Member.borrow_book`).  
  - Records a transaction if successful.  
  Returns `True` on success, otherwise `False`.

- `return_book(self, member_id, book_id)`  
  Handles the process of returning a borrowed book:  
  - Validates member and book.  
  - Removes the associated transaction.  
  - Calls the member’s `return_borrowed_books` method.  
  Returns `True` on success, otherwise `False`.

- `display_available_books(self)`: Displays all books in the library that have available copies left. Each book is printed using its `book_info()` method.

- `display_member_books(self, member_id)`: Displays all books currently borrowed by a specific member. Prints an error message if the member does not exist.

## Test Coverage

### **Basic Operations**
The following fundamental functions of the system are tested:
- **Adding books and members** — Verifies that books and members can be successfully registered in the library.
- **Borrowing and returning books** — Ensures that book transactions are properly handled.
- **Displaying information** — Confirms that available books and member information are displayed accurately.

### **Edge Cases**
Additional tests are performed to handle uncommon cases:
- **Borrowing unavailable books** — Prevents borrowing when no copies are left.
- **Exceeding borrowing limit** — Limits each member to a maximum of 3 borrowed books.
- **Returning books not borrowed** — Ensures users can only return books they currently hold.
- **Non-existent books or members** — Handles attempts involving IDs not registered in the system.

---

## Test Structure

### 1. **Book Class Tests**
```python
book1 = lo.Book('123', "Paruj in the wonderland", "Suwat", 20)
book2 = lo.Book('456', "Piya and the seven drawf", "tatsu", 1)
book3 = lo.Book('222', "Supaporn and the beast", "sutat", 5)
```
Tests the following:
- Book information display (`book_info()`)
- Borrowing and returning books
- Handling attempts to return already returned books or borrow unavailable copies

---

### 2. **Member Class Tests**
```python
member1 = lo.Member('007', 'Alice', 'Alice@gmail.com')
```
Covers:
- Borrowing and returning books
- Borrowing same book multiple times
- Attempting to return books not borrowed

---

### 3. **Library System Tests**

The library system (`Library`) integrates both `Book` and `Member` classes to simulate full operations.

#### **Tests Include:**
| Test No. | Description |
|-----------|--------------|
| **1** | Adding books |
| **2** | Registering members |
| **3** | Displaying available books |
| **4** | Successful borrowing |
| **5** | Displaying member's borrowed books |
| **6** | Displaying available books after borrowing |
| **7** | Borrowing the last available copy |
| **8** | Attempting to borrow unavailable books |
| **9** | Borrowing limit enforcement |
| **10** | Returning borrowed books |
| **11** | Attempting invalid returns |
| **12** | Returning and re-borrowing books |
| **13** | Handling non-existent members/books |
| **14** | Final summary of library status |

## How to Run Tests

Make sure both files are in the same directory:
```
library_oop.py
test_oop.py
```

Then, run the test file:
```bash
python test_oop.py
```

**or**

```bash
python oop_solution/test_oop.py
```
