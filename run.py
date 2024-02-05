"""
Battleships code file.
Player info: - The maximum size of the grid is 10 rows and 10 columns.
There will always be an equal number of rows and columns on the board.
The size selected by you will multiply by itself.
Letters are used to represent columns.
Numbers are used to represent rows.
You'll predict rows first, then columns, each time.
The battleships on the board will be concealed.
A "O" will appear if you strike a ship.
Missing a ship will result in a "X" being placed next to it.
"""

from random import randint
import os
import sys

os.system('clear')
print("                  Welcome to Battleships!")
print("-------------------------------------------------------------------")
print("         You will now create your own custom Battleship board!")
print("   You may create a Battleship board of up to 10 rows and 10 columns.")
print("   Below choose your board size by typing a number between 1 and 10,")
print("   You then may press enter to continue.")
print("-------------------------------------------------------------------")

while True:
    BOARD_SIZE = input(" Enter your board size: ")
    if BOARD_SIZE.isdigit():
        BOARD_SIZE = int(BOARD_SIZE)
        if BOARD_SIZE > 1 and BOARD_SIZE <= 10:
            print(" ")
            print("Great, let the games commence!")
            print("--------------------------------")
            break
        else:
            print("   Sorry, the number chosen has to be between 1 and 10")
    else:
        print("   Sorry, the letters and numbers cant be below 1 or above 10")
        continue



def get_board_size():
    """
    This is the global variable for the size of the board.
    The rows are made with this function.
    """
    for x in range(Y):
        BOARD.append(["-"] * Y)
    return Y


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"



def print_board():
    """
    This makes and prints the battleships board.
    """
    letters = ALPHABET[0: (Y)]
    print("      %s%s" % (" ", " ".join(letters)))
    row_number = 1
    for row in BOARD:
        if row_number <= 9:
            print("     %d|%s|" % (row_number, "|".join(row)))
        else:
            print("    %d|%s|" % (row_number, "|".join(row)))
        row_number += 1





run_game()
restart_game()