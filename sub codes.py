player1 = 'SA HA'.split()
player2 = 'D9 H3'.split()
sum=0
for i in range(len(player1)):
    if 'A' in player1[i][1:]:
        player1[i]=player1[i].replace(player1[i][1:], '11')
    sum=sum+int(player1[i][1:])

print(sum)