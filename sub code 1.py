import random
def display_cards():
    #i will consider A as 11 while addition
    club='C2 C3 C4 C5 C6 C7 C8 C9 C10 CA'.split()
    spades='S2 S3 S4 S5 S6 S7 S8 S9 S10 SA'.split()
    heart='H2 H3 H4 H5 H6 H7 H8 H9 H10 HA'.split()
    diamond='D2 D3 D4 D5 D6 D7 D8 D9 D10 DA'.split()
    p1c = []
    p2c = []
    for i in range(2):
        p1c.append(random.choice(club + spades + heart + diamond))
        p2c.append(random.choice(club + spades + heart + diamond))

    return(p1c,p2c)

k=display_cards()
print(k[0])
print(k[1])
print(k[0][0][:1])
print(k[0][1][:1])
print(k[1][1][:1])
print(k[1][0][:1])

if k[0][0][:1] == k[0][1][:1] and k[1][0][:1] != k[1][1][:1]:
    print("Player 1 Won, Due to Pair")

if k[0][0][:1] != k[0][1][:1] and k[1][0][:1] == k[1][1][:1]:
    print("Player 2 Won, Due to Pair")
