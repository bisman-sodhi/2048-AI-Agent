import random
from typing import List
import numpy as np
from copy import deepcopy

#USING newTileOption DONT DELETE
newTileOption = [2,4]  

'''
                        HELPER FUNCTION SECTION
'''
#put 2 2s are random places in the matrix
def startGame(board):
    countTwice = 0
    while(countTwice < 2):
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        board[row][col] = 2
        board[row][col] = 2
        countTwice += 1
    return board

#adds 2 with prob 0.9 or 4 with prob 0.10 to random empty cell
def add_new_tile(board):
    row = random.randint(0, 3)
    col = random.randint(0, 3)
    while(board[row][col] != 0):
        row = random.randint(0, 3)
        col = random.randint(0, 3)
    
    newTile = np.random.choice(newTileOption, p=[0.90, 0.10])
    board[row][col] = newTile
    return board

#returns a list of empty cells coordinates like [(x1,y1), (x2,y2), ...]
def emptyCells(board):
    emptyList = []
    for i in range(4):
        for j in range(4):
            if(board[i][j] == 0):
                emptyPos = [i,j]
                emptyList.append(emptyPos)
    return emptyList

#adds number at coordinate i,j
def addNewEntry(grid, i, j , number):
    grid[i][j] = number
    return grid


#prints the board
def printBoard(board):
    for i in range(4):
        print(board[i])
    

#makes a deepcopy of the board
def duplicate(board):
    return deepcopy(board)        


'''
                        HEPLER FUNCTION SECTION END
'''


'''

                        BOARD MANIPULATION SECTION

'''
#pushes all non zero numbers to one side
def pushNonZero(board):
    changed = False
    newM = [[0] * 4 for _ in range(4)]
    for i in range(4):
        fill_position = 0
        for j in range(4):
            if board[i][j] != 0:
                newM[i][fill_position] = board[i][j]
                if (j != fill_position):
                    changed = True 
                fill_position += 1
    return newM, changed

# adds adjacent tiles that have the same number and update score
def adjacentTitles(board):
    changed = False
    for i in range(4):
        for j in range(3):
            if board[i][j] != 0 and board[i][j] == board[i][j + 1]:
                board[i][j] *= 2
                board[i][j + 1] = 0
                changed = True
    return board, changed

#reverse a row
def reverseMatrix(board):
    newM = []
    for i in range(4):
        newM.append([])
        for j in range(4):
            newM[i].append(board[i][3 - j])
    return newM

#transpose
def transposeMatrix(board):
    newM = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            newM[i][j] = board[j][i]
    return newM

#move left
def left(board):
    newMatrix, changed = pushNonZero(board)
    newMatrix, changed = adjacentTitles(newMatrix)
    newMatrix, changed = pushNonZero(newMatrix)
    return newMatrix

#move right  
def right(board):
    newMatrix = reverseMatrix(board)
    newMatrix, changed = pushNonZero(newMatrix)
    newMatrix, changed = adjacentTitles(newMatrix)
    newMatrix, changed = pushNonZero(newMatrix)
    newMatrix = reverseMatrix(newMatrix)
    return newMatrix

#move up
def up(board):
    newMatrix = transposeMatrix(board)
    newMatrix, changed = pushNonZero(newMatrix)
    newMatrix, changed = adjacentTitles(newMatrix)
    newMatrix, changed = pushNonZero(newMatrix)
    newMatrix = transposeMatrix(newMatrix)
    return newMatrix

#move down
def down(board):
    newMatrix = transposeMatrix(board)
    newMatrix = reverseMatrix(newMatrix)
    newMatrix, changed = pushNonZero(newMatrix)
    newMatrix, changed = adjacentTitles(newMatrix)
    newMatrix, changed = pushNonZero(newMatrix)
    newMatrix = reverseMatrix(newMatrix)
    newMatrix = transposeMatrix(newMatrix)
    return newMatrix

#can move up
def canMoveUp(board):
    newMatrix = transposeMatrix(board)
    newMatrix, changed1 = pushNonZero(newMatrix)
    newMatrix, changed2 = adjacentTitles(newMatrix)
    if (changed1 == True) or (changed2 == True): 
        return True
    return False

#can move down
def canMoveDown(board):
    newMatrix = transposeMatrix(board)
    newMatrix = reverseMatrix(newMatrix)
    newMatrix, changed1 = pushNonZero(newMatrix)
    newMatrix, changed2 = adjacentTitles(newMatrix)
    if (changed1 == True) or (changed2 == True): 
        return True
    return False

#can move left
def canMoveLeft(board):
    newMatrix, changed1 = pushNonZero(board)
    newMatrix, changed2 = adjacentTitles(newMatrix)
    if (changed1 == True) or (changed2 == True): 
        return True
    return False

#can move right
def canMoveRight(board):
    newMatrix = reverseMatrix(board)
    newMatrix, changed1 = pushNonZero(newMatrix)
    newMatrix, changed2 = adjacentTitles(newMatrix)
    if (changed1 == True) or (changed2 == True): 
        return True
    return False     

#returns grid for direction
def canMoveAll(grid, direction):
    gridUp = duplicate(grid)
    gridDown = duplicate(grid)
    gridLeft = duplicate(grid)
    gridRight = duplicate(grid)
    afterMoveGrid = duplicate(grid)
    if direction == 0:
        afterMoveGrid = up(gridUp)
    elif direction == 1: 
        afterMoveGrid = down(gridDown)
    elif direction == 2: 
        afterMoveGrid = left(gridLeft)          
    elif direction == 3: 
        afterMoveGrid = right(gridRight)
    return afterMoveGrid

#return grid and bool for direction 
def canMove(grid, direction):
    gridUp = duplicate(grid)
    gridDown = duplicate(grid)
    gridLeft = duplicate(grid)
    gridRight = duplicate(grid)
    afterMoveGrid = duplicate(grid)
    afterMove = False
    
    if direction == 0:
        afterMove = canMoveUp(grid)
        if(afterMove == True):
            afterMoveGrid = up(gridUp)
    elif direction == 1: 
        afterMove = canMoveDown(grid)
        if(afterMove == True):
            afterMoveGrid = down(gridDown)
    elif direction == 2: 
        afterMove = canMoveLeft(grid)
        if(afterMove == True):
            afterMoveGrid = left(gridLeft)          
    elif direction == 3: 
        afterMove = canMoveRight(grid)
        if(afterMove == True):
            afterMoveGrid = right(gridRight)
    return afterMoveGrid, afterMove


'''

                        BOARD MANIPULATION SECTION ENDS

'''



'''

                        EXPECTIMAX HELPER FUNCTION 

'''

def mightWorkEval(board):
    a = 0
    w = [ [0.135759, 0.121925 , 0.102812, 0.099937], 
        [0.0997992, 0.0888405, 0.076711, 0.0724143 ], 
        [0.060654, 0.0562579, 0.037116 , 0.0161889] , 
        [0.0125498, 0.00992495, 0.00575871, 0.00335193] ]
    for x in range(0, 4):
        for y in range(0, 4):
            if board[x][y] != None:
                val = board[x][y]
                a += val * w[x][y]
    return a

def getChildren(grid):
    allMoves = [0,1,2,3]
    children = []
    moving = []
    for i in allMoves:
        movedGrid, moved = canMove(grid, i)
        if moved == True:
            children.append(movedGrid)
            moving.append(i)
    return children, moving

def getAllChildren(grid):
    children = []
    upAns = up(grid)
    children.append(upAns)
    downAns = down(grid)
    children.append(downAns)
    leftAns = left(grid)
    children.append(leftAns)
    rightAns = right(grid)
    children.append(rightAns)
    return children

def noMoreMoves(board):
    keyLen = []
    for i in range(4):
        mG, mD = canMove(board, i)
        if mD == False:
            keyLen.append(mD)
    if len(keyLen) == 4:
        return True
    else:
        return False

def got2048(board):
    for row in range(4):
        for col in range(4):
            curNum = board[row][col]
            if curNum == 2048:
                return True
    return False

def expminmax(grid, maxDepth, maxPlayer):
    bestDirection = None
    numOfEmptyCells = len(emptyCells(grid))
    if maxDepth == 0:
        return mightWorkEval(grid), bestDirection
    if maxPlayer == True:
        maxNum = float('-inf')
        children, moving = getChildren(grid)
        for move in moving:
            firstnewGrid = duplicate(grid)
            child = canMoveAll(firstnewGrid, move)
            maxAns, dir = expminmax(child, maxDepth - 1, False)
            if maxAns > maxNum:
                maxNum = maxAns
                bestDirection = move
        return maxNum , bestDirection
    else:
        expectedValues = 0
        emptyList = emptyCells(grid)
        for em in emptyList:
            newGrid = duplicate(grid)
            newGrid = addNewEntry(newGrid, em[0], em[1], 2)
            newScore, d = expminmax(newGrid, maxDepth - 1, True)
            if newScore == float('-inf'):
                expectedValues += 0
            else:
                expectedValues += (0.9 * newScore)
                bestDirection = d
            newGrid = duplicate(grid)
            newGrid = addNewEntry(newGrid, em[0], em[1], 4)
            newScore, d = expminmax(newGrid, maxDepth - 1, True)
            if newScore == float('-inf'):
                expectedValues += 0
            else:
                expectedValues += (0.1 * newScore)
                bestDirection = d
        expectedValues /= numOfEmptyCells
        return expectedValues, bestDirection


def localNextMove(Grid: List[List[int]], Step: int):
    gameis = Grid
    print("in local initial board")
    while(Step != 2000):
        ans = expminmax(gameis, 3, True)
        if ans[1] == None:
            return "quit"
        gameis, booll = canMove(gameis, ans[1])
        gameis = add_new_tile(gameis)
        printBoard(gameis)
        print("moved above board here " , ans[1])
        Step += 1
        print(Step)
    return ans[1]

def NextMove(Grid: List[List[int]], Step: int):
    ans = expminmax(Grid, 3, True)
    if ans[1] == None:
        return "quit"
    return ans[1]


myBoard = [[0,0,2,0], [0,0,0,0], [0,0,0,0], [2,0,0,0]]
newans = localNextMove(myBoard, 3)


