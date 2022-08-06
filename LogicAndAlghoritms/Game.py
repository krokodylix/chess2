from Piece import *
from Square import Square
import copy
class Game:
    def __init__(self):
        self.whitePieces=[]
        self.blackPieces=[]
        self.board=[]
        self.board=[Square(i) for i in range (0,64)]
        self.whiteKingsSquare=4
        self.blackKingsSquare=60
        self.historyOfMoves=[]
        '''
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
        '''
        self.canWhiteShortCastle=True
        self.canWhiteLongCastle=True
        self.canBlackShortCastle=True
        self.canBlackLongCastle=True

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
            while (temp>0):
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
            while(temp%8!=0 and temp>0):
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
            while (temp>0):
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
            while(temp%8!=0 and temp>0):
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
                    if(abs(temp%8-piece.square%8)<=1 and temp<=64 and temp>=0 and (self.board[temp].piece==None or self.board[temp].piece.color!=piece.color)):
                        t2r.append(temp)
            if(self.canWhiteShortCastle and self.board[5].piece==None):
                canI=True
                for p in self.blackPieces:
                    if 5 in self.whatSquaresDoIControll(p):
                        canI=False
                        break
                if canI:
                    t2r.append(6)
            if(self.canWhiteLongCastle and self.board[3].piece==None):
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
                    if(abs(temp%8-piece.square%8)<=1 and temp<=64 and temp>=0 and (self.board[temp].piece==None or self.board[temp].piece.color!=piece.color)):
                        t2r.append(temp)
            if(self.canBlackShortCastle and self.board[61].piece==None):
                canI=True
                for p in self.whitePieces:
                    if 61 in self.whatSquaresDoIControll(p):
                        canI=False
                        break
                if canI:
                    t2r.append(62)
            if(self.canBlackLongCastle and self.board[59].piece==None):
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
            while (temp>0):
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
            while(temp%8!=0 and temp>0):
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
            while (temp>0):
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
            while(temp%8!=0 and temp>0):
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
                    if(abs(temp%8-piece.square%8)<=1 and temp<=64 and temp>=0):
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

    def printBoard(self):
        for i in range (0,8):
            for j in range (0,8):
                print(str(self.board[56-8*i+j])+' ',end='')
            print()

    def printNumeration(self):
        for i in range (0,8):
            for j in range (0,8):
                if 56-8*i+j>=10:
                    print(str(56-8*i+j)+' ',end='')
                else:
                    print(' '+str(56 - 8 * i + j) + ' ', end='')
            print()

    def move(self,fr,to):
        if self.board[to].piece!=None:
            if self.board[to].piece.color=='white':
                self.whitePieces.remove(self.board[to].piece)
            else:
                self.blackPieces.remove(self.board[to].piece)
        self.board[to].piece=self.board[fr].piece
        self.board[fr].piece=None
        self.board[to].piece.square=to

    def isWhiteKingChecked(self):
        for p in self.blackPieces:
            if self.whiteKingsSquare in self.whatSquaresDoIControll(p):
                return True
        return False



    def isWhiteKingGoingToBeChecked(self,fr,to):
        tempGame=copy.deepcopy(self)
        tempGame.move(fr,to)
        return tempGame.isWhiteKingChecked()

