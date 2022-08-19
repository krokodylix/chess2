import time

from Piece import *
from Square import Square
import copy
class Game:
    def __init__(self):
        self.colors=['white','black']
        self.whitePieces=[]
        self.blackPieces=[]
        self.board=[]
        self.board=[Square(i) for i in range (0,64)]
        self.whiteKingsSquare=4
        self.blackKingsSquare=60
        self.historyOfMoves=[]
        self.choice=-1
        self.isGUI=False
        self.fr=-1
        self.to=-1
        for i in range (0,9):
            if i==0 or i==7:
                whiteRook=Rook('white',i)
                blackRook=Rook('black',63-i)
                self.board[i].piece=whiteRook
                self.board[63-i].piece=blackRook
                self.whitePieces.append(whiteRook)
                self.blackPieces.append(blackRook)
            elif i==1 or i==6:
                whiteKnight=Knight('white',i)
                blackKnight=Knight('black',63-i)
                self.board[i].piece=whiteKnight
                self.board[63-i].piece=blackKnight
                self.whitePieces.append(whiteKnight)
                self.blackPieces.append(blackKnight)
            elif i==2 or i==5:
                whiteBishop=Bishop('white',i)
                blackBishop=Bishop('black',63-i)
                self.board[i].piece=whiteBishop
                self.board[63-i].piece=blackBishop
                self.whitePieces.append(whiteBishop)
                self.blackPieces.append(blackBishop)
            elif i==3:
                whiteQueen=Queen('white',i)
                blackQueen=Queen('black',63-i-1)
                self.board[i].piece=whiteQueen
                self.board[63-i-1].piece=blackQueen
                self.whitePieces.append(whiteQueen)
                self.blackPieces.append(blackQueen)
            elif i==4:
                whiteKing=King('white',i)
                blackKing=King('black',63-i+1)
                self.board[i].piece=whiteKing
                self.board[63-i+1].piece=blackKing
                self.whitePieces.append(whiteKing)
                self.blackPieces.append(blackKing)
            elif i==8:
                for j in range (0,8):
                    whitePawn=Pawn('white',8+j)
                    blackPawn=Pawn('black',55-j)
                    self.board[8+j].piece=whitePawn
                    self.board[55-j].piece=blackPawn
                    self.whitePieces.append(whitePawn)
                    self.blackPieces.append(blackPawn)

        self.canWhiteShortCastle=True
        self.canWhiteLongCastle=True
        self.canBlackShortCastle=True
        self.canBlackLongCastle=True
        self.real=True

    def letSPlayGui(self):
        while True:
            if len(self.historyOfMoves)%2==0:
                moves=self.whereWhiteCanGo()
                while True:

                    if [self.fr,self.to] in moves:
                        self.move(self.fr,self.to)
                        self.fr=-1
                        self.to=-1
                        break
                    time.sleep(0.1)
            else:
                moves=self.whereBlackCanGo()
                while True:
                    if [self.fr,self.to] in moves:
                        self.move(self.fr,self.to)
                        self.fr=-1
                        self.to=-1
                        break
                    time.sleep(0.1)

    def letsPlay(self):
        while(True):
            print(self.colors[len(self.historyOfMoves)%2]+'\'s to move')
            print()
            self.printBoard()
            print()
            if self.colors[len(self.historyOfMoves)%2]=='white':
                moves=self.whereWhiteCanGo()

                if len(moves)==0 and self.isWhiteKingChecked():
                    print('mat czarne wygraly')
                    return None
                if len(moves)==0 and not self.isWhiteKingChecked():
                    print('pat, remis')
                    return None
                while True:
                    fr=int(input('from: '+'\n'+'>> '))
                    to=int(input('to: '+'\n'+'>> '))
                    if [fr,to] in moves:
                        self.move(fr,to)
                        break
            else:
                moves=self.whereBlackCanGo()
                if len(moves)==0 and self.isBlackKingChecked():
                    print('mat biale wygraly')
                    return None
                if len(moves)==0 and not self.isBlackKingChecked():
                    print('pat, remis')
                    return None
                while True:
                    fr=int(input('from: '+'\n'+'>> '))
                    to=int(input('to: '+'\n'+'>> '))
                    if [fr,to] in moves:
                        self.move(fr,to)
                        break


    def whereWhiteCanGo(self):
        t2r=[]
        for p in self.whitePieces:
            moves=self.whereCanIGo(p)
            for m in moves:
                if not self.isWhiteKingGoingToBeChecked(p.square,m):
                    t2r.append([p.square,m])
        return t2r
    def whereBlackCanGo(self):
        t2r=[]
        for p in self.blackPieces:
            moves=self.whereCanIGo(p)
            for m in moves:
                if not self.isBlackKingGoingToBeChecked(p.square,m):
                    t2r.append([p.square,m])
        return t2r
    def whereCanIGo(self,piece):
        t2r=[]
        if piece.pieceType=='R':
            # horizontally to the right
            temp = piece.square+1
            while (temp % 8 != 0):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    if self.board[temp].piece.color!=piece.color:
                        t2r.append(temp)
                    break
                temp += 1
            # horizontally to the left
            temp = piece.square-1
            while (temp % 8 != 7):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    if self.board[temp].piece.color!=piece.color:
                        t2r.append(temp)
                    break
                temp -= 1
            # vertically up
            temp = piece.square+8
            while (temp<64):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    if self.board[temp].piece.color!=piece.color:
                        t2r.append(temp)
                    break
                temp += 8
            # vertically down
            temp = piece.square-8
            while (temp>=0):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    if self.board[temp].piece.color!=piece.color:
                        t2r.append(temp)
                    break
                temp -= 8
            return t2r
        if piece.pieceType=='B':
            # +7 diagonal
            temp=piece.square+7
            while(temp%8!=7 and temp<63):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    if self.board[temp].piece.color!=piece.color:
                        t2r.append(temp)
                    break
                temp+=7
            # -7 diagonal
            temp=piece.square-7
            while(temp%8!=0 and temp>=0):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    if self.board[temp].piece.color!=piece.color:
                        t2r.append(temp)
                    break
                temp-=7
            # +9 diagonal
            temp=piece.square+9
            while(temp%8!=0 and temp<64):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    if self.board[temp].piece.color!=piece.color:
                        t2r.append(temp)
                    break
                temp+=9
            # -9 diagonal
            temp=piece.square-9
            while(temp%8!=7 and temp>=0):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    if self.board[temp].piece.color!=piece.color:
                        t2r.append(temp)
                    break
                temp-=9
            return t2r
        if piece.pieceType=='Q':
            # horizontally to the right
            temp = piece.square+1
            while (temp % 8 != 0):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    if self.board[temp].piece.color!=piece.color:
                        t2r.append(temp)
                    break
                temp += 1
            # horizontally to the left
            temp = piece.square-1
            while (temp % 8 != 7):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    if self.board[temp].piece.color!=piece.color:
                        t2r.append(temp)
                    break
                temp -= 1
            # vertically up
            temp = piece.square+8
            while (temp<64):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    if self.board[temp].piece.color!=piece.color:
                        t2r.append(temp)
                    break
                temp += 8
            # vertically down
            temp = piece.square-8
            while (temp>=0):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    if self.board[temp].piece.color!=piece.color:
                        t2r.append(temp)
                    break
                temp -= 8

            # +7 diagonal
            temp=piece.square+7
            while(temp%8!=7 and temp<63):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    if self.board[temp].piece.color!=piece.color:
                        t2r.append(temp)
                    break
                temp+=7
            # -7 diagonal
            temp=piece.square-7
            while(temp%8!=0 and temp>=0):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    if self.board[temp].piece.color!=piece.color:
                        t2r.append(temp)
                    break
                temp-=7
            # +9 diagonal
            temp=piece.square+9
            while(temp%8!=0 and temp<64):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    if self.board[temp].piece.color!=piece.color:
                        t2r.append(temp)
                    break
                temp+=9
            # -9 diagonal
            temp=piece.square-9
            while(temp%8!=7 and temp>=0):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    if self.board[temp].piece.color!=piece.color:
                        t2r.append(temp)
                    break
                temp-=9
            return t2r
        if piece.pieceType=='K' and piece.color=='white':
            posMoves=[1,7,8,9]
            for i in range (-1,2,2):
                for m in posMoves:
                    temp=(piece.square+i*m)
                    if(abs(temp%8-piece.square%8)<=1 and temp<=63 and temp>=0 and (self.board[temp].piece==None or self.board[temp].piece.color!=piece.color)):
                        t2r.append(temp)
            if(self.canWhiteShortCastle and not self.isWhiteKingChecked() and self.board[5].piece==None and self.board[6].piece==None):
                canI=True
                for p in self.blackPieces:
                    if 5 in self.whatSquaresDoIControll(p):
                        canI=False
                        break
                if canI:
                    t2r.append(6)
            if(self.canWhiteLongCastle and not self.isWhiteKingChecked() and self.board[3].piece==None and self.board[2].piece==None and self.board[1].piece==None):
                canI=True
                for p in self.blackPieces:
                    if 3 in self.whatSquaresDoIControll(p):
                        canI=False
                        break
                if canI:
                    t2r.append(2)

            return t2r
        if piece.pieceType=='K' and piece.color=='black':
            posMoves=[1,7,8,9]
            for i in range (-1,2,2):
                for m in posMoves:
                    temp=(piece.square+i*m)
                    if(abs(temp%8-piece.square%8)<=1 and temp<=63 and temp>=0 and (self.board[temp].piece==None or self.board[temp].piece.color!=piece.color)):
                        t2r.append(temp)
            if(self.canBlackShortCastle and not self.isBlackKingChecked() and self.board[61].piece==None and self.board[62].piece==None):
                canI=True
                for p in self.whitePieces:
                    if 61 in self.whatSquaresDoIControll(p):
                        canI=False
                        break
                if canI:
                    t2r.append(62)
            if(self.canBlackLongCastle and not self.isBlackKingChecked() and self.board[59].piece==None and self.board[58].piece==None and self.board[57].piece==None):
                canI=True
                for p in self.whitePieces:
                    if 59 in self.whatSquaresDoIControll(p):
                        canI=False
                        break
                if canI:
                    t2r.append(58)

            return t2r
        if piece.pieceType=='N':
            #+- 17, 10, 6, 15
            posMoves=[6,10,15,17]
            for i in range (-1,2,2):
                for m in posMoves:
                    temp=piece.square+i*m
                    res=abs(temp%8-piece.square%8)
                    if((res==2 or res==1) and temp<64 and temp>=0 and (self.board[temp].piece==None or self.board[temp].piece.color!=piece.color)):
                        t2r.append(temp)
            return t2r
        if piece.pieceType=='P' and piece.color=='white':
            if self.board[piece.square+8].piece==None:
                t2r.append(piece.square+8)
            if piece.square<=15 and self.board[piece.square+16].piece==None:
                t2r.append(piece.square+16)
            aSqr=self.whatSquaresDoIControll(piece)
            for s in aSqr:
                if self.board[s].piece!=None and self.board[s].piece.color=='black':
                    t2r.append(s)

                #en passant
                if piece.square<=39 and piece.square>=32 and (self.historyOfMoves[-1][1]+self.historyOfMoves[-1][0])/2==s and self.board[self.historyOfMoves[-1][1]].piece!=None and self.board[self.historyOfMoves[-1][1]].piece.pieceType=='P':
                    t2r.append(s)
            return t2r
        if piece.pieceType=='P' and piece.color=='black':

            if self.board[piece.square - 8].piece == None:
                t2r.append(piece.square - 8)
            if piece.square >= 48 and self.board[piece.square - 16].piece == None:
                t2r.append(piece.square - 16)
            aSqr = self.whatSquaresDoIControll(piece)
            for s in aSqr:
                if self.board[s].piece != None and self.board[s].piece.color == 'white':
                    t2r.append(s)

                # en passant
                if piece.square <= 31 and piece.square >= 24 and (self.historyOfMoves[-1][1] + self.historyOfMoves[-1][0]) / 2 == s and self.board[self.historyOfMoves[-1][1]].piece != None and self.board[self.historyOfMoves[-1][1]].piece.pieceType == 'P':
                    t2r.append(s)
            return t2r
    def whatSquaresDoIControll(self,piece):
        t2r=[]
        if piece.pieceType=='R':
            # horizontally to the right
            temp = piece.square+1
            while (temp % 8 != 0):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    t2r.append(temp)
                    break
                temp += 1
            # horizontally to the left
            temp = piece.square-1
            while (temp % 8 != 7):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    t2r.append(temp)
                    break
                temp -= 1
            # vertically up
            temp = piece.square+8
            while (temp<64):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    t2r.append(temp)
                    break
                temp += 8
            # vertically down
            temp = piece.square-8
            while (temp>=0):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    t2r.append(temp)
                    break
                temp -= 8
            return t2r
        if piece.pieceType=='B':
            # +7 diagonal
            temp=piece.square+7
            while(temp%8!=7 and temp<63):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    t2r.append(temp)
                    break
                temp+=7
            # -7 diagonal
            temp=piece.square-7
            while(temp%8!=0 and temp>=0):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    t2r.append(temp)
                    break
                temp-=7
            # +9 diagonal
            temp=piece.square+9
            while(temp%8!=0 and temp<64):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    t2r.append(temp)
                    break
                temp+=9
            # -9 diagonal
            temp=piece.square-9
            while(temp%8!=7 and temp>=0):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    t2r.append(temp)
                    break
                temp-=9
            return t2r
        if piece.pieceType=='Q':

            # horizontally to the right
            temp = piece.square+1
            while (temp % 8 != 0):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    t2r.append(temp)
                    break
                temp += 1
            # horizontally to the left
            temp = piece.square-1
            while (temp % 8 != 7):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    t2r.append(temp)
                    break
                temp -= 1
            # vertically up
            temp = piece.square+8
            while (temp<64):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    t2r.append(temp)
                    break
                temp += 8
            # vertically down
            temp = piece.square-8
            while (temp>=0):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    t2r.append(temp)
                    break
                temp -= 8

            # +7 diagonal
            temp=piece.square+7
            while(temp%8!=7 and temp<63):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    t2r.append(temp)
                    break
                temp+=7
            # -7 diagonal
            temp=piece.square-7
            while(temp%8!=0 and temp>=0):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    t2r.append(temp)
                    break
                temp-=7
            # +9 diagonal
            temp=piece.square+9
            while(temp%8!=0 and temp<64):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    t2r.append(temp)
                    break
                temp+=9
            # -9 diagonal
            temp=piece.square-9
            while(temp%8!=7 and temp>=0):
                if self.board[temp].piece==None:
                    t2r.append(temp)
                else:
                    t2r.append(temp)
                    break
                temp-=9
            return t2r
        if piece.pieceType=='K':
            posMoves=[1,7,8,9]
            for i in range (-1,2,2):
                for m in posMoves:
                    temp=(piece.square+i*m)
                    if(abs(temp%8-piece.square%8)<=1 and temp<=63 and temp>=0):
                        t2r.append(temp)
            return t2r
        if piece.pieceType=='N':
            #+- 17, 10, 6, 15
            posMoves=[6,10,15,17]
            for i in range (-1,2,2):
                for m in posMoves:
                    temp=piece.square+i*m
                    res=abs(temp%8-piece.square%8)
                    if((res==2 or res==1) and temp<64 and temp>=0):
                        t2r.append(temp)
            return t2r
        if piece.pieceType=='P' and piece.color=='white':
            if(abs(piece.square%8-(piece.square+7)%8)==1):
                t2r.append(piece.square+7)
            if(abs(piece.square%8-(piece.square+9)%8)==1):
                t2r.append(piece.square+9)
            return t2r
        if piece.pieceType=='P' and piece.color=='black':
            if(abs(piece.square%8-(piece.square-7)%8)==1):
                t2r.append(piece.square-7)
            if(abs(piece.square%8-(piece.square-9)%8)==1):
                t2r.append(piece.square-9)
            return t2r
    def printBoard(self):
        for i in range (0,8):
            print(str(8-i)+' ',end='')
            for j in range (0,8):
                print(str(self.board[56-8*i+j])+' ',end='')
            print('   ',end='')

            for j in range (0,8):
                if 56-8*i+j>=10:
                    print(str(56-8*i+j)+' ',end='')
                else:
                    print(' '+str(56 - 8 * i + j) + ' ', end='')
            print()
        print(' ',end='')
        for i in range(0,8):
            print('  '+str(chr(97+i)).upper(),end='')

    def move(self,fr,to):
        if self.board[fr].piece.pieceType=='K' and self.board[fr].piece.color=='white' and abs(fr-to)==2:
            if to>fr:
                self.whiteKingsSquare=6
                self.canWhiteLongCastle=False
                self.canWhiteShortCastle=False
                self.board[4].piece.square=6
                self.board[6].piece=self.board[4].piece
                self.board[4].piece=None
                self.board[7].piece.square=5
                self.board[5].piece=self.board[7].piece
                self.board[7].piece=None
            if to<fr:
                self.whiteKingsSquare=2
                self.canWhiteLongCastle=False
                self.canWhiteShortCastle=False
                self.board[4].piece.square=2
                self.board[2].piece=self.board[4].piece
                self.board[4].piece=None
                self.board[0].piece.square=3
                self.board[3].piece=self.board[0].piece
                self.board[0].piece=None
            self.historyOfMoves.append([fr,to])
            return None
        if self.board[fr].piece.pieceType=='K' and self.board[fr].piece.color=='white':
            self.canWhiteShortCastle=False
            self.canWhiteLongCastle=False
            self.whiteKingsSquare=to
        if self.board[fr].piece.pieceType=='R' and fr==7 and self.board[fr].piece.color=='white' and self.canWhiteShortCastle:
            self.canWhiteShortCastle=False
        if self.board[fr].piece.pieceType=='R' and fr==0 and self.board[fr].piece.color=='white' and self.canWhiteLongCastle:
            self.canWhiteLongCastle=False
        if self.board[fr].piece.pieceType=='P' and abs(fr%8-to%8)==1 and self.board[to].piece==None:
            self.board[to].piece=self.board[fr].piece
            self.board[to].piece.square=to
            self.board[fr].piece=None
            if self.board[to].piece.color=='white':
                self.blackPieces.remove(self.board[self.historyOfMoves[-1][1]].piece)
                self.board[self.historyOfMoves[-1][1]].piece=None
            else:
                self.whitePieces.remove(self.board[self.historyOfMoves[-1][1]].piece)
                self.board[self.historyOfMoves[-1][1]].piece=None
            self.historyOfMoves.append([fr,to])
            return None
        if self.board[fr].piece.pieceType=='K' and self.board[fr].piece.color=='black' and abs(fr-to)==2:
            if to>fr:
                self.blackKingsSquare=62
                self.canBlackLongCastle=False
                self.canBlackShortCastle=False
                self.board[60].piece.square=62
                self.board[62].piece=self.board[60].piece
                self.board[60].piece=None
                self.board[63].piece.square=61
                self.board[61].piece=self.board[63].piece
                self.board[63].piece=None
            if to<fr:
                self.blackKingsSquare=58
                self.canBlackLongCastle=False
                self.canBlackShortCastle=False
                self.board[60].piece.square=58
                self.board[58].piece=self.board[60].piece
                self.board[60].piece=None
                self.board[56].piece.square=59
                self.board[59].piece=self.board[56].piece
                self.board[56].piece=None
            self.historyOfMoves.append([fr,to])
            return None
        if self.board[fr].piece.pieceType=='K' and self.board[fr].piece.color=='black':
            self.canBlackShortCastle=False
            self.canBlackLongCastle=False
            self.blackKingsSquare=to
        if self.board[fr].piece.pieceType=='R' and fr==63 and self.board[fr].piece.color=='black' and self.canBlackShortCastle:
            self.canBlackShortCastle=False
        if self.board[fr].piece.pieceType=='R' and fr==56 and self.board[fr].piece.color=='black' and self.canBlackLongCastle:
            self.canBlackLongCastle=False
        if self.board[to].piece!=None:
            if self.board[to].piece.color=='white':
                self.whitePieces.remove(self.board[to].piece)
            else:
                self.blackPieces.remove(self.board[to].piece)
        self.board[to].piece=self.board[fr].piece
        self.board[fr].piece=None
        self.board[to].piece.square=to
        self.historyOfMoves.append([fr,to])
        if self.board[to].piece.pieceType=='P' and  self.board[to].piece.color=='white' and fr>=48 and self.real:
            transformations=['Q','R','N','B']
            print('choose transformation: ')
            print('1. Queen')
            print('2. Rook')
            print('3. Knight')
            print('4. Bishop')
            if not self.isGUI:
                inp=int(input('>> '))
                while not (inp>=1 and inp<=4):
                    inp = int(input('>> '))
            else:
                inp=self.choice
            self.board[to].piece.pieceType=transformations[inp-1]
        if self.board[to].piece.pieceType=='P' and  self.board[to].piece.color=='black' and fr<=15 and self.real:
            transformations=['Q','R','N','B']
            print('choose transformation: ')
            print('1. Queen')
            print('2. Rook')
            print('3. Knight')
            print('4. Bishop')
            if not self.isGUI:
                inp=int(input('>> '))
                while not (inp>=1 and inp<=4):
                    inp = int(input('>> '))
            else:
                inp = self.choice
            self.board[to].piece.pieceType=transformations[inp-1]
    def isWhiteKingChecked(self):
        for p in self.blackPieces:
            if self.whiteKingsSquare in self.whatSquaresDoIControll(p):

                return True
        return False

    def isBlackKingChecked(self):
        for p in self.whitePieces:
            if self.blackKingsSquare in self.whatSquaresDoIControll(p):
                return True
        return False


    def isWhiteKingGoingToBeChecked(self,fr,to):
        tempGame=copy.deepcopy(self)
        tempGame.real=False
        tempGame.move(fr,to)
        return tempGame.isWhiteKingChecked()

    def isBlackKingGoingToBeChecked(self,fr,to):
        tempGame=copy.deepcopy(self)
        tempGame.real=False
        tempGame.move(fr,to)

        return tempGame.isBlackKingChecked()