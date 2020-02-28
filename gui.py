from tkinter import *

class Window:
    def __init__(self, master):  # this function doesnt needs to be called explicitly
        frame = Frame(master)
        frame.grid(column = 0, row = 0)


columnPlaceDealer = 1
class addCardDealer:	
	def __init__(self,master,card):
		global columnPlaceDealer
		self.image1 = PhotoImage(file = card)
		imageh = Label(master,image=self.image1)
		imageh.grid(column = columnPlaceDealer, row = 0)

		if(columnPlaceDealer == 1):	# the second card
			self.image2 = PhotoImage(file = "deck_cards/back.png")
			imageh = Label(master,image=self.image2)
			imageh.grid(column = 2, row = 0)

		columnPlaceDealer+=1


columnPlacePlayer = 1
class addCardPlayer:
	def __init__(self,master,card):
		global columnPlacePlayer
		self.image1 = PhotoImage(file = card)
		imageh = Label(master,image=self.image1)
		imageh.grid(column = columnPlacePlayer, row = 1)

		columnPlacePlayer+=1

class addButton():
	def __init__(self,master,textP,columnP,rowP,commandP=None):
		self.buttonh = Button(master,text=textP,command=commandP)
		self.buttonh.grid(column=columnP,row=rowP)

class addLabel():
	def __init__(self,master,textP,columnP,rowP):
		self.labelh = Label(master,text=textP)
		self.labelh.grid(column=columnP,row=rowP)




