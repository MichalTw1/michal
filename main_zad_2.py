import magazine.Products
import magazine.Order
import magazine.Utils


lib1 = magazine.Utils.Library("Warsaw", "Main St", "00-001", "8-16", "123456")

emp1 = magazine.Products.Employee(
    "John",
    "Doe",
    "2020-01-01",
    "1990-05-05",
    "Warsaw",
    "Side St",
    "00-002",
    "111"
)
stud1 = magazine.Products.Student(
    "Alice",
    []
)
book1 = magazine.Products.Book(
    lib1,
    "2000",
    "Adam",
    "Mickiewicz",
    300
)

order1 = magazine.Order.Order(emp1, stud1, [book1], "2023-10-01")

print(order1)
