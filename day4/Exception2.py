class InsufficientFundsError(Exception):
    pass
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        try:
            if amount < 0:
                raise ValueError("Value Error")
            if amount >  self.balance:
                raise InsufficientFundsError("Insufficient funds")
            self.balance -= amount
            return f"Remaining Balance : {self.balance}"
        
        except ValueError as e:
            return e
        except InsufficientFundsError as e:
            return e
        except Exception as e:
            return e

account = BankAccount(100)
print(account.withdraw(150))
print(account.withdraw(-10))