import numpy as np

def check_current_board(xw_yw_G, xw_yw_Y, board):
    g_inside = []
    for i in range(len(xw_yw_G)):
        if   (xw_yw_G[i][0] >= 0.13 and xw_yw_G[i][0] < 0.21) and (xw_yw_G[i][1] >= 0.00 and xw_yw_G[i][1] < 0.08):
            insertLetter('X', 1, board)
            g_inside.append(i)
        elif (xw_yw_G[i][0] >= 0.13 and xw_yw_G[i][0] < 0.21) and (xw_yw_G[i][1] >= 0.08 and xw_yw_G[i][1] < 0.16):
            insertLetter('X', 2, board)
            g_inside.append(i)
        elif (xw_yw_G[i][0] >= 0.13 and xw_yw_G[i][0] < 0.21) and (xw_yw_G[i][1] >= 0.16 and xw_yw_G[i][1] < 0.24):
            insertLetter('X', 3, board)
            g_inside.append(i)
        elif (xw_yw_G[i][0] >= 0.21 and xw_yw_G[i][0] < 0.29) and (xw_yw_G[i][1] >= 0.00 and xw_yw_G[i][1] < 0.08):
            insertLetter('X', 4, board)
            g_inside.append(i)
        elif (xw_yw_G[i][0] >= 0.21 and xw_yw_G[i][0] < 0.29) and (xw_yw_G[i][1] >= 0.08 and xw_yw_G[i][1] < 0.16):
            insertLetter('X', 5, board)
            g_inside.append(i)
        elif (xw_yw_G[i][0] >= 0.21 and xw_yw_G[i][0] < 0.29) and (xw_yw_G[i][1] >= 0.16 and xw_yw_G[i][1] < 0.24):
            insertLetter('X', 6, board)
            g_inside.append(i)
        elif (xw_yw_G[i][0] >= 0.29 and xw_yw_G[i][0] < 0.37) and (xw_yw_G[i][1] >= 0.00 and xw_yw_G[i][1] < 0.08):
            insertLetter('X', 7, board)
            g_inside.append(i)
        elif (xw_yw_G[i][0] >= 0.29 and xw_yw_G[i][0] < 0.37) and (xw_yw_G[i][1] >= 0.08 and xw_yw_G[i][1] < 0.16):
            insertLetter('X', 8, board)
            g_inside.append(i)
        elif (xw_yw_G[i][0] >= 0.29 and xw_yw_G[i][0] < 0.37) and (xw_yw_G[i][1] >= 0.16 and xw_yw_G[i][1] < 0.24):
            insertLetter('X', 9, board)
            g_inside.append(i)
        else:
            continue 

    y_inside = []
    for i in range(len(xw_yw_Y)):
        if   (xw_yw_Y[i][0] >= 0.12 and xw_yw_Y[i][0] < 0.23) and (xw_yw_Y[i][1] >= 0.00 and xw_yw_Y[i][1] < 0.08):
            insertLetter('O', 1, board)
            y_inside.append(i)
        elif (xw_yw_Y[i][0] >= 0.12 and xw_yw_Y[i][0] < 0.23) and (xw_yw_Y[i][1] >= 0.08 and xw_yw_Y[i][1] < 0.16):
            insertLetter('O', 2, board)
            y_inside.append(i)
        elif (xw_yw_Y[i][0] >= 0.12 and xw_yw_Y[i][0] < 0.23) and (xw_yw_Y[i][1] >= 0.16 and xw_yw_Y[i][1] < 0.24):
            insertLetter('O', 3, board)
            y_inside.append(i)
        elif (xw_yw_Y[i][0] >= 0.22 and xw_yw_Y[i][0] < 0.32) and (xw_yw_Y[i][1] >= 0.00 and xw_yw_Y[i][1] < 0.08):
            insertLetter('O', 4, board)
            y_inside.append(i)
        elif (xw_yw_Y[i][0] >= 0.22 and xw_yw_Y[i][0] < 0.32) and (xw_yw_Y[i][1] >= 0.08 and xw_yw_Y[i][1] < 0.16):
            insertLetter('O', 5, board)
            y_inside.append(i)
        elif (xw_yw_Y[i][0] >= 0.22 and xw_yw_Y[i][0] < 0.32) and (xw_yw_Y[i][1] >= 0.16 and xw_yw_Y[i][1] < 0.24):
            insertLetter('O', 6, board)
            y_inside.append(i)
        elif (xw_yw_Y[i][0] >= 0.32 and xw_yw_Y[i][0] < 0.42) and (xw_yw_Y[i][1] >= 0.00 and xw_yw_Y[i][1] < 0.08):
            insertLetter('O', 7, board)
            y_inside.append(i)
        elif (xw_yw_Y[i][0] >= 0.32 and xw_yw_Y[i][0] < 0.42) and (xw_yw_Y[i][1] >= 0.08 and xw_yw_Y[i][1] < 0.16):
            insertLetter('O', 8, board)
            y_inside.append(i)
        elif (xw_yw_Y[i][0] >= 0.32 and xw_yw_Y[i][0] < 0.42) and (xw_yw_Y[i][1] >= 0.16 and xw_yw_Y[i][1] < 0.24):
            insertLetter('O', 9, board)
            y_inside.append(i)
        else:
            continue
        printBoard(board)

    return g_inside, y_inside

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def insertLetter(letter, pos, board):
    board[pos] = letter

def spaceIsFree(pos, board):
    return board[pos] == ' '
    
def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

def playerMove(board):
    global grid_3x3
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move, board):
                    run = False
                    #print(move)
                    return move
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')
            

def compMove(board):
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        
    return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True