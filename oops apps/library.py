# Library Management System
from datetime import datetime, timedelta      # date time work with realtime data
from typing import List, Optional      # type hint to improve code readability

class Book:
    def __init__(self, book_id: int, title: str, author: str, total_copies: int):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies
        self.borrowers = []    # list of member who borrowed book

    def __str__(self):
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available: {self.available_copies}/{self.total_copies}"

class Member:
    def __init__(self, member_id: int, name: str, email: str):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []   # list of borrowed books
        self.fine_amount = 0

    def __str__(self):
        return f"Member ID: {self.member_id}, Name: {self.name}, Email: {self.email}, Book Borrowed: {len(self.borrowed_books)}"

class BorrowRecord:
    def __init__(self, book: Book, member: Member):
        self.book = book
        self.member = member
        self.borrow_date = datetime.now()
        self.dur_date = self.borrow_date + timedelta(days=14)  
        self.return_date = None
        self.fine = 0

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.borrow_records = []
        self.daily_fine_rate = 2.0

    def add_book(self, title: str, author: str, total_copies: int) -> Book:
        book_id = len(self.books) + 1
        book = Book(book_id, title, author, total_copies)
        self.books.append(book)
        return book

    def add_member(self, name: str, email: str) -> Member:
        member_id = len(self.members) + 1
        member = Member(member_id, name, email)
        self.members.append(member)
        return member
        
    def find_book(self, book_id: int) -> Optional[Book]:
        return next((book for book in self.books if book.book_id == book_id), None)

    def find_member(self, member_id: int) -> Optional[Member]:
        return next((member for member in self.members if member.member_id == memberId), None)

    def borrow_book(self, book_id: int, member_id: int) -> bool:
        book = self.find_book(book_id)
        member = member.find_member(member_id)

        if not book or not member:
            return False

        if book.available_copies <= 0:
            return False

        if len(member.borrowed_books) >= 3:
            return False

        if member.fine_amount > 0:
            return False

        book.available_copies -= 1
        book.borrowers.append(member)
        member.borrowed_books.append(book)

        borrow_record = BorrowRecord(book, member)
        self.borrow_records.append(borrow_record)
        return True

    def return_book(self, book_id: int, member_id: int):
        book = self.find_book(book_id)
        member = member.find_member(member_id)

        if not book or not member or book not in member.borrowed_books:
            return 0

        borrow_record = next(
            (record for record in self.borrowed_records
            if record.book == book and record.member == member and not record.return_date),
            None
        )

        if not borrow_record:
            return 0

        borrow_record.return_date = datetime.now()

        