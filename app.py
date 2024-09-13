import random
from Game import Game
from Player import Player
from Card import Card


if __name__ == "__main__":
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

    actions = {
        "Skip": game.skip_player,
        "Reverse": game.reverse,
        "Draw 2": game.add_to_draw,
        "Draw 4": game.add_to_draw
    }

    game.add_player(Player('Gavin'))
    game.add_player(Player('Bri'))
    game.add_player(Player('Luke'))

    for i in range(7):
        for player, player_obj in game.players.items():
            card = random.choice(game.deck)
            game.deck.remove(card)
            player_obj.add_card(card)


    prev_card = random.choice(game.deck)
    if prev_card.value in ["Wild", "Draw 4"]:
        prev_card.color = random.choice(colors)
    print(f"First card is {prev_card.color} {prev_card.value}")

    player = game.players[list(game.players.keys())[0]]

    while True:
        print("\n\n\n\n")
        print("Current draw pool:", game.current_draw)
        print(f"Last card played: {prev_card}")
        print(player)

        if game.current_draw > 0:
            if player.can_stack(prev_card):
                player_input = input("You can stack or you can draw, make a choice!")

            else:  # player has to draw
                game.deck, drawed_cards = player.draw_number_of_cards(game.deck, game.current_draw)
                print(f"{player.name} drew {drawed_cards} cards!")
                player = game.next_player(player.name)
                game.current_draw = 0
                continue
        else:
            player_input = input("Make a play! ")

        if player_input in ['wild', 'd4']:
            played_card = player.get_card('', player_input)

        elif player_input == "draw":  # will draw cards until player has a playable card
            if not player.has_playable(prev_card):
                print(player.name, "is drawing cards")
                game.deck, drawed_cards = player.draw_cards(game.deck, prev_card)
                print(f"{player.name} drew {drawed_cards} cards!")
                if(game.current_draw > 0):
                    game.current_draw = 0
                    player = game.next_player(player.name)
                continue
            else:
                print("You have a playable card!")
                continue

        else:
            color = player_input[0]
            value = player_input[1:]
            played_card = player.get_card(color, value)

        if not played_card:  # player tried to play a card they do not have
            print("You do not have this card!")
            continue

        if(prev_card.can_play(played_card, game.current_draw)):

            prev_card = played_card
            player.cards.remove(played_card)
            game.deck.append(played_card)

            if len(player.cards) == 0:
                game.winner = player.name
                break

            if played_card.value in actions:
                if played_card.value == "Skip":
                    print(f"Skipped {game.next_player(player.name).name}")
                    player = actions[played_card.value](player.name)
                    continue
                elif played_card.value == "Draw 4":
                    actions[played_card.value](4)
                elif played_card.value == "Draw 2":
                    actions[played_card.value](2)
                else:
                    actions[played_card.value]()

            if played_card.color == '':
                new_color = input("Pick a new color. ")
                prev_card.color = new_color

            player = game.next_player(player.name)
        else:
            print("Not a valid card to play!")
    print(f"THE WINNER IS {game.winner}")

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
    
