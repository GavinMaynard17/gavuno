class Game:
    def __init__(self, deck):
        self.players = {}
        self.direction = True
        self.winner = ""
        self.deck = deck

    def add_player(self, player):
        self.players.update({player.name: player})

    def print_deck(self):
        print(', '.join(str(card) for card in self.deck))
        