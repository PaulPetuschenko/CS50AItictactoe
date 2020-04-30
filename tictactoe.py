"""
Tic Tac Toe Player
"""
import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    numOfMoves = 0

    for row in board:
        for el in row:
            if el == X or el == O:
                numOfMoves += 1
    
    if numOfMoves % 2 == 0:
        return X
    
    return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actionSet = set()

    actionSet = set()

    for row in range(3):
        for col in range(3):
            if board[row][col] is EMPTY:
                actionSet.add((row, col))

    return actionSet

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """ 
    state = copy.deepcopy(board)

    if player(board) is X:
        state[action[0]][action[1]] = X
    elif player(board) is O:
        state[action[0]][action[1]] = O

    return state

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    def findLines(br):
        out = []

        for num in range(3):
            col = []
            
            for row in br:
                col.append(row[num])
            
            out.append(col)

        for row in br:
            out.append(row)
            
        out.append([br[0][0], br[1][1], br[2][2]])
        out.append([br[0][2],br[1][1],br[2][0]])

        return out

    for el in findLines(board):
        if el[0] == el[1] and el[0] == el[2] and el[1] is X:
            return X
        elif el[0] == el[1] and el[0] == el[2] and el[1] is O:
            return O
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if winner(board) is X or winner(board) is O:
        return True
    
    for row in board:
        for cell in row:
            if cell is EMPTY:
                return False

    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if terminal(board):
        if winner(board) == X:
            return 1
        
        if winner(board) == O:
            return -1

        return 0

    raise ValueError

def playerToMove(boole):
    if boole:
        return X
    else:
        return O

def findMoveCoefficient(board, setOfMoves):
    coefficient = 0
    
    for move in setOfMoves:
        newMove = result(board, move)

        if terminal(newMove):
            coefficient += utility(newMove)

        coefficient += findMoveCoefficient(newMove, actions(newMove)) * 0.1
    
    return coefficient

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None             

    moves = {}

    for move in actions(board):
        newMove = result(board, move)
        
        moves.update( {move: findMoveCoefficient(newMove, actions(newMove))} )
    
    v = list(moves.values())
    k = list(moves.keys())

    if player(board) == X:
        return k[v.index(max(v))]

    else: 
        return k[v.index(min(v))]

        