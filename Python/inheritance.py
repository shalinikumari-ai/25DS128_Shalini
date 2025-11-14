class Animal :
    def speaks(self):
        print("Animal speaks")
class Dog(Animal):
    def speaks(self):
        print("Dog barks 🐶")

dog = Dog()
dog.speaks()

class Cat:
    def sound(self):
        return "Meow 🐱"

class Dog:
    def sound(self):
        return "Woof🐶"

for animal in [Cat(), Dog()]:
    print(animal.sound())