#Class
class Car:
    def __init__(self, brand, colour):
        self.brand = brand
        self.colour = colour
    def drive (self):
        print(f"{self.colour} {self.brand} is driving🚗")

#Object
car1 = Car("BMW", "Black")
car2 = Car("Tesla", "White")

car1.drive()
car2.drive()


