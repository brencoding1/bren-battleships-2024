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
    BOARD_SIZE = input(" Enter your board size:\n")
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


def placing_ships():
    """
    The area the ships are put on the board.
    """
    ships_placed = 0
    global TOTAL_SHIPS
    if Y <= 3:
        TOTAL_SHIPS = 1
        while ships_placed != TOTAL_SHIPS:
            ship_row = randint(1, (Y))
            ship_col = randint(1, (Y))
            ship_location = [ship_row, ship_col]
            SHIP_PLACEMENT.append(ship_location)
            ships_placed += 1
    elif Y < 8 and Y > 3:
        TOTAL_SHIPS = 3
        while ships_placed != TOTAL_SHIPS:
            ship_row = randint(1, (Y))
            ship_col = randint(1, (Y))
            ship_location = [ship_row, ship_col]
            SHIP_PLACEMENT.append(ship_location)
            ships_placed += 1
    else:
        TOTAL_SHIPS = 10
        while ships_placed != TOTAL_SHIPS:
            ship_row = randint(1, (Y))
            ship_col = randint(1, (Y))
            ship_location = [ship_row, ship_col]
            SHIP_PLACEMENT.append(ship_location)
            ships_placed += 1
    # print(ship_placement)
    # un-comment this if you want to see where the ships are placed.


def user_guess():
    """
    The user will provide input to this function.
    Verify the input by comparing it to the ships' location.
    Capture the estimate and provide the result via the terminal.
    modifies the board based on hit or miss.
    """
    global SHIPS_SUNK
    for turn in range((Y*Y) // 2):
        shots = int((Y*Y) // 2)
        print(" ")
        print(f'  There are {shots - turn} shots left."')
        print('   How many ships remaining?"')
        print(f'  "{TOTAL_SHIPS - SHIPS_SUNK} left."')
        guess_col = None
        while True:
            guess_col = input("  Enter your column letter: ")
            if guess_col.isalpha() and len(guess_col) == 1:
                guess_col = guess_col.lower()
                guess_col = ord(guess_col) - 96
                break
            else:
                print_board()
                print(" The available letters left are....")
                continue
        guess_row = None
        while True:
            guess_row = input("  Enter row number: ")
            if guess_row.isdigit():
                guess_row = int(guess_row)
                break
            else:
                print_board()
                print("  Oops, your entry is not in range...")
                continue
        g_row = guess_row
        g_col = guess_col
        guess = [g_row, g_col]
        if guess in SHIP_PLACEMENT:
            print("-------------------------------------------------------")
            print("          Good Job! You have sank a battleship!")
            print("-------------------------------------------------------")
            BOARD[g_row - 1][g_col - 1] = "O"
            SHIPS_SUNK += 1
        elif (turn + 1) - shots == 0:
            print("-------------------------------------------------------")
            print("                   Game Over...")
            print("   Lets return to base and try again later")
            print("-------------------------------------------------------")
        elif (g_row < 1 or g_row > Y) or (g_col < 1 or g_col > Y):
            print("-------------------------------------------------------")
            print("           Your coordinates are out of range!")
            print("              You are wasting all your shots!")
            print(f"          Try to shoot within rows: 1-{Y}")
            print(f"          And the columns: A-{ALPHABET[Y - 1]}")
            print("-------------------------------------------------------")
        elif (BOARD[g_row - 1][g_col - 1]) == "X":
            print("-------------------------------------------------------")
            print("          You have already guessed that one...")
            print("-------------------------------------------------------")
        elif (BOARD[g_row - 1][g_col - 1]) == "O":
            print("-------------------------------------------------------")
            print("          You guessed that one already Sir...")
            print("-------------------------------------------------------")
        else:
            print("-------------------------------------------------------")
            print(" You have missed the battleship, let's go again!")
            print("-------------------------------------------------------")
            BOARD[g_row - 1][g_col - 1] = "X"
        if SHIPS_SUNK == TOTAL_SHIPS:
            print_board()
            print("-------------------------------------------------------")
            print("Congratulations, you have sunk all the remaining ships!")
            print("               Mission Complete!")
            print("-------------------------------------------------------")
            break
        print_board()
    turn += 1


def run_game():
    """
    Overall game is ran here. It is ran in order.
    """
    get_board_size()
    print("               Let's Begin Battleships!")
    print("-----------------------------------------------------")
    print(" ")
    print_board()
    placing_ships_ships()
    user_guess()


def restart_game():
    """
    Lets us restart game or quit to terminal.
    """
    play = input("Type yes if you would like to play again or no if you would like to quit: ").lower()
    while True:
        if play == "no":
            exit()
        elif play == "yes":
            # The restart code is from StackOverflow
            print("------------------------------------")
            print("argv was", sys.argv)
            print("sys.executable was", sys.executable)
            print("restart now")
            print("------------------------------------")
            os.execv(sys.executable, ['python'] + sys.argv)
        else:
            print("please enter either yes or no")
            restart_game()

            

# Gloabal Variables
Y = BOARD_SIZE
BOARD = []
SHIP_PLACEMENT = []
TOTAL_SHIPS = 10
SHIPS_SUNK = 0

run_game()
restart_game()