class Card:
    def __init__(self, color, value, type):
        self.value = value
        self.color = color
        self.type = type
        
    def __str__(self):
        if self.color == '':
            return f"{self.value}"
        return f"{self.color} {self.value}"

    def can_play(self, card):
        if card.value == 'Wild':
            return True
        if (self.color == card.color) or (self.value == card.value):
            return True
        return False