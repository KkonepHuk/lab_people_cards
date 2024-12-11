class Savings_account:
    def __init__(self, balance = 0, percent = 0):
        self.balance = balance
        self.percent = percent

    def top_up(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

    def show_info(self):
        s = f'Balance - {self.balance}, Percent - {self.percent}%'
        return s
    
    def __str__(self):
        return self.show_info()
    
    def __repr__(self):
        return self.show_info()
