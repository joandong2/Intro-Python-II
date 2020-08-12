from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside cave entrance':  Room("Outside Cave Entrance",
                                   "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'grand overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow passage':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure chamber': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside cave entrance'].n_to = room['foyer']
room['foyer'].s_to = room['outside cave entrance']
room['foyer'].n_to = room['grand overlook']
room['foyer'].e_to = room['narrow passage']
room['grand overlook'].s_to = room['foyer']
room['narrow passage'].w_to = room['foyer']
room['narrow passage'].n_to = room['treasure chamber']
room['treasure chamber'].s_to = room['narrow passage']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player("John123123", "outside cave entrance")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

is_playing = True

while is_playing:
    move = input("next move: ")

    if(move == 'q'):
        print('quitting...')
        is_playing = False
    elif(move == 'n'):
        try:
            new_room = room[player1.current_room].n_to
            print(f'currently in {new_room.name}')
            player1.current_room = new_room.name.lower()
        except AttributeError:
            print('can\'t move in that direction')
    elif(move == 's'):
        try:
            new_room = room[player1.current_room].s_to
            print(f'currently in {new_room.name}')
            player1.current_room = new_room.name.lower()
        except AttributeError:
            print('can\'t move in that direction')
    elif(move == 'w'):
        try:
            new_room = room[player1.current_room].w_to
            print(f'currently in {new_room.name}')
            player1.current_room = new_room.name.lower()
        except AttributeError:
            print('can\'t move in that direction')
    elif(move == 'e'):
        try:
            new_room = room[player1.current_room].e_to
            print(f'currently in {new_room.name}')
            player1.current_room = new_room.name.lower()
        except AttributeError:
            print('can\'t move in that direction')
    else:
        print('direction is not available')
