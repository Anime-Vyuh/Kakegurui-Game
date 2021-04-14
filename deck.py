import random

def build_deck():
    num=list(range(2,11)) #it is a 40 card deck game with face card removed
    suits = ['S','H','C','D']
    deck = []
    for ace_card in range(len(suits)):
        ace=suits[ace_card]+'A'
        deck.append(ace)
    for i in num:
        for s in suits:
            card = s+str(i)
            deck.append(card)
    random.shuffle(deck)    #shuffles the deck, make sure not to assign it.
    return deck

k=build_deck()
print(k)
print(len(k)) #it should be 40 as its 40 card deck game