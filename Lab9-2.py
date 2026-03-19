class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author: ")
        self.books.append(Book(title, author))
        print("Book added successfully!")

    def add_member(self):
        name = input("Enter member name: ")
        self.members.append(Member(name))
        print("Member added successfully!")

    def lend_book(self):
        title = input("Enter book title: ")
        name = input("Enter member name: ")

        for b in self.books:
            if b.title == title and b.available:
                for m in self.members:
                    if m.name == name:
                        b.available = False
                        m.borrowed_books.append(b.title)
                        print("Book issued successfully!")
                        return
        print("Book not available")

    def return_book(self):
        title = input("Enter book title: ")

        for b in self.books:
            if b.title == title:
                b.available = True
                print("Book returned successfully!")
                return
        print("Book not found")

    def display_books(self):
        print("\n--- Book List ---")
        for b in self.books:
            status = "Available" if b.available else "Issued"
            print(b.title, "-", b.author, "-", status)

lib = Library()

while True:
    print("\n1.Add Book  2.Add Member  3.Lend Book")
    print("4.Return Book  5.Display Books  6.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        lib.add_book()
    elif choice == 2:
        lib.add_member()
    elif choice == 3:
        lib.lend_book()
    elif choice == 4:
        lib.return_book()
    elif choice == 5:
        lib.display_books()
    elif choice == 6:
        break
    else:
        print("Invalid choice")