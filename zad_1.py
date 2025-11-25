class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average = sum(self.marks) / len(self.marks)
        return average > 50

student1 = Student("Jan Kowalski", [60, 75, 80])
student2 = Student("Anna Nowak", [40, 30, 45])

print(f"Student {student1.name}: {student1.is_passed()}")
print(f"Student {student2.name}: {student2.is_passed()}")