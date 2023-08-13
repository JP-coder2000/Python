import random

print('=============================================')
print('Hey there!')
print('Welcome to the game of rock-paper-scissors')
print('=============================================')

print('Please write down the number of the choice you want to take!')
print('1 is for ROCK')
print('2 is for PAPER')
print('3 is for SCISSORS')

player = int(input('Pick a nuber: '))

if player == 1:
    print('You choose ROCK!')
elif player == 2:
    print('You choose PAPER!')
elif player == 3:
    print('You choose SCISSORS!')
else:
    print('Please pick a valid answer!')
    exit()


machine = random.randint(1,3)

if machine == 1:
    print('The machine choose ROCK!')
elif machine == 2:
    print('The machine choose PAPER!')
elif machine == 3:
    print('The machine choose SCISSORS!')
else:
    print('Please pick a valid answer!')
    exit()

if player == 1 and machine == 3:
    print('You win!')
elif player == 2 and machine == 1:
    print('You win!')
elif player == 3 and machine == 2:
    print('You win!')
elif player == machine:
    print('Its a tie!')
else:
    print('The machine won!')

