import library_oop as lo

# Test Code for Object Oriented Library System

#TEST book class
book1 = lo.Book(123, "Paruj in the wonderland", "Suwat", 20)
book2 = lo.Book(456, "Piya and the seven drawf", "tatsu", 1)

#Test take and return book
book1.display_info()
book1.take_book()
book1.display_info()
book1.return_book()
book1.display_info()

#Test book error
book1.return_book()
book2.display_info()
book2.take_book()
book2.take_book()
book2.display_info()