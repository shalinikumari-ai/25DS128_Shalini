class Animal:
    def speak(self):
        print("Animal make different sound")
class dog(Animal):
    def speak(self):
        print("Dog barks")
class cat(Animal):
    def speak(self):
        print("Cat meows")
for pet in (dog(),cat()):
    pet.speak()