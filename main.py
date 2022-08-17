# Tic-tac-toe game

# Created by Botan Bulut - 16, August 2022

#imports:
import random
# Setting the tic-tac-toe board and mechanics

gameStatus = True
possible_locations = [1, 2, 3, 4, 5, 6, 7, 8, 9]
playerStatus = None
botStatus = None

def win_check(x):
    """Checks whether a win occured or not returns True if win occured. There are 8 unique index-wise win combiantions."""
    if (x[0] == "X" and x[3] == "X" and x[6] == "X") or (x[0] == "O" and x[3] == "O" and x[6] == "O"):
        return True
    elif (x[0] == "X" and x[4] == "X" and x[8] == "X") or (x[0] == "O" and x[4] == "O" and x[8] == "O"):
        return True
    elif (x[0] == "X" and x[1] == "X" and x[2] == "X") or (x[0] == "O" and x[1] == "O" and x[2] == "O"):
        return True
    elif (x[1] == "X" and x[4] == "X" and x[7] == "X") or (x[1] == "O" and x[4] == "O" and x[7] == "O"):
        return True
    elif (x[3] == "X" and x[4] == "X" and x[5] == "X") or (x[3] == "O" and x[4] == "O" and x[5] == "O"):
        return True
    elif (x[6] == "X" and x[7] == "X" and x[8] == "X") or (x[6] == "O" and x[7] == "O" and x[8] == "O"):
        return True
    elif (x[2] == "X" and x[5] == "X" and x[8] == "X") or (x[2] == "O" and x[5] == "O" and x[8] == "O"):
        return True
    elif (x[2] == "X" and x[4] == "X" and x[6] == "X") or (x[2] == "O" and x[4] == "O" and x[6] == "O"):
        return True
    else:
        return False


def display_board(location):
    """This function displays the game board"""
    print(location[0 : 3: ])
    print(location[3: 6: ])
    print(location[6: :])

print("Welcome to my tic-tac-toe game. Your aim is to defeat your opponent by lining up 3 \"X\" together either diagnoal, horizontal or vertically.")
print("Possible Locations are given below: ")
display_board(possible_locations)
print("\n")

gameBoard = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
print("Initial game status is: ")
display_board(gameBoard)
print("\n")

while gameStatus != False: # Total game loop happens here
    userInput = int(input("Enter location: "))
   
    while userInput not in possible_locations:
        print("possible locations are:", *possible_locations)
        userInput = int(input("Enter a possible location: "))
    
    possible_locations.remove(userInput)
    gameBoard[userInput - 1] = "X"
    display_board(gameBoard)
    print("\n")
    # Cheking for player win
    playerStatus = win_check(gameBoard)
    if playerStatus == True:
        print("Player win!")
        break
        
    
    #Bot
    if len(possible_locations) != 0:
        botInput = random.randint(1, 9)
    
        while botInput not in possible_locations:
            botInput = random.randint(1, 9)
    
        possible_locations.remove(botInput)
        print("Bot Played: ")
        gameBoard[botInput -1] = "O"
        display_board(gameBoard)
        print("\n")

        # Bot win check
        botStatus = win_check(gameBoard)
        if botStatus == True:
            print("Bot wins!")
            break

    else:
        print("Draw!")
        break

