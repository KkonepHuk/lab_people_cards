import random
from card import *
from savings_accounts import *

class Person:
    def __init__(self, first_name, last_name, cards, age = None, savings_account = None):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.savings_account = savings_account
        self.cards = [Card.form_card(card) for card in cards]

    def purchase(self):
        goods = ['hat', 'boots', 'food', 'glasses']
        good = random.choice(goods)
        lim = self.cards[0].balance
        if self.cards[0].limit != None and self.cards[0].limit < lim:
            lim = self.cards[0].limit
        price = random.randint(1, int(lim) - 1)

        if self.age == None:
            s = f'{self.first_name} {self.last_name} makes a purchase: {good}\n'
        else:
            s = f'{self.first_name} {self.last_name}, {self.age} y.o. makes a purchase: {good}\n'
        s += f'Price: {price}'

        self.cards[0].spend(price)
        return s
    
    def create_savings_account(self, start_balance = 0, percent = 0):
        self.savings_account = Savings_account(start_balance, percent)
        self.cards[0].spend(start_balance)

    def get_money(self, amount):
        if self.savings_account == None:
            self.cards[0].get(amount)
        else:
            deduction = amount * self.savings_account.percent / 100
            self.savings_account.top_up(deduction)
            self.cards[0].get(amount - deduction)

    def __str__(self):
        return self.show_info()
    
    def __repr__(self):
        return self.show_info()
    
class Adult(Person):
    def __init__(self, last_name, first_name, cards, children, age = None, savings_account = None):
        super().__init__(last_name, first_name, cards, age, savings_account)
        self.children = [Child.form_child(child) for child in children]

    
    @classmethod
    def from_json(cls, adult):
        return cls(adult['last_name'], adult['first_name'], adult['cards'], adult['children'])

        

    def give_money_to_child(self, amount):
        self.cards[0].spend(amount)
        self.children[0].get_money(amount)
        
    def show_info(self):
        s = f'{self.first_name} {self.last_name}\n'
        s += f'Cards: {";\n".join([str(card) for card in self.cards])}\n'
        if self.savings_account != None:
            s += f'Savings account: {str(self.savings_account)}\n'
        s += f'Children: {"\n".join([str(child) for child in self.children])}'
        return s
    
class Child(Person):
    def __init__(self, first_name, last_name, cards, age, savings_account = None):
        super().__init__(first_name, last_name, cards, age, savings_account = None)

    @classmethod
    def form_child(cls, child):
        return cls(child['first_name'], child['last_name'], child['cards'], child['age'])

    def show_info(self):
        s = f'{self.first_name} {self.last_name}, {self.age} y.o.\n'
        s += f'Cards: {";\n".join([str(card) for card in self.cards])}'
        if self.savings_account != None:
            s += f'Savings account: {str(self.savings_account)}'
        return s
    

    
