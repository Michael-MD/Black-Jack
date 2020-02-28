from blackjack import *
from gui import *


root = Tk()
root.title("BlackJack")

mainWindow = Window(root)

# create classes
dealer = Dealer()
player = Player()

#create deck and shiffle
gameDeck = Deck()
gameDeck.shuffle()


# player card classes
playerCardClasses = []
# dealer card classes
dealerCardClasses = []

# place labels
totalTextD = str(dealer.total()["soft"])+"/"+str(dealer.total()["hard"])
dealerShow = addLabel(root,totalTextD,0,0)

totalTextP = str(player.total()["soft"])+"/"+str(player.total()["hard"])
playerShow = addLabel(root, totalTextP ,0,1)


def hit():
	global player
	global playerShow
	player.giveCard( gameDeck.deal() )
	playerCard1 = addCardPlayer(root,"deck_cards/"+ player.cards[-1] +".png")
	playerCardClasses.append(playerCard1)

	totalTextP = str(player.total()["soft"])+"/"+str(player.total()["hard"])
	playerShow.labelh.config(text=totalTextP)

	if(player.total()["hard"] > 21):
		stand()


# give dealer one card now and another later when the player stands 
cardName = gameDeck.deal()
dealer.giveCard( gameDeck.deal() )
dealerCard1 = addCardDealer(root,"deck_cards/"+ dealer.cards[-1] +".png")
dealerCardClasses.append(dealerCard1)

totalTextD = str(dealer.total()["soft"])+"/"+str(dealer.total()["hard"])
dealerShow = addLabel(root,totalTextD,0,0)

print( dealer.cards[0] )	#print card to console

# #give player two cards
for a in range(0,2):
	player.giveCard( gameDeck.deal() )
	playerCard1 = addCardPlayer(root,"deck_cards/"+ player.cards[-1] +".png")
	playerCardClasses.append(playerCard1)

totalTextP = str(player.total()["soft"])+"/"+str(player.total()["hard"])
playerShow.labelh.config(text=totalTextP)

def winner(dealerCards,playerCards):
	winnerLabel = addLabel(root,"",2,2)

	if(dealerCards["hard"] > 21 and dealerCards["soft"] > 21):
		print("Player Wins")
		winnerLabel.labelh.config(text="Player Wins")
		return None
	else:
		subTotalDealer = dealerCards["soft"]
	if(playerCards["hard"] > 21 and playerCards["soft"] > 21):
		print("Dealer Wins")
		winnerLabel.labelh.config(text="Dealer Wins")
		return None
	else:
		subTotalPlayer = playerCards["soft"]

	if(subTotalDealer > subTotalPlayer):
		print("Dealer Wins")
		winnerLabel.labelh.config(text="Dealer Wins")
		return None
	elif(subTotalDealer < subTotalPlayer):
		print("Player Wins")
		winnerLabel.labelh.config(text="Player Wins")
		return None

	if(subTotalDealer == subTotalPlayer):
		print("Push")
		winnerLabel.labelh.config(text="Push")

	if(dealerCards["hard"] > 21 and playerCards["hard"] > 21):
		print("Push")
		winnerLabel.labelh.config(text="Push")




def stand():
	global dealer
	global gameDeck
	global root
	global dealerCardClasses

	#check if total is 16 or less
	while True:	#deal
		if( dealer.total()["hard"] <= 16 ):
			dealer.giveCard( gameDeck.deal() )
			dealerCard1 = addCardDealer(root,"deck_cards/"+ dealer.cards[-1] +".png")
			dealerCardClasses.append(dealerCard1)

			if(dealer.overall >= 21):
				break
		else: #greater than 16 so stop
			break

	print( dealer.cards )
	print( dealer.total() )

	totalTextD = str(dealer.total()["soft"])+"/"+str(dealer.total()["hard"])
	dealerShow = addLabel(root,totalTextD,0,0)

	winner(dealer.total(),player.total())

#create player options buttons
hitButton = addButton(root,"Hit",0,2,hit)
surrenderButton = addButton(root,"Stand",1,2,stand)


# #player has now played, dealer will now play
# #dealer will always use hard
# The dealer's moves are placed in the stand function




root.mainloop()