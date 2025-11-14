


class abc :
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = abc ("Rachit", 23)
print(p1.name, p1.age)

class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"My name is {self.name} and I am {self.age} years old")

result = Person("Rachit", 23)
result.greet()

