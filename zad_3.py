class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

class House(Property):
    def __init__(self, area, rooms, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House at {self.address}, Area: {self.area}, Rooms: {self.rooms}, Plot: {self.plot}"

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat at {self.address}, Area: {self.area}, Rooms: {self.rooms}, Floor: {self.floor}"

house = House(150, 5, 500000, "Kwiatowa 1", 1000)
flat = Flat(60, 3, 300000, "Polna 5", 2)

print(house)
print(flat)