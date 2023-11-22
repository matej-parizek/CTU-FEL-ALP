import sys
import random
import copy
import base

from draw import Drawer


class Player(base.BasePlayer):
    def __init__(self, name, board, marks, stones, player):
        """ constructor of Player. Place you variables here with prefix 'self' -> e.g. 'self.myVariable' """
        self.stones=stones
        self.board=board
        base.BasePlayer.__init__(self, name, board, marks, stones, player)  #do not change this line!!
        self.algorithm = "my great method"  #name of your method. Will be used in tournament mode
    def otoceni(self,n):
        self.sloupce=[]
        self.radky=[]
        for i in range(len(self.kamen)):
            if n>0:
                self.kamen[i][0],self.kamen[i][1]=self.kamen[i][1],-self.kamen[i][0]
            self.radky.append( self.kamen[i][0])
            self.sloupce.append(self.kamen[i][1])
        MinSloupec=min(self.sloupce)
        MinRadek=min(self.radky)
        Sloupec=max(self.sloupce)
        Radek=max(self.radky)
        osax = -1*MinSloupec
        osay = -1*MinRadek
        self.sirka = osax + Sloupec + 1
        self.vyska = osay + Radek + 1
        for k in range(len(self.kamen)):
            self.kamen[k][1]= self.kamen[k][1] +osax
            self.kamen[k][0]= self.kamen[k][0]+osay
        return self.kamen
    def mimox(self,posun):
        return posun+ self.sirka > len(self.board)
    def mimoy(self,posun):
        return posun+ self.vyska> len(self.board)

    def kontrolabarvy(self,y,x):
        if x > 0 :
            if self.board[y][x - 1] == self.barva:
                return False
        if y > 0:
            if self.board[y - 1][x] ==self.barva:
                return False
        if x < len(self.board) - 1:
            if self.board[y][x + 1] ==self.barva:
                return False
        if y < len(self.board) - 1:
            if self.board[y + 1][x] ==self.barva:
                return False
        return True
    def pravidlo(self,kamen,PosunR,PosunS):
        tabulka=[]
        for i in range(len(self.board)):
            radek=[]
            for k in range(len(self.board[i])):
                radek.append(self.board[i][k])
            tabulka.append(radek)
        for s in kamen:
            tabulka[s[0]+PosunR][s[1]+PosunS]=self.barva
        for r in range(len(self.board)-1):
            for s in range(len(self.board)-1):
                if tabulka[r][s]!=0 and tabulka[r][s+1]!=0 and tabulka[r+1][s]!=0 and tabulka[r+1][s+1] !=0:
                    return True
        else:
            return False
    def napojeni(self,y,x):
        if self.isEmpty():
            return True
        if x >0 :
            if self.board[y][x-1] !=0:
                return True
        if y >0:
            if self.board[y-1][x ] != 0:
                return True
        if x<len(self.board)-1:
            if self.board[y][x+1] !=0:
                return True
        if y<len(self.board)-1:
            if self.board[y+1][x] != 0:
                return True
        return False

    def dosazeni(self,kamen):
        final=[]
        for PosunR in range(len(self.board)):
            if self.mimoy(PosunR):
                break
            for PosunS in range(len(self.board)):
                if self.mimox(PosunS):
                    break
                if self.pravidlo(kamen,PosunR,PosunS):
                    continue
                volno = True
                stav=[]
                for sourad in kamen:
                    if self.board[sourad[0] + PosunR][sourad[1] + PosunS] != 0:
                        volno = False
                        break
                    if self.kontrolabarvy(sourad[0] + PosunR,sourad[1] + PosunS )==False:
                        volno=False
                        break
                    if self.napojeni(sourad[0] + PosunR, sourad[1] + PosunS)==True:
                        stav.append("True")
                    else:
                        stav.append("False")
                if stav.count("True")==0:
                    continue
                if volno == False:
                    continue
                for sourad in kamen:
                    final.append([sourad[0] + PosunR, sourad[1] + PosunS])
                return final
    def move(self):
        """ return [ stoneIdx, [ stonePosition] ]
            stoneIdx .. integer .. index of stone to self.freeStones
            [stonePosition] = [ [row1,col1] ... [rown, coln] ] .. position into board where stone is placed

            if no stone can be placed:
            return []
        """
        for i in range(0,len(self.freeStones),1):
            if self.freeStones[i] == False:
                continue
            for j in range(4):
                self.kamen = self.stones[i][1]
                self.barva = self.stones[i][0]
                kamen=self.otoceni(i)
                if self.dosazeni(kamen)!=None:
                    return [i,self.dosazeni(kamen)]
        return []


if __name__ == "__main__":

    #load stones from file
    stones = base.loadStones("stones.txt")
    #print("stones are", stones)

    #prepare board and marks
    board, marks = base.makeBoard10();

    #create both players    
    p1 = Player("pepa", board, marks, stones, 1)
    p2 = Player("franta", board, marks, stones, -1)

    #not necessary, only if you want to draw board to png files
    d = Drawer()
    d.draw(p1.board, p1.marks, "init.png");

    moveidx = 0
    while True:
        p1play = True
        p2play = True

        m = p1.move()  #first player, we assume that a corrent output is returned

        #the following if/else is simplified. On Brute, we will check if return value
        #from move() is valid ...
        if len(m) == 0:
            p1play = False
        else:
            stoneIdx, stone = m
            stoneColor = stones[stoneIdx][0]
            base.writeBoard(p1.board, stone, stoneColor) #write stone to player1's board
            base.writeBoard(p2.board, stone, stoneColor) #write stone to player2's board
            p1.freeStones[ stoneIdx ] = False #tell player1 which stone is used
            p2.freeStones[ stoneIdx ] = False #tell player2 which stone is used
        d.draw(p2.board, p2.marks, "move-{:02d}a.png".format(moveidx)) #draw to png

        #now we call player2 and update boards/freeStones of both players
        m = p2.move()  
        if len(m) == 0:
            p2play = False
        else:
            stoneIdx, stone = m
            stoneColor = stones[stoneIdx][0]
            base.writeBoard(p1.board, stone, stoneColor)
            base.writeBoard(p2.board, stone, stoneColor)
            p1.freeStones[ stoneIdx ] = False
            p2.freeStones[ stoneIdx ] = False
        d.draw(p1.board, p1.marks, "move-{:02d}b.png".format(moveidx))
        #if both players return [] from move, the game ends
        if p1play == False and p2play == False:
            print("end of game")
            break
    
        moveidx+=1
        print(" -- end of move ", moveidx, " score is ", p1.score(p1.player), p1.score(-p1.player) )




