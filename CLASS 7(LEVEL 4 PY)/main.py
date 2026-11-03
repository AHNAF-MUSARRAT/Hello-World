# What is polymorphism?
# Polymorphism is the abilityof an object to take on many forms
# Polymorphism is used in oop to achieve code re-usability

# Types of Polymorphism
# 1. Method overriding
# 2. Method overloading

# Polymorphism using Inheritance
# Parent class and child class method behavior is same
# Child class name, different implementation
# Calling methods using different objects

# Project Example:

class animal:
    def sound(self):
        print("Animal is making sound")

class Dog(Animal):
    def sound(self):
        print("Dog is barking")

class Cat(Animal):
    def sound(self):
        print("Cat is meowing")

dog = Dog()
car = Cat()
dog.sound()
cat.sound()
