class Account:
    def __init__(self, title = None, balance = 0):
        self.title = title
        self.balance = balance


class savingsAccounts(Account):

    def __init__(self, title = None, balance = 0, interestRate = 0):
        super().__init__(title, balance)
        self.interestRate = interestRate

s = savingsAccounts("Ashish", 5000, 5)
print(s.title)
print(s.balance)
print(s.interestRate)
















   
