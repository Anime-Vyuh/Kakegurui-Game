import string,time
import random,sys,pygame
import os
import termcolor

dialog_path = os.path.join("assets","yumeko.ogg")

def display_rules():
    termcolor.cprint('''
    Try your luck
    Idea taken from: KAKEGURUI Season 1 episode 4

    INDIAN POKER (deck of 40 cards with joker and face card removed)

    game rules, read this before playing
    [here player 2 is  computer]
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
    \n ''',"green")

# heart(H), spade(S), club(C), diamond(D)

def deck_cards():
    num=list(range(2,11)) #it is a 40 card deck game with face card removed
    suits = ['S','H','C','D']
    deck = []
    for ace_card in suits: #this for loop appends ace cards in the deck
        deck.append(ace_card+'A')
    for suits_card in num:
        for s in suits:
            card = s+str(suits_card)
            deck.append(card)
    random.shuffle(deck) #shuffles the 40 deck
    return deck

def get_cards(deck40):
    #lets consider A as 11 while addition for higher cards
    #p1c - player 1 random cards
    #computer - computer random cards
    p1c,comp = [],[]
    for i in range(2):
        p1c.append(random.choice(deck40))
        comp.append(random.choice(deck40))
    return(p1c,comp)

def display1card_toPlayer(sp1c): #show 1 card out of 2 to the player
    print("Displaying 1 card out of 2 to the Player")
    print("\n\n Your Card:{} \n\n".format(random.choice(sp1c)))

def bet(chips1, chips2, name,card_player1,card_player2,total_chips_won):
    print('Collecting match fee of 1 chip each....')
    chips1-=1
    chips2-=1
    time.sleep(3)
    while True:
        try:
            player1_bet = int(input("{}; Enter your bet in range(1-5) or 0 to show: ".format(name)))
            comp_bet = random.randint(0,5)
            if player1_bet==0:
                confirm = input("Are you filling to show?(Y/n)").lower()
                if confirm.startswith("y"):
                    termcolor.cprint("{} decides to show".format(name),"red")
                    winner(name,card_player1,card_player2,total_chips_won,chips1,chips2)
                    break
                else:
                    continue
            if comp_bet==0:
                termcolor.cprint("Computer Decided to Show","red")
                winner(name,card_player1,card_player2,total_chips_won,chips1,chips2)
                break
            elif player1_bet in range(1,6):
                if chips1>1 and chips2>1:
                    chips1 = chips1-player1_bet
                    print("Computer Placed His Bet:{}".format(comp_bet))
                    chips2 = chips2-comp_bet
                    total_chips_won += player1_bet+comp_bet
                else:
                    print("Insuffient Chip, you are forced to show")
                    winner(name,card_player1,card_player2,total_chips_won,chips1,chips2)
                    break
            else:
                print("Invalid Bet Range(1-5) or 0 to show")
                continue
            termcolor.cprint("Your Available Chips:{}".format(chips1),"blue")
            termcolor.cprint("Computer Available Chips:{}".format(chips2),"blue")
        except ValueError:
            print("Illegal entry")

"""def show(p1c,p2c):
    print('Player 1 cards:',p1c)
    print('Player 2 cards:',p2c)"""

def cards_showdown(player1_card,comp_card):
    print("Player 1 cards:{}".format(player1_card))
    print("Computer cards:{}".format(comp_card))

def winner(p1name,player1_card,comp_card,total_chips_won,chips1,chips2):
    #addition of higher card is important when both player gets same card or pig

    # if both player as pair, higher card wins
    sum_for_same_pair_p1=sum_for_same_pair_p2=0   #sum of both player p1 and p2
    #if both player as suit, same house
    sum_for_same_suit_p1=sum_for_same_suit_p2=0
    #if both as a pig
    sum_for_pig_p1=sum_for_pig_p2=0

    #checking for the pair
    if player1_card[0][1:] == player1_card[1][1:] and comp_card[0][1:] != comp_card[1][1:]:
        chips1+=total_chips_won
        print("{} won, Pair of number".format(p1name))
        cards_showdown(player1_card,comp_card)
    elif player1_card[0][1:] != player1_card[1][1:] and comp_card[0][1:] == comp_card[1][1:]:
        chips2+=total_chips_won
        print("{} won, Pair of number".format("Computer"))
        cards_showdown(player1_card,comp_card)
    elif player1_card[0][1:] == player1_card[1][1:] and comp_card[0][1:] == comp_card[1][1:]:
        for player1 in range(len(player1_card)):
            if 'A' in player1_card[player1][1:]:
                player1_card[player1] = player1_card[player1].replace(player1_card[player1][1:], '11')
            sum_for_same_pair_p1 = sum_for_same_pair_p1 + int(player1_card[player1][1:])
        for player2 in range(len(comp_card)):
            if 'A' in comp_card[player2][1:]:
                comp_card[player2] = comp_card[player2].replace(comp_card[player2][1:], '11')
            sum_for_same_pair_p2 = sum_for_same_pair_p2 + int(comp_card[player2][1:])
        if sum_for_same_pair_p1 > sum_for_same_pair_p2:
            print("{} won, as a Higher Pair card".format(p1name))
            chips1+=total_chips_won
            cards_showdown(player1_card,comp_card)
        else:
            chips2+=total_chips_won
            print("{} won, as a Higher Pair card".format("Computer"))
            cards_showdown(player1_card,comp_card)

    elif player1_card[0][:1] == player1_card[1][:1] and comp_card[0][:1] != comp_card[1][:1]:
        chips1+=total_chips_won
        print("{} won, Higher Suits".format(p1name))
        cards_showdown(player1_card,comp_card)
    elif player1_card[0][:1] != player1_card[1][:1] and comp_card[0][:1] == comp_card[1][:1]:
        chips2+=total_chips_won
        print("{} won, Higher Suits".format("Computer"))
        cards_showdown(player1_card,comp_card)
    elif player1_card[0][:1] == player1_card[1][:1] and comp_card[0][:1] == comp_card[1][:1]:
        for player1 in range(len(player1_card)):
            if 'A' in player1_card[player1][1:]:
                player1_card[player1] = player1_card[player1].replace(player1_card[player1][1:], '11')
            sum_for_same_suit_p1 = sum_for_same_suit_p1 + int(player1_card[player1][1:])
        for player2 in range(len(comp_card)):
            if 'A' in comp_card[player2][1:]:
                comp_card[player2] = comp_card[player2].replace(comp_card[player2][1:], '11')
            sum_for_same_suit_p2 = sum_for_same_suit_p2 + int(comp_card[player2][1:])
        if sum_for_same_suit_p1 > sum_for_same_suit_p2:
            print("{} won, as a Higher Suit card".format(p1name))
            cards_showdown(player1_card,comp_card)
            chips1+=total_chips_won
        else:
            chips2+=total_chips_won
            print("{} won, as a Higher Suit card".format("Computer"))
            cards_showdown(player1_card,comp_card)
    else:
        for player1 in range(len(player1_card)):
            if 'A' in player1_card[player1][1:]:
                player1_card[player1] = player1_card[player1].replace(player1_card[player1][1:], '11')
            sum_for_pig_p1 = sum_for_pig_p1 + int(player1_card[player1][1:])
        for player2 in range(len(comp_card)):
            if 'A' in comp_card[player2][1:]:
                comp_card[player2] = comp_card[player2].replace(comp_card[player2][1:], '11')
            sum_for_pig_p2 = sum_for_pig_p2 + int(comp_card[player2][1:])
        if sum_for_pig_p1 > sum_for_pig_p2:
            chips1+=total_chips_won
            print("{} won, as a Higher Pig card".format(p1name))
            cards_showdown(player1_card,comp_card)
        else:
            chips2+=total_chips_won
            print("{} won, as a Higher Pig card".format("Computer"))
            cards_showdown(player1_card,comp_card)
    return chips1,chips2

def play_again():
    play = input('Do you wanna play again?(Y/n)').lower()
    if play.startswith('y'):
        return True
    else:
        print("Thank You For Playing")
        sys.exit()

game_rules=input('Do you want to see the game rules(y/n):').lower()
if 'y' in game_rules:
    display_rules()
deck40=deck_cards()
total_chips_won = 0
round=1
pygame.init()
chips1,chips2=100,100
player=input('Enter player name:')
pygame.mixer.music.load(dialog_path)
pygame.mixer.music.play(loops=1)
termcolor.cprint('Lets get the Kakegurui freak on',"red")

while True:
    #choose cards
    player_card = get_cards(deck40)
    card_p1, card_comp = player_card[0], player_card[1]
    time.sleep(1.5)
    display1card_toPlayer(card_p1)
    bet(chips1,chips2,player,card_p1,card_comp,total_chips_won)

    chips1,chips2 = winner(player,card_p1,card_comp)
    round +=1
    if round > 10:
        play_again()

    print("\n\n\tRound {} begins \n\n".format(round))
    time.sleep(5)
    continue