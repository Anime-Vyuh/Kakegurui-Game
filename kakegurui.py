import string,time
import random,sys
from intro import kakegurui_intro

def display_rules():
    print('''
    Try your luck
    Idea taken from: KAKEGURUI Season 1 episode 4

    INDIAN POKER (deck of 40 cards with joker and face card removed)

    game rules, read this before playing
    rule 0: 2 players will play the game simultaneously which is 40 deck card Indian poker
    rule 1: 1000 chips will be provided initially, game starts with 50 chip as fee and 2 cards to each player
    rule 2: minimum of 25 chips can be bet at a time
    rule 3: maximum of 100 chips can be bet at a time
    rule 4: game will continue till the players give up or chip is 0 and player lose the bet
    rule 5: type1:PAIR denotes same number
    rule 6: type2:SUIT denotes same house
    rule 7: type3:PIG denotes different house and different number
    rule 8: if both the player have same type, higher sum is the winner

    SO COME ON LETS GET KAKEGURUI FREAK ON
    \n ''')

# heart(H), spade(S), club(C), diamond(D)

def deck_cards():
    num=list(range(2,11)) #it is a 40 card deck game with face card removed
    suits = ['S','H','C','D']
    deck = []
    for ace_card in range(len(suits)): #this for loop appends ace cards in the deck
        ace=suits[ace_card]+'A'
        deck.append(ace)
    for suits_card in num:
        for s in suits:
            card = s+str(suits_card)
            deck.append(card)
    random.shuffle(deck) #shuffles the 40 deck 
    return deck

def get_cards(deck40):
    #lets consider A as 11 while addition for higher cards
    #p1c - player 1 random cards
    #p2c - player 2 random cards
    p1c,p2c = [],[]
    for i in range(2):
        p1c.append(random.choice(deck40))
        p2c.append(random.choice(deck40))
    return(p1c,p2c)

def display1card(sp1c,sp2c): #show 1 card out of 2 to both the players
    print("Warning: Displaying just one card of player 1.........\n")
    time.sleep(3)
    print("One of the card of player 1 is: \n")
    print('*' * 10)
    for i in range(5):
        if i == 2:
            print('*   ' +random.choice(sp1c) + '   *')
            continue
        print('*' + ' ' * 8 + '*')
    print('*' * 10)
    time.sleep(3)
    #this for loop below is just a distraction provided so that the other player should not see each other cards
    for i in range(10000):
        print(random.choice(string.ascii_letters), end='')
        if i in (50, 100, 150,200,250, 290, 320, 350, 380):
            print('')
    time.sleep(3)
    print("\n Warning: Displaying just one card of player 2.........\n")
    time.sleep(3)
    print("One of the card of player 2 is: \n")
    print('*' * 10)
    for i in range(5):
        if i == 2:
            print('*   ' +random.choice(sp2c)+ '   *')
            continue
        print('*' + ' ' * 8 + '*')
    print('*' * 10)
    time.sleep(4)
    for i in range(10000):
        print(random.choice(string.ascii_letters), end='')
        if i in (30,100,170, 200, 230, 250, 290, 320, 350, 380):
            print('')
    time.sleep(2)
    print('\n')

def bet(chips1, chips2, name1, name2):
    print('Collecting match fee of 50 chips each....')
    time.sleep(1.5)
    chips1 = chips1 - 50
    chips2 = chips2 - 50
    print('Lets get the Kakegurui freak on')
    time.sleep(2)
    while chips1>0 and chips2>0:
        #player1 bets here
        while True:
            try:
                bet1 = int(input(f'{name1}, place your bet(20<chips<100): '))
                if bet1 < 20 or bet1 > 100:
                    print("Enter a valid bet: ")
                    continue
                chips1 = chips1 - bet1
                if chips1 < 0:
                    print('You can only place bet in range under', abs(chips1+bet1), end='')
                    continue
                if chips1<20:
                    print(name1, 'your are out of chips')
                    break
                print('Balance player1', chips1)
                break
            except Exception:
                continue
            #used try and except coz it should only accept validate number

#player2 bets here
        while True:
            try:
                bet2 = int(input(f"{name2},place your bet(20<chips<100): "))
                if bet2 < 20 or bet2 > 100:
                    print('Enter a valid bet: ')
                    continue
                chips2 = chips2 - bet2
                if chips2 < 0:
                    print('You can only place bet in range under', abs(chips2))
                    continue
                if chips2<20:
                    print(name2, 'your are out of chips')
                    break
                print('Balance', chips2)
                break
            except Exception:
                continue
        continue

def show(p1c,p2c):
    print('Player 1 cards:',p1c)
    print('Player 2 cards:',p2c)

def pair():
    pass
def suit():
    pass
def pig():
    pass

def play_again():
    play = input('Do you wanna play again?(Y/n)').lower()
    if play.startswith('y'):
        return True
    else:
        sys.exit()

while True:
    print(kakegurui_intro) #the intro py module just displays the game intro design
    #enter players name
    game_rules=input('Do you want to see the game rules(y/n):').lower()
    if 'y' in game_rules:
        display_rules()
    deck40=deck_cards()
    player1=input('Enter player 1 name:')
    while player1=='' or player1 in string.digits or player1 in string.punctuation:
        player1=input('Enter player 1 name:')
        continue
    player2=input('Enter player 2 name:')
    while player2=='' or player2 in string.digits or player2 in string.punctuation:
        player2=input('Enter player 2 name:')
        continue
    chips1,chips2=500,500
    #choose cards
    k = get_cards(deck40)
    card_p1, card_p2 = k[0], k[1]
    display1card(card_p1,card_p2)
    bet(chips1,chips2,player1,player2)
    show(card_p1,card_p2)
    play_again()
    break