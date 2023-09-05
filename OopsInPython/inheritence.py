#define a base class named "Animal" with the attributes 'name'
class Animal:
    def __init__(self, name):
        self.name=name
#create a method speak that prings a generic animal sound
    def speak(self):
        print("Animal sound")
#crate a derived class Dog that inherits from animal.
class Dog(Animal):
    def speak(self):
        print("Bhaun Bhaun")

#crate a derived class Cat that inherits from animal.
class Cat(Animal):
    def speak(self):
        print("Meow Meow")

dog = Dog(name="Saif")
cat = Cat(name="Akansha")

dog.speak()
cat.speak()
        