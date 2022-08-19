import tkinter as tk
from LogicAndAlghoritms import Game


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(False,False)
        backG=tk.Label(self.root)
        backG.place(relx=0,rely=0,relheight=1,relwidth=1)
        backG.config(bg='#B7825F')
        self.game=Game()
        self.game.isGUI=True
        self.images=[]
        self.root.geometry('1000x800')
        self.buttons=[]
        self.fr=-1
        self.to=-1
        self.infoFrame=tk.Frame(self.root)
        self.infoFrame.config(bg='#C4A484')
        self.doWeWaitForChoice=False
        self.infoFrame.place(relx=0.83,rely=0.05,relheight=0.9,relwidth=0.15)
    def sortAr(self):
        for i in range(0,len(self.buttons)):
            for j in range (i+1,len(self.buttons)):
                if self.buttons[j].index<self.buttons[i].index:
                    temp=self.buttons[j]
                    self.buttons[j]=self.buttons[i]
                    self.buttons[i]=temp




    def updateBoard(self):
        for i in range (len(self.game.board)):
            if self.game.board[i].piece!=None:
                self.images[i]=(tk.PhotoImage(file='assets/'+self.game.board[i].piece.color+self.game.board[i].piece.pieceType+'.png'))
            else:
                self.images[i]=(None)
        for button in self.buttons:
            if self.game.board[button.index].piece!=None:
                button.config(image=self.images[button.index])
            else:
                button.config(image="")



    def setDataInGame(self, data):
        if not self.doWeWaitForChoice:
            colors=['white','black']
            if self.fr == -1 or (self.game.board[data].piece!=None and colors[len(self.game.historyOfMoves)%2]==self.game.board[data].piece.color):
                self.fr = data
                return
            if self.fr!=-1 and self.to==-1:
                self.to = data
                if(len(self.game.historyOfMoves)%2==0 and [self.fr,self.to] in self.game.whereWhiteCanGo() ):
                    if self.game.board[self.fr].piece.pieceType=='P' and data>=56:
                        self.showTrans()
                        self.doWeWaitForChoice=True
                        return

                    self.game.move(self.fr, self.to)
                    self.updateBoard()
                    self.labelInfo.config(text='black to move')

                    self.game.choice=-1
                    if len(self.game.whereBlackCanGo())==0 and self.game.isBlackKingChecked():
                        self.labelInfo.config(text='mate, white won')
                    if len(self.game.whereBlackCanGo())==0 and not self.game.isBlackKingChecked():
                        self.labelInfo.config(text='stalemate, draw')
                if(len(self.game.historyOfMoves)%2==1 and [self.fr,self.to] in self.game.whereBlackCanGo() ):
                    if self.game.board[self.fr].piece.pieceType=='P' and data<=7:
                        self.showTrans()
                        self.doWeWaitForChoice=True
                        return

                    self.game.move(self.fr, self.to)
                    self.updateBoard()
                    self.labelInfo.config(text='white to move')
                    if len(self.game.whereWhiteCanGo())==0 and self.game.isWhiteKingChecked():
                        self.labelInfo.config(text='mate, black won')
                    if len(self.game.whereWhiteCanGo())==0 and not self.game.isWhiteKingChecked():
                        self.labelInfo.config(text='stalemate, draw')
                self.fr=-1
                self.to=-1
                return


    def setGamesChoice(self,choice):
        if len(self.game.historyOfMoves)%2==0:
            self.game.choice=choice
            self.game.move(self.fr, self.to)
            self.updateBoard()
            self.labelInfo.config(text='black to move')
            self.doWeWaitForChoice=False
            self.game.choice = -1
            self.stopShowingTrans()
            if len(self.game.whereBlackCanGo()) == 0 and self.game.isBlackKingChecked():
                self.labelInfo.config(text='mate, white won')
            if len(self.game.whereBlackCanGo()) == 0 and not self.game.isBlackKingChecked():
                self.labelInfo.config(text='stalemate, draw')
            print(choice)
        else:
            self.game.choice=choice
            self.game.move(self.fr, self.to)
            self.updateBoard()
            self.labelInfo.config(text='white to move')
            self.doWeWaitForChoice=False
            self.game.choice = -1
            self.stopShowingTrans()
            if len(self.game.whereWhiteCanGo()) == 0 and self.game.isWhiteKingChecked():
                self.labelInfo.config(text='mate, black won')
            if len(self.game.whereWhiteCanGo()) == 0 and not self.game.isWhiteKingChecked():
                self.labelInfo.config(text='stalemate, draw')
            print(choice)
        self.fr = -1
        self.to = -1
    def showTrans(self):
        for i in range(4):
            b = tk.Button(self.infoFrame)
            b.place(relx=0.25, rely=0.3 + 0.15 * i, relwidth=0.5, relheight=0.1)
            b.config(image=self.trans[(len(self.game.historyOfMoves)+1) % 2 ][i], command=lambda x=i:self.setGamesChoice(x+1))
    def stopShowingTrans(self):
        l=tk.Label(self.infoFrame)
        l.place(relx=0.25,rely=0.3,relwidth=0.5,relheight=0.6)
        l.config(bg='#C4A484')
    def run(self):

        frame=tk.Frame(self.root,bg='pink')
        frame.place(relx=0.1,rely=0.05,relheight=0.9,relwidth=0.72)
        lab=tk.Label(frame)
        lab.place(relx=0,rely=0,relheight=1,relwidth=1)
        bg=tk.PhotoImage(file='assets/frame.png')
        lab.config(image=bg)

        for sqr in self.game.board:
            if sqr.piece!=None:
                self.images.append(tk.PhotoImage(file='assets/'+sqr.piece.color+sqr.piece.pieceType+'.png'))
            else:
                self.images.append(None)


        for y in range(8):
            for x in range(8):
                if self.images[56-8*y+x]==None:
                    button = GUIButton(56-8*y+x,frame)

                else:
                    button = GUIButton(56-8*y+x,frame, image=self.images[56-8*y+x])
                if(x+y)%2==1:
                    button.config(bg='#C4A484',activebackground='#C4A484')
                button.config(command=lambda x=button.index:self.setDataInGame(x))
                button.place(relx=0.1+x*0.1,rely=0.1+y*0.1,relheight=0.1,relwidth=0.1)
                self.buttons.append(button)
        self.labelInfo=tk.Label(self.infoFrame)
        self.labelInfo.place(relx=0,rely=0.1,relwidth=1,relheight=0.15)
        self.labelInfo.config(text='white to move',font=("Arial",15),bg='#C4A484')
        self.sortAr()

        self.trans=[[tk.PhotoImage(file='assets/blackQ.png'),tk.PhotoImage(file='assets/blackR.png'),tk.PhotoImage(file='assets/blackN.png'),tk.PhotoImage(file='assets/blackB.png')],[tk.PhotoImage(file='assets/whiteQ.png'),tk.PhotoImage(file='assets/whiteR.png'),tk.PhotoImage(file='assets/whiteN.png'),tk.PhotoImage(file='assets/whiteB.png')]]
        self.root.mainloop()





class GUIButton(tk.Button):
    def __init__(self,index,parent,*args,**kwargs):
        tk.Button.__init__(self,parent,*args,**kwargs)
        self.index=index