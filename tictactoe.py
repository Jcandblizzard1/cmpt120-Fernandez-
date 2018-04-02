# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: John Fernandez
# Created: 2018-3-26
symbol = [ " ", "x", "o" ]
print("+-----+")

def printBoard(board):
# print the top border    
# for each row in the board... # print the row
    for row in range(3):
#print the next border
        for num in range(3):
            print('|',end="")
            if board[row][num] == 0:
                board[row][num] == ""
            print(board[row] [num], end="")
        print("|")
        print("+-----+")
    
def markBoard(board, row, col, player):
# check to see whether the desired square is blank # if so, set it to the player number
    if board[row][col] == " ":
        board[row][col] = symbol[player]
        return True 


    else:
        print("Try again")
        return False
    


def getPlayerMove():
        
    row = int(input("What row would you like to input in (1-3)? "))
    column = int(input("What column would you like to input in (1-3)? "))

        
    # prompt the user separately for the row and column numbers
    return int(row) -1 , int(column) -1 # then return that row and column instead of (0,0)

def hasBlanks(board):
# for each row in the board...
# for each square in the row...
# check whether the square is blank
# if so, return True
# if no square is blank, return False
    end = 0
    for row in range(3):
        for column in range(3):
            if board[row][column] == symbol[0]:
                return True
            if board[row][column] == symbol[1] or board[row][column] == symbol[2]:
                end = end + 1
                if end == 9:
                    print('')
                    return False 
def main():
    board = [
        [ " ", " ", " "],
        [ " ", " ", " "],
        [ " ", " ", " "]
        ]# TODO replace this with a three-by-three matrix of zeros
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        if markBoard(board,row,col,player):
            player = player % 2 + 1 # switch player for next turn
    printBoard(board)
main()

        
            




