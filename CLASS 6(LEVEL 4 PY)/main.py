 # What is Abstraction?
 # Abstraction is the process of hiding the complexity of a system by simplifying it.

 # Module of absraction
 # from abc imort ABC, abstractmethod
 # ABC = AbstractBaseClass

 # Example of Abstraction
 from abc import ABC, abstractmethod

 class ATM(ABC):
    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

# Child class where we implement all complex logic

class BankATM(ATM):
    def __init__(self, balance):
        self.balance = balance 

    def check_ balance(self):
        print(f"Current balance is: {self.balance}")

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
            print(f"You withdraw: {amount} Taka")
        else:
            print("Insufficient balance")
   def dep.osit(self, amount):

    if amount < 500:
        print("Minimum amount is 500")
    else:
        self.balance += amount
            print(f"You deposited: {amount} Taka")

atm = BankATM(1000)
atm.check_balance()
atm.deposit(500)
atm.check_balance()




