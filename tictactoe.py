# Imports
import random

board = [[ 0 for x in range(3)] for y in range(3)] # 3x3 nested list
player = ' x ' # set to ' o ' for player O  and ' x ' for player X.
filledBoxes = [[ 0 for x in range(3)] for y in range(3)] # 3x3 nested list for valid checks and AI moves
quitting = False

def setupBoard():
    board[0][0] = ' 1 '
    board[0][1] = ' 2 '
    board[0][2] = ' 3 '
    board[1][0] = ' 4 '
    board[1][1] = ' 5 '
    board[1][2] = ' 6 '
    board[2][0] = ' 7 '
    board[2][1] = ' 8 '
    board[2][2] = ' 9 '

    filledBoxes[0][0] = 0
    filledBoxes[0][1] = 0
    filledBoxes[0][2] = 0
    filledBoxes[1][0] = 0
    filledBoxes[1][1] = 0
    filledBoxes[1][2] = 0
    filledBoxes[2][0] = 0
    filledBoxes[2][1] = 0
    filledBoxes[2][2] = 0

def displayBoard():
    print()
    for r in range(3):
        print(" ", end="")
        for c in range(3):
            print(board[r][c], end="")
            if c < 2:
                print("|", end="")
        print()
        if(r < 2):
            print(" ---|---|---")

def validMove(move):
    flag = False

    if move == 1:
        if filledBoxes[0][0] == 0:
            flag = True
    elif move == 2:
        if filledBoxes[0][1] == 0:
            flag = True
    elif move == 3:
        if filledBoxes[0][2] == 0:
            flag = True
    elif move == 4:
        if filledBoxes[1][0] == 0:
            flag = True
    elif move == 5:
        if filledBoxes[1][1] == 0:
            flag = True
    elif move == 6:
        if filledBoxes[1][2] == 0:
            flag = True
    elif move == 7:
        if filledBoxes[2][0] == 0:
            flag = True
    elif move == 8:
        if filledBoxes[2][1] == 0:
            flag = True
    elif move == 9:
        if filledBoxes[2][2] == 0:
            flag = True
    elif move == 0:
        flag = True

    return flag

def win(playerXO):
    global quitting
    global player

    player = ' o '

    displayBoard()

    if playerXO == "x":
        print("Player x won!")
    elif playerXO == "o":
        print("Player o won!")
    elif playerXO == "t":
        print("Tie!")

    data = input("Enter 1 to play again, 0 to quit: ")

    while data.isnumeric() == False or int(data) not in [0, 1]:
        data = input("Error: enter 1 to play again, 0 to quit: ")

    if int(data) == 0:
        quitting = True
    elif int(data) == 1:
        setupBoard()

def gameReporter():
    if filledBoxes[0][0] == 1 and filledBoxes[0][1] == 1 and filledBoxes[0][2] == 1:
        win("x")
    elif filledBoxes[0][0] == 2 and filledBoxes[0][1] == 2 and filledBoxes[0][2] == 2:
        win("o")
    elif filledBoxes[1][0] == 1 and filledBoxes[1][1] == 1 and filledBoxes[1][2] == 1:
        win("x")
    elif filledBoxes[1][0] == 2 and filledBoxes[1][1] == 2 and filledBoxes[1][2] == 2:
        win("o")
    elif filledBoxes[2][0] == 1 and filledBoxes[2][1] == 1 and filledBoxes[2][2] == 1:
        win("x")
    elif filledBoxes[2][0] == 2 and filledBoxes[2][1] == 2 and filledBoxes[2][2] == 2:
        win("o")
    elif filledBoxes[0][0] == 1 and filledBoxes[1][0] == 1 and filledBoxes[2][0] == 1:
        win("x")
    elif filledBoxes[0][0] == 2 and filledBoxes[1][0] == 2 and filledBoxes[2][0] == 2:
        win("o")
    elif filledBoxes[0][1] == 1 and filledBoxes[1][1] == 1 and filledBoxes[2][1] == 1:
        win("x")
    elif filledBoxes[0][1] == 2 and filledBoxes[1][1] == 2 and filledBoxes[2][1] == 2:
        win("o")
    elif filledBoxes[0][2] == 1 and filledBoxes[1][2] == 1 and filledBoxes[2][2] == 1:
        win("x")
    elif filledBoxes[0][2] == 2 and filledBoxes[1][2] == 2 and filledBoxes[2][2] == 2:
        win("o")
    elif filledBoxes[0][0] == 1 and filledBoxes[1][1] == 1 and filledBoxes[2][2] == 1:
        win("x")
    elif filledBoxes[0][0] == 2 and filledBoxes[1][1] == 2 and filledBoxes[2][2] == 2:
        win("o")
    elif filledBoxes[0][2] == 1 and filledBoxes[1][1] == 1 and filledBoxes[2][0] == 1:
        win("x")
    elif filledBoxes[0][2] == 2 and filledBoxes[1][1] == 2 and filledBoxes[2][0] == 2:
        win("o")
    
    tie = True
    for row in filledBoxes:
        for block in row:
            if block == 0:
                tie = False

    if tie == True:
        win("t")

def turn(playerXO):
    loc = 0

    if playerXO == ' x ':
        print()
        data = input("please enter 1-9 to make your move (0 to quit): ")

        while data.isnumeric() == False or validMove(int(data)) == False:
            if data.isnumeric() == False:
                data = input("Error: enter 1-9 to make your move (0 to quit): ")
            elif validMove(int(data)) == False:
                data = input("Not a valid move. Enter 1-9 to make your move (0 to quit): ")

        loc = int(data)

    if playerXO == ' o ':
        print()
        print("Player o is making a move...")
        loc = makeMove()

    if loc == 1:
        board[0][0] = playerXO
        if playerXO == ' x ':
            filledBoxes[0][0] = 1
        else:
            filledBoxes[0][0] = 2
    elif loc == 2:
        board[0][1] = playerXO
        if playerXO == ' x ':
            filledBoxes[0][1] = 1
        else:
            filledBoxes[0][1] = 2
    elif loc == 3:
        board[0][2] = playerXO
        if playerXO == ' x ':
            filledBoxes[0][2] = 1
        else:
            filledBoxes[0][2] = 2
    elif loc == 4:
        board[1][0] = playerXO
        if playerXO == ' x ':
            filledBoxes[1][0] = 1
        else:
            filledBoxes[1][0] = 2
    elif loc == 5:
        board[1][1] = playerXO
        if playerXO == ' x ':
            filledBoxes[1][1] = 1
        else:
            filledBoxes[1][1] = 2
    elif loc == 6:
        board[1][2] = playerXO
        if playerXO == ' x ':
            filledBoxes[1][2] = 1
        else:
            filledBoxes[1][2] = 2
    elif loc == 7:
        board[2][0] = playerXO
        if playerXO == ' x ':
            filledBoxes[2][0] = 1
        else:
            filledBoxes[2][0] = 2
    elif loc == 8:
        board[2][1] = playerXO
        if playerXO == ' x ':
            filledBoxes[2][1] = 1
        else:
            filledBoxes[2][1] = 2
    elif loc == 9:
        board[2][2] = playerXO
        if playerXO == ' x ':
            filledBoxes[2][2] = 1
        else:
            filledBoxes[2][2] = 2

    gameReporter()

    return loc

def blockMove():
    if filledBoxes[0][0] == 1 and filledBoxes[0][1] == 1 and filledBoxes[0][2] == 0:
        return 3
    elif filledBoxes[0][0] == 1 and filledBoxes[0][1] == 0 and filledBoxes[0][2] == 1:
        return 2
    elif filledBoxes[0][0] == 0 and filledBoxes[0][1] == 1 and filledBoxes[0][2] == 1:
        return 1
    elif filledBoxes[1][0] == 1 and filledBoxes[1][1] == 1 and filledBoxes[1][2] == 0:
        return 6
    elif filledBoxes[1][0] == 1 and filledBoxes[1][1] == 0 and filledBoxes[1][2] == 1:
        return 5
    elif filledBoxes[1][0] == 0 and filledBoxes[1][1] == 1 and filledBoxes[1][2] == 1:
        return 4
    elif filledBoxes[2][0] == 1 and filledBoxes[2][1] == 1 and filledBoxes[2][2] == 0:
        return 9
    elif filledBoxes[2][0] == 1 and filledBoxes[2][1] == 0 and filledBoxes[2][2] == 1:
        return 8
    elif filledBoxes[2][0] == 0 and filledBoxes[2][1] == 1 and filledBoxes[2][2] == 1:
        return 7
    elif filledBoxes[0][0] == 1 and filledBoxes[1][0] == 1 and filledBoxes[2][0] == 0:
        return 7
    elif filledBoxes[0][0] == 1 and filledBoxes[1][0] == 0 and filledBoxes[2][0] == 1:
        return 4
    elif filledBoxes[0][0] == 0 and filledBoxes[1][0] == 1 and filledBoxes[2][0] == 1:
        return 1
    elif filledBoxes[0][1] == 1 and filledBoxes[1][1] == 1 and filledBoxes[2][1] == 0:
        return 8
    elif filledBoxes[0][1] == 1 and filledBoxes[1][1] == 0 and filledBoxes[2][1] == 1:
        return 5
    elif filledBoxes[0][1] == 0 and filledBoxes[1][1] == 1 and filledBoxes[2][1] == 1:
        return 2
    elif filledBoxes[0][2] == 1 and filledBoxes[1][2] == 1 and filledBoxes[2][2] == 0:
        return 9
    elif filledBoxes[0][2] == 1 and filledBoxes[1][2] == 0 and filledBoxes[2][2] == 1:
        return 6
    elif filledBoxes[0][2] == 0 and filledBoxes[1][2] == 1 and filledBoxes[2][2] == 1:
        return 3
    elif filledBoxes[0][0] == 1 and filledBoxes[1][1] == 1 and filledBoxes[2][2] == 0:
        return 9
    elif filledBoxes[0][0] == 1 and filledBoxes[1][1] == 0 and filledBoxes[2][2] == 1:
        return 5
    elif filledBoxes[0][0] == 0 and filledBoxes[1][1] == 1 and filledBoxes[2][2] == 1:
        return 1
    elif filledBoxes[0][2] == 1 and filledBoxes[1][1] == 1 and filledBoxes[2][0] == 0:
        return 7
    elif filledBoxes[0][2] == 1 and filledBoxes[1][1] == 0 and filledBoxes[2][0] == 1:
        return 5
    elif filledBoxes[0][2] == 0 and filledBoxes[1][1] == 1 and filledBoxes[2][0] == 1:
        return 3
    else:
        return -1

def winningMove():
    if filledBoxes[0][0] == 2 and filledBoxes[0][1] == 2 and filledBoxes[0][2] == 0:
        return 3
    elif filledBoxes[0][0] == 2 and filledBoxes[0][1] == 0 and filledBoxes[0][2] == 2:
        return 2
    elif filledBoxes[0][0] == 0 and filledBoxes[0][1] == 2 and filledBoxes[0][2] == 2:
        return 1
    elif filledBoxes[1][0] == 2 and filledBoxes[1][1] == 2 and filledBoxes[1][2] == 0:
        return 6
    elif filledBoxes[1][0] == 2 and filledBoxes[1][1] == 0 and filledBoxes[1][2] == 2:
        return 5
    elif filledBoxes[1][0] == 0 and filledBoxes[1][1] == 2 and filledBoxes[1][2] == 2:
        return 4
    elif filledBoxes[2][0] == 2 and filledBoxes[2][1] == 2 and filledBoxes[2][2] == 0:
        return 9
    elif filledBoxes[2][0] == 2 and filledBoxes[2][1] == 0 and filledBoxes[2][2] == 2:
        return 8
    elif filledBoxes[2][0] == 0 and filledBoxes[2][1] == 2 and filledBoxes[2][2] == 2:
        return 7
    elif filledBoxes[0][0] == 2 and filledBoxes[1][0] == 2 and filledBoxes[2][0] == 0:
        return 7
    elif filledBoxes[0][0] == 2 and filledBoxes[1][0] == 0 and filledBoxes[2][0] == 2:
        return 4
    elif filledBoxes[0][0] == 0 and filledBoxes[1][0] == 2 and filledBoxes[2][0] == 2:
        return 1
    elif filledBoxes[0][1] == 2 and filledBoxes[1][1] == 2 and filledBoxes[2][1] == 0:
        return 8
    elif filledBoxes[0][1] == 2 and filledBoxes[1][1] == 0 and filledBoxes[2][1] == 2:
        return 5
    elif filledBoxes[0][1] == 0 and filledBoxes[1][1] == 2 and filledBoxes[2][1] == 2:
        return 2
    elif filledBoxes[0][2] == 2 and filledBoxes[1][2] == 2 and filledBoxes[2][2] == 0:
        return 9
    elif filledBoxes[0][2] == 2 and filledBoxes[1][2] == 0 and filledBoxes[2][2] == 2:
        return 6
    elif filledBoxes[0][2] == 0 and filledBoxes[1][2] == 2 and filledBoxes[2][2] == 2:
        return 3
    elif filledBoxes[0][0] == 2 and filledBoxes[1][1] == 2 and filledBoxes[2][2] == 0:
        return 9
    elif filledBoxes[0][0] == 2 and filledBoxes[1][1] == 0 and filledBoxes[2][2] == 2:
        return 5
    elif filledBoxes[0][0] == 0 and filledBoxes[1][1] == 2 and filledBoxes[2][2] == 2:
        return 1
    elif filledBoxes[0][2] == 2 and filledBoxes[1][1] == 2 and filledBoxes[2][0] == 0:
        return 7
    elif filledBoxes[0][2] == 2 and filledBoxes[1][1] == 0 and filledBoxes[2][0] == 2:
        return 5
    elif filledBoxes[0][2] == 0 and filledBoxes[1][1] == 2 and filledBoxes[2][0] == 2:
        return 3
    else:
        return -1

def trickMove():
    if filledBoxes[1][1] == 0:
        return 5
    else:
        return -1

def makeMove():
    if winningMove() != -1:
        return winningMove()
    elif blockMove() != -1:
        return blockMove()
    elif trickMove() != -1:
        return trickMove()
    else:
        loc = random.randint(1, 9)

        while validMove(loc) == False:
            loc = random.randint(1, 9)

        return loc

print("Player 1 will be x and player 2 will be o")

setupBoard()
displayBoard()

while quitting == False:
    if turn(player) == 0:
        quitting = True
    
    if quitting == False:
        displayBoard()
        if player == ' x ':
            player = ' o '
        else:
            player = ' x '

print("Thank you for playing!")
