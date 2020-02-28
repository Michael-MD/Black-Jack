import gui

class Card:
	def __init__(self,value,suit,color):
		self.number = value
		self.suit = suit
		self.color = color

	def name(self):
		return "%s of %s"%(self.number,self.suit)

import random as rand

class Deck:
	def __init__(self):
		self.numbers = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
		self.suits = ["Hearts","Diamonds","Clubs","Spades"]

		self.deck = []
		self.deckVals = []
		# create deck
		for suit in self.suits:
			for num in self.numbers:
				#create card instance
				card = Card(num,suit,"black")
				self.deck.append(card.name())
				self.deckVals.append(num)

	def shuffle(self):
		for a in range(1,500):
			while True:
				self.pos1 = rand.randint(0,len(self.deck)-1)
				self.pos2 = rand.randint(0,len(self.deck)-1)

				if self.pos1 != self.pos2:
					break

			self.val1 = self.deck[self.pos1]
			self.val2 = self.deck[self.pos2]

			self.deck[self.pos1] = self.val2
			self.deck[self.pos2] = self.val1


			self.val1 = self.deckVals[self.pos1]
			self.val2 = self.deckVals[self.pos2]

			self.deckVals[self.pos1] = self.val2
			self.deckVals[self.pos2] = self.val1

	def randomCard(self):
		return self.deck[rand.randint(0,len(self.deck)-1)]

	def deal(self):
		return [self.deck.pop(),self.deckVals.pop()]
		

class Dealer:
	def __init__(self):
		self.cards = []
		self.cardVals = []
		self.sum = {"soft":0,"hard":0}
		self.overall = 0

	def giveCard(self,card):
		self.cards.append(card[0])
		self.cardVals.append(card[1])

		self.total()

		#decide weather to take hard or soft
		if(self.sum["soft"] <= 21):
			self.overall = self.sum["soft"]
		else:
			self.overall = self.sum["hard"]

	def total(self):
		#soft,hard
		self.sum = {"soft":0,"hard":0}
		for card in self.cardVals:
			if(card == "Jack" or card == "Queen" or card == "King"):
				self.sum["soft"]+=10 #soft
				self.sum["hard"]+=10 #hard
			elif(card == "Ace"):
				self.sum["soft"]+=11 #soft
				self.sum["hard"]+=1 #hard
			else:
				self.sum["soft"]+=int(card) #soft
				self.sum["hard"]+=int(card) #hard

		return self.sum

class Player(Dealer):
	#player can double, surrender
	def double(self):
		pass

