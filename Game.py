class Game:
    def __init__(self, deck):
        self.players = {}
        self.direction = True
        self.winner = ""
        self.deck = deck
        self.current_draw = 0

    def add_player(self, player):
        self.players.update({player.name: player})

    def print_deck(self):
        print(', '.join(str(card) for card in self.deck))
    
    def next_player(self, name):
        player_list = list(self.players.keys())
        
        # Find the current player's index
        current_index = player_list.index(name)
        
        # Calculate the next player's index based on the direction
        if self.direction:
            next_index = (current_index + 1) % len(player_list)
        else:
            next_index = (current_index - 1) % len(player_list)
        
        return self.players[player_list[next_index]]
    
    def reverse(self):
        if self.direction:
            self.direction = False
            return
        self.direction = True

    def skip_player(self, name):
        player_list = list(self.players.keys())
        
        # Find the current player's index
        current_index = player_list.index(name)
        
        # Calculate the next player's index based on the direction
        if self.direction:
            next_index = (current_index + 2) % len(player_list)
        else:
            next_index = (current_index - 2) % len(player_list)
        
        return self.players[player_list[next_index]]
    
    def add_to_draw(self, amount):
        self.current_draw = self.current_draw + amount
