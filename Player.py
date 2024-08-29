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
        for card in self.cards:
            if (card.color == color) and (str(card.value) == value):
                return card
            
        return None