class Piece:
    def __init__(self,color,initialSquare,pieceType):
        self.color=color
        self.square=initialSquare
        self.pieceType=pieceType
    def get_color(self):
        return self.color
    def set_color(self,color):
        self.color=color
    def equals(self,piece):
        return type(self)==type(piece) and self.pieceType==piece.pieceType and self.square==piece.square and self.color==piece.color
    def __str__(self):
        return self.color[0]+self.pieceType

class Pawn(Piece):
    def __init__(self,color,initialSquare):
        super().__init__(color,initialSquare,pieceType='P')


class Rook(Piece):
    def __init__(self,color,initialSquare):
        super().__init__(color,initialSquare,pieceType='R')




class Knight(Piece):
    def __init__(self,color,initialSquare):
        super().__init__(color,initialSquare,pieceType='N')

class Bishop(Piece):
    def __init__(self,color,initialSquare):
        super().__init__(color,initialSquare,pieceType='B')

class Queen(Piece):
    def __init__(self,color,initialSquare):
        super().__init__(color,initialSquare,pieceType='Q')

class King(Piece):
    def __init__(self,color,initialSquare):
        super().__init__(color,initialSquare,pieceType='K')