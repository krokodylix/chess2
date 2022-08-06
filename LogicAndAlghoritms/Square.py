class Square:
    def __init__(self,index):
        self.index=index
        self.piece=None
    def __str__(self):
        if self.piece==None:
            return 'oo'
        else:
            return str(self.piece)