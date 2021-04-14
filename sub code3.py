import time
def bet(chips1, chips2, name1, name2):
    print('Collecting match fee of 50 chips each....')
    time.sleep(1.5)
    chips1 = chips1 - 50
    chips2 = chips2 - 50
    print('Lets get the Kakegurui freak on')
    time.sleep(2)

    while chips1>20 and chips2>20:
        #player1 bets here
        while True:
            try:
                bet1 = int(input(f'{name1}, place your bet(20<chips<100): '))
                if bet1 < 20 or bet1 > 100:
                    print("Enter a valid bet: ")
                    continue
                if chips1 < bet1:
                    print('You can only place bet in range under',chips1, end='')
                    continue
                chips1 = chips1 - bet1

                print('Balance player1', chips1)
                break

            except Exception:
                 continue
            # used try and except coz it should only accept validate number

        if chips1<20:
            print(name1, 'your are out of chips')
            break


#player2 bets here
        while True:
            try:
                bet2 = int(input(f"{name2},place your bet(20<chips<100): "))
                if bet2 < 20 or bet2 > 100:
                    print('Enter a valid bet: ')
                    continue

                if chips2 < bet2:
                    print('You can only place bet in range under', chips2)
                    continue

                chips2 = chips2 - bet2

                print('Balance', chips2)
                break
            except Exception:
                continue

        if chips2 < 20:
            print(name2, 'your are out of chips')
            break

bet(500,500,'Tarun','Rahul')