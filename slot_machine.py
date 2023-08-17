import random

symbols = ['🍒','🍇','🍉','🥥','🍏','7️⃣']




def Play():
    for i in range (1,20):
        results = random.choices(symbols, k=3 )
        print(results[0] + "|" + results[1] + "|" + results[2])
        if results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] =='7️⃣':
            print('You have won!')
            break
        else:
            results = random.choices(symbols, k=3 )
    
    answer = ''
    while answer.upper() != 'N':
        answer = input('Keep playing? (Y/N) ')
        if answer.upper() == 'Y':
            Play()
        elif answer.upper() == 'N':
            print('Thanks for playing!')
            break


        
Play()