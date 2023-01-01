# Реализуйте алгоритм игры “Тайный Санта (Secret Santa)”. В шляпу кладутся небольшие записки с именами участников.
# Затем каждый играющий по очереди вытягивает бумажку с именем того, кому предстоит вручить презент.
# Ваша программа должна, используя список имен участников, выдать на выходе пары, кто и кому будет дарить,
# причем сам себе человек не может подарить, дубликаты тоже не допустимы.

# Importing
from random import choice, randrange


# Defining function
def secret_santa(players):
    if len(players) < 2:  # Length check: can't play if not enough players
        print(f"Not enough players!")
        return
    unmatched = False
    if len(players) % 2 != 0:
        found_unmatched = True
        unmatched = players.pop(randrange(len(players)))
    used_players = []  # Players who got their match
    for player in players:
        player_match = choice(players)
        while player_match == player or player_match in used_players:  # Rematching if player is matching themselves or
            # match is already taken
            player_match = choice(players)
        used_players.append(player_match)  # Match found, marking match as used
        print(f"{player}, your match is: {player_match}")  # Showing the result
    if unmatched:
        print(f"Sorry {unmatched}, you don't have a match. :(")  # If total amount of players is not even


players = []  # List of players to be handed to the main function
while True:
    player = input(f"Input player's name or 'stop' to stop inputting: ")
    if player != 'stop':
        players.append(player)
    else:
        break


# Calling out function
secret_santa(players)
