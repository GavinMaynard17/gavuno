import random

class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []

    def __str__(self):
        cards_str = ', '.join(str(card) for card in self.cards)
        return f"{self.name}: [{cards_str}]"

    def add_card(self, card):
        self.cards.append(card)

    def get_card(self, color, value):
        if value in value_map:
            value = value_map[value]
        
        for card in self.cards:
            if (card.color == color_map[color]) and (str(card.value) == value):
                return card
            
        return None
    
    def draw_cards(self, deck, last_card):
        count = 0
        while True:
            count = count+1
            drawed_card = random.choice(deck)
            self.cards.append(drawed_card)
            deck.remove(drawed_card)
            if last_card.can_play(drawed_card):
                return deck, count
    
    def draw_number_of_cards(self, deck, amount):
        count = 0
        while count < amount:
            count = count+1
            drawed_card = random.choice(deck)
            self.cards.append(drawed_card)
            deck.remove(drawed_card)
        return deck, count
    

    def has_playable(self, last_card):
        for card in self.cards:
            if last_card.can_play(card):
                return True
            
        return False
    
    def can_stack(self, last_card):
        for card in self.cards:
            if last_card.can_stack(card):
                return True

color_map = {
            'y': "Yellow",
            'r': "Red",
            'b': "Blue",
            'g': "Green",
            '': ""
}

value_map = {
    'd2': "Draw 2",
    'd4': "Draw 4",
    'wild': "Wild",
    'rev': "Reverse",
    's': "Skip"
}