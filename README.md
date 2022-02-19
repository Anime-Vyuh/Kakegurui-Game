# Kakegurui Indian Poker

<img src="https://i.pinimg.com/originals/63/8b/b4/638bb431c597836bfa701f99e4f93e2d.gif" alt="Yumeko-Mary_Kakegurui">

## Rules

- Each group of 4 plays with Deck of 40 cards instead of 52, with all the face cards and joker removed. 
- The dealer will pass out 2 cards to each player. 
- Initially 10 chips is provided to each player, which add up to total of their debt. If you do the calculation, each chips costs 1/10 of the players's debt, so it is not like a normal poker where the actual sum matters. 
- The game will be played for 10 Rounds, each ayer needs to pay at least one chip in each round to participate. 
- Furthermore, players may only bet up to 5 chips at once. Players can fold, when they are not willing to bet.
- The strongest hand is Pair, where the number match. Up next is Suit, where the club match. And the weakest is pig, where there is no similarly in the cards. 
- In case if multiplayer players  have the same hand then winner is decided by highest sum of the cards. 

## Python Code

Few rules modification has been made here.
- Instead of 4 or 5 players, this code is programmed only for 2 players i.e., you and the computer. 
- Programming it for 4 to 5 players is no nig deal but since it is command line Python Code, 1 player vs Computer is the most preferable. 
- Ok moving on to the next modification. There is no debt imposed on the player, instead chips are at stake. Players compete with computers starting with 20 chips. 
- Match fee of 1 chip is collected after every round. 
- Once the fee is collected, the player is supposed to bet in a range of 1-5. And 0 is to Show or Fold when you are not willing to bet. 

## Termcolor

Adds up great look to the output statements by changing the color of the output. It is easy to implement.

```py
termcolor.cprint("Message","color") #syntax
termcolor.cprint("Anime Vyuh","red") #example
```
