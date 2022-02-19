import string,time
import random,sys,pygame
import os
import termcolor

dialog_path = os.path.join("assets","yumeko.ogg")

class Kakegurui:

    def __init__(self,player):
        self.player_name = player
        self.chips1 = 20
        self.chips2 = 20
        self.total_chips_won = 0
        self.player1_card,self.computer_card = [],[]

    def display_rules(self):
        termcolor.cprint('''
        Try your luck
        Idea taken from: KAKEGURUI Season 1 episode 4

        INDIAN POKER (deck of 40 cards with joker and face card removed)

        game rules, read this before playing
        [here player 2 is  computer]
        rule 0: Player will play the game with computer; the game is 40 deck card Indian poker
        rule 1: 20 chips will be provided initially, game starts with 1 chip as fee
        rule 1.1: 2 cards each will be provided to both player and computer
        rule 2: minimum of 1 and maximum of 5 chips can be bet at a time
        rule 3: 0 to show the cards
        rule 4: game will continue till the players give up(i.e., show=0) or chip is 0 and player lose the bet
        rule 5: type1:PAIR denotes same number
        rule 6: type2:SUIT denotes same house
        rule 7: type3:PIG denotes different house and different number
        rule 8: if both the player and computer have same type, higher sum is the winner
        Note: type1>type2>type3
        \n ''',"green")

    # heart(H), spade(S), club(C), diamond(D)

    def deck_cards(self):
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

    def get_cards(self,deck40):
        #lets consider A as 11 while addition for higher cards
        #self.player1_card - player 1 random cards
        #computer_card - computer random cards
        for i in range(2):
            self.player1_card.append(random.choice(deck40))
            self.computer_card.append(random.choice(deck40))


    def display1card_toPlayer(self): #show 1 card out of 2 to the player
        print("Displaying 1 card out of 2 to the Player")
        print("\n\n Your Card:{} \n\n".format(random.choice(self.player1_card)))

    def bet(self):
        print("Current Available Chips of {}:{}.".format(self.player_name,self.chips1))
        print("Current Available Chips of Computer:{}.\n".format(self.chips2))
        print('Collecting match fee of 1 chip each....')
        self.chips1 -= 1
        self.chips2 -= 1
        time.sleep(3)
        while True:
            try:
                player1_bet = int(input("{}; Enter your bet in range(1-5) or 0 to show: ".format(self.player_name)))
                if player1_bet==0:
                    confirm = input("Are you filling to show?(Y/n)").lower()
                    if confirm.startswith("y"):
                        termcolor.cprint("{} decides to show".format(self.player_name),"red")
                        self.winner()
                        break
                    else:
                        continue
                elif player1_bet in range(1,6):
                    comp_bet = random.randint(0,5)
                    if self.chips1>1 and self.chips2>1 and comp_bet<self.chips2 and self.chips1>player1_bet:
                        self.chips1 = self.chips1-player1_bet
                        self.total_chips_won+=player1_bet
                        if comp_bet==0:
                            termcolor.cprint("Computer Decided to Show","red")
                            self.winner()
                            break
                        print("Computer Placed His Bet:{}".format(comp_bet))
                        self.chips2 = self.chips2-comp_bet
                        self.total_chips_won += comp_bet
                    else:
                        print("\nInsuffient Chip, forced to show")
                        self.winner()
                        break
                else:
                    print("Invalid Bet Range(1-5) or 0 to show")
                    continue
                termcolor.cprint("Your Available Chips:{}".format(self.chips1),"blue")
                termcolor.cprint("Computer Available Chips:{}".format(self.chips2),"blue")
            except ValueError:
                print("Illegal entry")

    def cards_showdown(self):
        print("Player 1 cards:{}".format(self.player1_card))
        print("Computer cards:{}".format(self.computer_card))

    def player_wins(self,how):
        self.chips1+=self.total_chips_won
        termcolor.cprint("\n{} won, {}".format(self.player_name.capitalize(),how),"red")
        termcolor.cprint("Total Chips Won By {} is: {}.\n".format(self.player_name,self.total_chips_won),"blue")

    def computer_wins(self,how):
        self.chips2+=self.total_chips_won
        termcolor.cprint("\nComputer won, {}".format(how),"red")
        termcolor.cprint("Total Chips Won By Computer is: {}.\n".format(self.total_chips_won),"blue")

    def conclude(self):
        won_by = self.player_name if self.chips1>self.chips2 else "Computer"
        termcolor.cprint(f"{won_by.capitalize()} Won","green")
        if self.play_again():
            main()

    def winner(self):
        #addition of higher card is important when both player gets same card or pig

        # if both player has pair, higher card wins
        sum_for_same_pair_p1=sum_for_same_pair_p2=0   #sum of both player p1 and p2
        #if both player has suit, same house
        sum_for_same_suit_p1=sum_for_same_suit_p2=0
        #if both has a pig
        sum_for_pig_p1=sum_for_pig_p2=0

        #checking for the pair
        if self.player1_card[0][1:] == self.player1_card[1][1:] and self.computer_card[0][1:] != self.computer_card[1][1:]:
            self.player_wins(how="Pair Of Number")
            self.cards_showdown()
        elif self.player1_card[0][1:] != self.player1_card[1][1:] and self.computer_card[0][1:] == self.computer_card[1][1:]:
            self.computer_wins(how="Pair Of Number")
            self.cards_showdown()
        elif self.player1_card[0][1:] == self.player1_card[1][1:] and self.computer_card[0][1:] == self.computer_card[1][1:]:
            for player1 in range(len(self.player1_card)):
                if 'A' in self.player1_card[player1][1:]:
                    self.player1_card[player1] = self.player1_card[player1].replace(self.player1_card[player1][1:], '11')
                sum_for_same_pair_p1 = sum_for_same_pair_p1 + int(self.player1_card[player1][1:])
            for player2 in range(len(self.computer_card)):
                if 'A' in self.computer_card[player2][1:]:
                    self.computer_card[player2] = self.computer_card[player2].replace(self.computer_card[player2][1:], '11')
                sum_for_same_pair_p2 = sum_for_same_pair_p2 + int(self.computer_card[player2][1:])
            if sum_for_same_pair_p1 > sum_for_same_pair_p2:
                self.player_wins(how="by a Higher Pair card")
                self.cards_showdown()
            else:
                self.computer_wins(how="by a Higher Pair card")
                self.cards_showdown()

        elif self.player1_card[0][:1] == self.player1_card[1][:1] and self.computer_card[0][:1] != self.computer_card[1][:1]:
            self.player_wins(how="Higher Suits")
            self.cards_showdown()
        elif self.player1_card[0][:1] != self.player1_card[1][:1] and self.computer_card[0][:1] == self.computer_card[1][:1]:
            self.computer_wins(how="Higher Suits")
            self.cards_showdown()
        elif self.player1_card[0][:1] == self.player1_card[1][:1] and self.computer_card[0][:1] == self.computer_card[1][:1]:
            for player1 in range(len(self.player1_card)):
                if 'A' in self.player1_card[player1][1:]:
                    self.player1_card[player1] = self.player1_card[player1].replace(self.player1_card[player1][1:], '11')
                sum_for_same_suit_p1 = sum_for_same_suit_p1 + int(self.player1_card[player1][1:])
            for player2 in range(len(self.computer_card)):
                if 'A' in self.computer_card[player2][1:]:
                    self.computer_card[player2] = self.computer_card[player2].replace(self.computer_card[player2][1:], '11')
                sum_for_same_suit_p2 = sum_for_same_suit_p2 + int(self.computer_card[player2][1:])
            if sum_for_same_suit_p1 > sum_for_same_suit_p2:
                self.player_wins(how="by a Higher Suit Card")
                self.cards_showdown()
            else:
                self.computer_wins(how="by a Higher Suit Card")
                self.cards_showdown()
        else:
            for player1 in range(len(self.player1_card)):
                if 'A' in self.player1_card[player1][1:]:
                    self.player1_card[player1] = self.player1_card[player1].replace(self.player1_card[player1][1:], '11')
                sum_for_pig_p1 = sum_for_pig_p1 + int(self.player1_card[player1][1:])
            for player2 in range(len(self.computer_card)):
                if 'A' in self.computer_card[player2][1:]:
                    self.computer_card[player2] = self.computer_card[player2].replace(self.computer_card[player2][1:], '11')
                sum_for_pig_p2 = sum_for_pig_p2 + int(self.computer_card[player2][1:])
            if sum_for_pig_p1 > sum_for_pig_p2:
                self.player_wins(how="by a Higher Pig Card")
                self.cards_showdown()
            else:
                self.computer_wins(how="by a Higher Pig Card")
                self.cards_showdown()
        self.player1_card.clear()
        self.computer_card.clear()
        self.total_chips_won = 0

    def play_again(self):
        play = input('Do you wanna play again?(Y/n)').lower()
        if play.startswith('y'):
            round = 1
            self.chips1 = 100
            self.chips2 = 100
            self.total_chips_won = 0
            self.player1_card,self.computer_card = [],[]
            return True
        else:
            print("Thank You For Playing")
            sys.exit()

def main():
    player=input('Enter player name:')
    kakeguruiGame = Kakegurui(player)
    pygame.init()

    game_rules=input('Do you want to see the game rules(y/n):').lower()
    if 'y' in game_rules:
        kakeguruiGame.display_rules()
        time.sleep(5)
    pygame.mixer.music.load(dialog_path)
    pygame.mixer.music.play(loops=1)
    deck40=kakeguruiGame.deck_cards()
    round=1
    termcolor.cprint('Lets get the Kakegurui freak on',"red")

    while True:
        #choose cards
        kakeguruiGame.get_cards(deck40)
        time.sleep(1)
        kakeguruiGame.display1card_toPlayer()
        kakeguruiGame.bet()
        round +=1
        if round > 10:
            print("Rounds Over, Genrating Results.....")
            kakeguruiGame.conclude()
            break

        if kakeguruiGame.chips1<2 or kakeguruiGame.chips2<2:
            print("Game ends due to insufficient fund")
            kakeguruiGame.conclude()
            break

        print("\n\n\tRound {} begins \n\n".format(round))
        time.sleep(1.5)
        continue

if __name__ == '__main__':
    main()