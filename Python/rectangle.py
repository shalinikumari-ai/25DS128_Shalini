class Rectangle :
    def __init__ (self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

result = Rectangle (4,5)
print(result.area())