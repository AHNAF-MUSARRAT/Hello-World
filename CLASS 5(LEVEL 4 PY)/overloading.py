# What is Method Overloading?
# Method overloading is a feature of object-oriented programming where a class can have multiple methods with the same name but different parameters.

# Example:

class Calculator:

    def add(self, a, b, c=0, d=0):
        return a + b + c + d


calc = Calculator()

print(calc.add(5, 8))
print(calc.add(5, 10, 56))
print(calc.add(5, 10, 20, 30))

