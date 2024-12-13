import library as lib

library = lib.Library()

b1 = library.add_book("Ugly Love", "Colleen Hoover", 5)
b2 = library.add_book("Harry potter", "J.K. Rowlling", 3)
print(b1, b2)

m1 = library.add_member("SuperCoder", "sc121@gmail.com")
m2 = library.add_member("ItsAK", "ak212@gmail.com")
print(m1, m2)

