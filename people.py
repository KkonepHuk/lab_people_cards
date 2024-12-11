import random
import main
from card import *

class Person:
    def __init__(self, first_name, last_name, cards, age = None):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
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

    def __str__(self):
        return self.show_info()
    
    def __repr__(self):
        return self.show_info()
    
class Adult(Person):
    def __init__(self, last_name, first_name, cards, children, age = None, ident = None):
        super().__init__(last_name, first_name, cards, age)
        self.ident = self.generate_ident()
        self.children = [Child.form_child(child) for child in children]
        for card in self.cards:
            card.ident = self.ident

    
    @classmethod
    def from_json(cls, adult):
        return cls(adult['last_name'], adult['first_name'], adult['cards'], adult['children'])

        

    def give_money_to_child(self, amount):
        self.cards[0].spend(amount)
        self.children[0].cards[0].get(amount)
        
    def show_info(self):
        s = f'{self.first_name} {self.last_name}\n'
        s += f'Cards: {";\n".join([str(card) for card in self.cards])}\n'
        s += f'Children: {"\n".join([str(child) for child in self.children])}'
        return s
    
class Child(Person):
    def __init__(self, first_name, last_name, cards, age):
        super().__init__(first_name, last_name, cards, age)

    @classmethod
    def form_child(cls, child):
        return cls(child['first_name'], child['last_name'], child['cards'], child['age'])

    def show_info(self):
        s = f'{self.first_name} {self.last_name}, {self.age} y.o.\n'
        s += f'Cards: {";\n".join([str(card) for card in self.cards])}'
        return s
    

    
