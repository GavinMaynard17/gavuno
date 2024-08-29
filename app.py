import random
from Game import Game
from Player import Player
from Card import Card

base_deck = []
colors = ['Blue', 'Green', 'Red', 'Yellow']
for i in range(4):  # Add wild cards
    base_deck.append(Card('', 'Wild', 'Wild'))
    base_deck.append(Card('', 'Draw 4', 'Wild'))
for color in colors:# Add color cards
    for i in range(2):  # Add action cards for color
        base_deck.append(Card(color, 'Draw 2', 'Action'))
        base_deck.append(Card(color, 'Skip', 'Action'))
        base_deck.append(Card(color, 'Reverse', 'Action'))
    for i in range(10):
        base_deck.append(Card(color, i, 'Number'))
        if i>0:  # 0's only get put in once
            base_deck.append(Card(color, i, 'Number'))

game = Game(base_deck)
game.add_player(Player('Gavin'))
game.add_player(Player('Bri'))
game.add_player(Player('Luke'))

for i in range(7):
    for player, player_obj in game.players.items():
        card = random.choice(game.deck)
        game.deck.remove(card)
        player_obj.add_card(card)


prev_card = random.choice(game.deck)
print(f"First card is {prev_card.color} {prev_card.value}")

while True:
    for player_name, player in game.players.items():
        print(player)
        player_input = input("Make a play! ")
        if player_input in ['Wild', 'Draw 4']:
            played_card = player.get_card('', player_input)
        else:
            color, value = player_input.split(',')
            played_card = player.get_card(color, value)
        print(played_card)

        if(prev_card.can_play(played_card)):
            prev_card = played_card
            if played_card.color == '':
                new_color = input("Pick a new color. ")
                prev_card.color = new_color
            print(f"Last played card is {prev_card.color} {prev_card.value}")
        else:
            print("Not a valid card to play!")

# Logic for playing a card
# while True:
#     played_card_str = input("Play a card! ")

#     value, color = played_card_str.split(',')
#     played_card = Card(value, color)
#     print(played_card.__dict__)

#     if(prev_card.can_play(played_card)):
#         prev_card = played_card
#         if played_card.color is '':
#             new_color = input("Pick a new color. ")
#             prev_card.color = new_color
#         print(f"Last played card is {prev_card.color} {prev_card.value}")
#     else:
#         print("Not a valid card to play!")
    
