# ticTacToe.py

# This is a two-player tic-tac-toe game. Players tell
# the computer their names and enter their moves, and
# the computer runs the game and announces the winner.

# inspired by https://automatetheboringstuff.com/chapter5/
# and also http://inventwithpython.com/chapter10.html
# but also I made (a lot of) stuff up

# created 7 Mar. 2018; last updated 15 Mar. 2018


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Definitions & Minor Functions

import random

def coinFlip():
    return random.randint(0, 1)


theBoard = {'A1': ' ', 'B1': ' ', 'C1': ' ',
            'A2': ' ', 'B2': ' ', 'C2': ' ',
            'A3': ' ', 'B3': ' ', 'C3': ' '}

labels = {'A1': 'A1', 'B1': 'B1', 'C1': 'C1',
          'A2': 'A2', 'B2': 'B2', 'C2': 'C2',
          'A3': 'A3', 'B3': 'B3', 'C3': 'C3'}

def layout(board, square):
    return "{:^3}".format(board[square])

def printBoard(board):
    print(layout(board, 'A1') + '|' + layout(board, 'B1') + '|' + layout(board, 'C1'))
    print('---+---+---')
    print(layout(board, 'A2') + '|' + layout(board, 'B2') + '|' + layout(board, 'C2'))
    print('---+---+---')
    print(layout(board, 'A3') + '|' + layout(board, 'B3') + '|' + layout(board, 'C3'))


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Major Functions

def intro():
    print("Welcome to two-player Tic-Tac-Toe!")
    print()
    print("Here's how the board is labeled:")
    printBoard(labels)
    print("Hit Enter to start game.")
    input()
    print("Let's get started!")
    print()
    
def players():    
    print("Who's playing?")
    names = []
    names.append(input("One player: ").capitalize())
    names.append(input("The other player: ").capitalize())
    print()
    return names

def firstPlayer(names):
    i = coinFlip()
    if i == 1:
        names = [names[1], names[0]]
    print(names[0], "is X and", names[1], "is O;")
    print(names[0], "goes first.")
    print()
    return names


def getMove(names, turn):
    print("It's " + names[turn] + "'s turn. Place an " + ["X", "O"][turn] + " where?")
    move = input("> ").upper()
    print()
    while move not in theBoard or theBoard[move] != " ":
        if move not in theBoard:
            print("That's not a valid space. Try again. Move on which space?")
        else:
            print("That space is already taken. Try again. Move on which space?")
        move = input().upper()
    return move

def placeMove(turn, move):
    theBoard[move] = ["X", "O"][turn]
    printBoard(theBoard)
    print()

def checkWinner(B, N): # B = board, N = names
    winner = ""
    for i in ["X", "O"]:
        if ((B["A1"] == B["A2"] == B["A3"] == i) or # columns
            (B["B1"] == B["B2"] == B["B3"] == i) or
            (B["C1"] == B["C2"] == B["C3"] == i) or
            (B["A1"] == B["B1"] == B["C1"] == i) or # rows
            (B["A2"] == B["B2"] == B["C2"] == i) or
            (B["A3"] == B["B3"] == B["C3"] == i) or
            (B["A1"] == B["B2"] == B["C3"] == i) or # diagonals
            (B["A3"] == B["B2"] == B["C1"] == i)):
                winner = i
                print("Three", winner + "s,", N[["X", "O"].index(winner)], "wins!\n")
    return winner

def nextTurn(T): # T = turn
    if T == 0:
        T = 1
    else:
        T = 0
    return T


def runGame(names):
    turn = 0
    for i in range(9):
        move = getMove(names, turn)
        placeMove(turn, move)
        winner = checkWinner(theBoard, names)
        if winner != "":
            break
        elif i == 8:
            print("Oops, looks like it's a draw!\n")
        else:
            turn = nextTurn(turn)

def playAgain(names):
    print("Game over. Play again?")
    again = input("> ").upper()[0]
    if again == "Y":
        names = [names[1], names[0]]
        print("\nOkay, new game. This time", names[0], "is X \n"
              "and", names[1], "is O, and ", names[0], "goes first.\n")
        PLAY(names)
    else:
        print("Goodbye!\n")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# The Main Function(s)

def SETUP():
    intro()
    names = firstPlayer(players())
    return names

def PLAY(names):
    runGame(names)
    playAgain(names)


def main():
    names = SETUP()
    PLAY(names)

main()
