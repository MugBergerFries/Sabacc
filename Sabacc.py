suits = ["Staves", "Flasks", "Sabers", "Coins"]
rankedcards = ["Commander", "Mistress", "Master", "Ace"]

deck = {}

for suit in range(0, len(suits)):
	for i in range(1, 12):
		deck.update({"%i of %s" % (i, suits[suit]):i})
	for i in range(0, len(rankedcards)):
		if rankedcards[i] == "Commander":
			value = 12
		if rankedcards[i] == "Mistress":
			value = 13
		if rankedcards[i] == "Master":
			value = 14
		if rankedcards[i] == "Ace":
			value = 15
		deck.update({"%s of %s" % (rankedcards[i], suits[suit]):value})

deck.update({"The Star (Red)":-17})
deck.update({"The Star (Black)":-17})
deck.update({"The Evil One (Red)":-15})
deck.update({"The Evil One (Black)":-15})
deck.update({"Moderation (Red)":-14})
deck.update({"Moderation (Black)":-14})
deck.update({"Demise (Red)":-13})
deck.update({"Demise (Black)":-13})
deck.update({"Balance (Red)":-11})
deck.update({"Balance (Black)":-11})
deck.update({"Endurance (Red)":-8})
deck.update({"Endurance (Black)":-8})
deck.update({"Queen of Air and Darkness (Red)":-2})
deck.update({"Queen of Air and Darkness (Black)":-2})
deck.update({"Idiot (Red)":0})
deck.update({"Idiot (Black)":0})

print len(deck)
print deck

#deal()
#
#print deckdict["Queen of Air and Darkness"]
#
#def deal():
	## some code
#
#def handTotal():