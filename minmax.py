#%%
from random import choice
from math import inf as infinity
import time
from os import system
class board:
    HUMAN = -1
    COMP = +1
    def printBoard(self,cMark,hMark):
        for l in self.state:
            for v in l:
                if (v == -1):
                    print(hMark, end=' | ')
                elif (v == +1):
                    print(cMark, end = ' | ')
                else:
                    print('_',end = ' | ')
            print('\n')
    def clean (self):
        system('cls')
        print("\n-------------")
    def evaluate(self):
        if self.wins(self.COMP):
            score = +1
        elif self.wins(self.HUMAN):
            score = -1
        else:
            score = 0
        return score

    def validMove(self, x, y):
        if [x,y] in self.emptyCells():
            return True
        else:
            return False
            
    def __init__(self):
        self.state = [[0,0,0],[0,0,0],[0,0,0]]

    def markCell(self, x, y, player):
        if self.validMove( x, y):
            self.state[x][y]=player
            return True
        else:
            return False
    def gameOver(self):
        return self.wins(self.HUMAN) or self.wins(self.COMP)

    def wins(self, player):
        endGames = [
            [self.state[0][0], self.state[0][1], self.state[0][2]],
            [self.state[1][0], self.state[1][1], self.state[1][2]],
            [self.state[2][0], self.state[2][1], self.state[2][2]],
            [self.state[0][0], self.state[1][0], self.state[2][0]],
            [self.state[0][1], self.state[1][1], self.state[2][1]],
            [self.state[0][2], self.state[1][2], self.state[2][2]],
            [self.state[0][0], self.state[1][1], self.state[2][2]],
            [self.state[2][0], self.state[1][1], self.state[0][2]]
        ]
        if [player,player,player] in endGames:
            return True
        else:
            return False

   
    def emptyCells(self):
        cells = []
        for x, rows in enumerate(self.state):
            for y, cell in enumerate(rows):
                if (cell ==0):
                    cells.append([x,y])
        return cells
    def minmax(self, depth, player):
        if player == self.COMP:
            best =[-1,-1,-infinity]
        else:
            best = [1,1,+infinity]
        if depth == 0 or self.gameOver():
            score = self.evaluate()
            return [-1,-1,score]
        for cell in self.emptyCells():
            x, y = cell[0], cell[1]
            self.state[x][y] = player
            score = self.minmax(depth-1, -player)
            self.state[x][y] = 0
            score[0],score[1] = x,y
                
            if player == self.COMP:
                if score[2] > best[2]:
                    best = score
            else: 
                if score[2] < best [2]:
                    best = score
        return best
    def aiChoice(self, cMark,hMark):
        depth = len(self.emptyCells())
        if depth == 0 or self.gameOver():
            return
        if depth == 9:
            x = choice([0,1,2])
            y = choice([0,1,2])
        else: 
            move = self.minmax(depth, self.COMP)
            x, y = move[0], move[1]
        self.markCell(x,y,self.COMP)
        time.sleep(1) 
    def hChoice(self,cMark,hMark):
        move = -1
        moves = {
            7:[0,0], 8:[0,1], 9:[0,2],
            4:[1,0], 5:[1,1], 6:[1,2],
            1:[2,0], 2:[2,1], 3:[2,2]
        }
        while move < 1 or move > 9:
            try:
                move = int(input("use the numpad to choose a cell"))
                coord = moves[move]
                can_move = self.markCell(coord[0],coord[1], self.HUMAN)

                if not can_move:
                    print('bad move')
            except(EOFError, KeyboardInterrupt):
                print('bye')
                exit()
            except(ValueError,KeyError):
                print('bad choice')

    
#%%
def game():
    b =board()
    b.printBoard(0,0)
    hMark = ' '
    cMark = ' '
    first = ' '
    while hMark !='X' and hMark !='O':
        try:
            hMark = input("X or O?").upper()
        except(EOFError, KeyboardInterrupt):
            print('bye')
            exit()
        except(ValueError,KeyError):
            print('bad choice')
    if hMark == 'X':
        cMark = 'O'
    else:
        cMark = 'X'
    while first !='Y' and first !='N':
        try:
            first = input("want to start? y/n").upper()
        except(EOFError, KeyboardInterrupt):
            print('bye')
            exit()
        except(ValueError,KeyError):
            print('bad choice')
    b.printBoard(cMark,hMark)
    while len(b.emptyCells())> 0 and not b.gameOver():
        if first =='N':
            b.clean()
            b.aiChoice(cMark,hMark)
            b.printBoard(cMark,hMark)
            first = ''
        b.hChoice(cMark,hMark)
        b.printBoard(cMark,hMark)
        b.clean()
        b.aiChoice(cMark,hMark)
        b.printBoard(cMark,hMark)
    if b.wins(b.HUMAN):
        b.clean()
        b.printBoard(cMark,hMark)
        print('YOU WIN')

    elif b.wins(b.COMP):
        b.clean()
        b.printBoard(cMark,hMark)
        print('YOU LOSE')
    else:
        b.clean()
        b.printBoard(cMark,hMark)
        print('DRAW')
    exit()
game()


#%%