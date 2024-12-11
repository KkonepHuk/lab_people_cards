class Card:
    def __init__(self, number, balance, limit = None):
        self.number = number
        self.balance = balance
        self.limit = limit

    @classmethod
    def form_card(cls, card):
        if 'limit' in card:
            return cls(card['number'], card['balance'], card['limit'])
        return cls(card['number'], card['balance'])

    def get(self, amount):
        self.balance += amount
        
    def spend(self, price):
        self.balance -= price

    def show_info(self):
        if self.limit == None:
            return f'Number - {self.number}, Balance - {self.balance}'
        return f'Number - {self.number}, Balance - {self.balance}, Limit - {self.limit}'

    def __str__(self):
        return self.show_info()
    
    def __repr__(self):
        return self.show_info()
    
    