# Definition of Encapsulation:
# Encapsulation means wrapping data and methods together inside a class.

#Access Modifiers:
#1. Public: Anyone can access the data and methods from anywhere.
#2. Protected: Only the class and its subclasses can access the data and methods.
#3. Private: Only the class can access the data and methods.

# Example of Public variable:

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

stu1 = Student("Faizan", 12)
print(stu1.name)

# Example of Protected variable:

class Company:
    def __init__(self, id, salary):
        self._id = id
        self._salary = salary

class Employee (Company):
    def _init__(self, name, age, company):
        self._name = name
        self._age = age
        super().__init__(company._id, company._salary)

emp1 = Employee("Faizan", 12, Company(1, 10000))
print(empl._id)


# Example of Private variable:
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

class SavingsAccount(BankAccount):
    def _init__(self):
        super()._init__()

acc1 = BankAccount(1000)
print(acc1._balance)