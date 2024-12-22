import library as lib

library = lib.Library()

try:
    b1 = library.add_book("Ugly Love", "Colleen Hoover", 5)
    b2 = library.add_book("Harry Potter", "J.K. Rowling", 3)
    print(b1, b2)
except Exception as e:
    print(f"Error adding books: {e}")

try:
    m1 = library.add_member("SuperCoder", "sc121@gmail.com")
    m2 = library.add_member("ItsAK", "ak212@gmail.com")
    print(m1, m2)
except Exception as e:
    print(f"Error adding members: {e}")

# Display the list of books
print("Books in the library:")
for book in library.books:
    print(book)

# Display the list of members
print("Members in the library:")
for member in library.members:
    print(member)

