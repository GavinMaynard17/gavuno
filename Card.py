class Card:
    def __init__(self, color, value, type):
        self.value = value
        self.color = color
        self.type = type
        
    def __str__(self):
        if self.color == '':
            return f"{self.value}"
        return f"{self.color} {self.value}"

    def can_play(self, card, draw_amount=0):

        # if there are cards to be drawed and played card is not
        # matching the draw 4 or draw 2, false
        if draw_amount > 0 and self.value in ["Draw 4", "Draw 2"]:
            if self.value != card.value:
                return False
            
        if card.value in ["Wild", "Draw 4"]:
            return True
        
        if (self.color == card.color) or (self.value == card.value):
            return True
        return False
    
    def can_stack(self, card):
        if self.value == card.value:
            return True
        return False