# Python-Bootcamp-Milestone-Project-1
Milestone project 1 for Python Bootcamp


Our aim is to create a tic-tac-toe game using Python language. Program will have a function that will take user input and update visual (conventional 3x3 tic-tac-toe matrix) accordingly.

_______________________________________________________________________________________________________________________________________________________________________
PSEUDOCODE

gameboard will have a design like this:
[" ", " ", " "]
[" ", " ", " "]
[" ", " ", " "]

this design is important and will be printed by function. Thefunction will take a list as an argument:

gameboard = [" ", ... , " "] (1x9) list.

User will enter a location for his/her selection of mark. There are 9 possible locations:
[1, 2, 3,]
[4, 5, 6]
[7, 8, 9]

When user enter 5, for instance, we will update the list as shown below:
[" ", " ", " "]
[" ", "X", " "] ---> Here location 5 corresponds to gameboard[4] user input updates gameboard and removes the imput value from the list.
[" ", " ", " "]

Same logic will be applied for the opponent (bot).
_______________________________________________________________________________________________________________________________________________________________________
Winning conditions are summerized below:

2 diagnoal
3 vertical --> Uniquely
3 horizontal
These are all possible winning conditions. Winning conditions will be checked index-wise. Index-wise player generate a list and if the sorted list matches one of winning conditions then game will end so does the loop (gamestatus = False).


There may be a draw. In that case, all possible location list will be empty list and hence draw will occur.
_______________________________________________________________________________________________________________________________________________________________________
