# What is a Method Overriding?
# Method overriding is a feature of object-oriented programming where a child class can provide a different implementatio of a method that is already defined in its parent class.

# Example:

class Animal:
    def sound(self):
        print("The animal makes a generic sound")

class Cat(Animal):
    def sound(self):
        print("The cat makes a meow sound")

cat = Cat()
cat.sound()