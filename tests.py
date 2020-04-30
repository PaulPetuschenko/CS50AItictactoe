import random
import pytest

from tictactoe import *

testBoard = [[EMPTY, EMPTY, X],
            [EMPTY, X, O],
            [EMPTY, EMPTY, EMPTY]]

testMinimax01 = [[EMPTY, EMPTY, X],
            [EMPTY, X, O],
            [EMPTY, EMPTY, O]]

xWinBoard = [[EMPTY, EMPTY, X],
            [EMPTY, X, O],
            [X, EMPTY, EMPTY]]

oWinBoard = [[EMPTY, EMPTY, O],
            [EMPTY, X, O],
            [EMPTY, EMPTY, O]]

fullBoard = [[X, O, X],
            [X, X, O],
            [O, X, O]]

def test_player():
    assert player(testBoard) == O

def test_actions():
    assert actions(testBoard) == {(0, 0), (0, 1), (1, 0), (2, 0), (2, 1), (2, 2)}

def test_result():
    assert result(testBoard, (0, 0)) == [[O, EMPTY, X],[EMPTY, X, O],[EMPTY, EMPTY, EMPTY]]

def test_winner():
    assert winner(testBoard) == None
    assert winner(xWinBoard) == X
    assert winner(oWinBoard) == O

def test_terminal():
    assert terminal(testBoard) == False
    assert terminal(xWinBoard) == True
    assert terminal(fullBoard) == True

def test_utility():
    assert utility(xWinBoard) == 1
    assert utility(oWinBoard) == -1
    assert utility(fullBoard) == 0

def test_minima():
    assert minimax(testMinimax01) == (2, 0)