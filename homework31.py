class InsufficientFundsError(Exception):
   def __init__(self, message):
       self.message = message


class BankAccount:
   def __init__(self, balance=0):
       self.balance = balance

   def deposit(self, amount):
       if amount > 0:
           self.balance += amount
           return self.balance
       else:
           print("Invalid deposit amount")
           return self.balance

   def withdraw(self, amount):
       if amount > self.balance:
           raise InsufficientFundsError(f"Insufficient funds. Current balance: {self.balance}")
       elif amount <= 0:
           print("Invalid withdrawal amount")
           return self.balance
       else:
           self.balance -= amount
           return self.balance
