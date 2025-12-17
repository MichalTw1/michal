import magazine.Utils


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


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student: {self.name}"


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
        return (f"Book by {self.author_name}"
                f" {self.author_surname} (from {self.library})")
