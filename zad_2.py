class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library in {self.city}, {self.street}"


class Employee:
    def __init__(
            self,
            first_name,
            last_name,
            hire_date,
            birth_date,
            city,
            street,
            zip_code,
            phone
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}"


class Book:
    def __init__(
            self,
            library,
            publication_date,
            author_name,
            author_surname,
            number_of_pages
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f"Book by {self.author_name} {self.author_surname}"
                f" (from {self.library})")


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student: {self.name}"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_list = ", ".join([str(b) for b in self.books])
        return (f"Order by {self.student} handled by "
                f"{self.employee}. Books: {book_list}")


lib1 = Library("Warsaw", "Main St", "00-001", "8-16", "123456")
lib2 = Library("Krakow", "Old St", "30-001", "9-17", "654321")

emp1 = Employee(
    "John",
    "Doe",
    "2020-01-01",
    "1990-05-05",
    "Warsaw",
    "Side St",
    "00-002",
    "111"
)
emp2 = Employee(
    "Jane",
    "Smith",
    "2021-02-01",
    "1992-06-06",
    "Krakow",
    "New St",
    "30-002",
    "222"
)
emp3 = Employee(
    "Bob",
    "Brown",
    "2019-03-01",
    "1988-07-07",
    "Warsaw",
    "Big St",
    "00-003",
    "333"
)

stud1 = Student("Alice", [])
stud2 = Student("Mike", [])
stud3 = Student("Eve", [])

book1 = Book(lib1, "2000", "Adam", "Mickiewicz", 300)
book2 = Book(lib1, "2005", "Juliusz", "Slowacki", 250)
book3 = Book(lib2, "2010", "Henryk", "Sienkiewicz", 400)
book4 = Book(lib2, "2015", "Boleslaw", "Prus", 350)
book5 = Book(lib1, "2020", "Stefan", "Zeromski", 200)

order1 = Order(emp1, stud1, [book1, book2], "2023-10-01")
order2 = Order(emp2, stud2, [book3], "2023-10-02")

print(order1)
print(order2)
