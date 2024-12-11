from people import *
from card import *
import json

people = []
with open('people_cards.json', 'r') as json_file:
    data = json.load(json_file)
    for adult in data:
        people.append(Adult.from_json(adult))
        
