import magazine.Utils


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_list = ", ".join([str(b) for b in self.books])
        return (f"Order by {self.student} handled by"
                f" {self.employee}. Books: {book_list}")
