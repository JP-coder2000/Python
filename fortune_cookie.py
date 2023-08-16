import random

def fortune():
    random_number = random.randint(1,9)
    if random_number == 1:
        print("Don't persue happiness - create it.")
    elif random_number == 2:
        print("All things are difficult before they are easy.")
    elif random_number == 3:
        print("The early bird gets the worm, but the second mouse gets the cheese.")
    elif random_number == 4:
        print("If you eat something and nobody sees you eat it, it has no calories.")
    elif random_number == 5:
        print("Someone in your life needs a letter from you.")
    elif random_number == 6:
        print("Don't just think. Act!")
    elif random_number == 7:
        print("Your heart will skip a beat.")
    elif random_number == 8:
        print("The fortune you search for is in another cookie.")
    elif random_number == 9:
        print("Help! I'm being held prisoner in a Chinese bakery!")
    else:
        exit()

fortune()

#Codedex answer without if's:
import random

options = [
  'Don’t pursue happiness – create it.',
  'All things are difficult before they are easy.',
  'The early bird gets the worm, but the second mouse gets the cheese.',
  'If you eat something and nobody sees you eat it, it has no calories.',
  'Someone in your life needs a letter from you.',
  'Don’t just think. Act!',
  'Your heart will skip a beat.',
  'The fortune you search for is in another cookie.',
  'Help! I’m being held prisoner in a Chinese bakery!'
]

def fortune():
  random_fortune = random.randint(0, len(options) - 1)
  print(options[random_fortune])
