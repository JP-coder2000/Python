print("Welcome!")
print('Im the sorting hat, Im the one who is going to put you in your respective house')
print('Please write the number of the answer you would like to choose')

Gryffindor = 0
Slytherin = 0
Ravenclaw = 0
Hufflepuff = 0

print('Q1) Do you like Dawn or Dusk')
print('1) Dawn')
print('2) Dusk')
q1 = int(input())

if q1 == 1:
    Gryffindor += 1 
    Ravenclaw += 1
elif q1 == 2:
    Slytherin += 1
    Hufflepuff += 1
else:
    print('Wrong input')

print('Q2) When I’m dead, I want people to remember me as:')
print('1) The Good')
print('2) The Great')
print('3) The Wise')
print('4) The Bold')
q2 = int(input())

if q2 == 1:
    Hufflepuff += 2
elif q2 == 2:
    Slytherin += 2
elif q2 == 3:
    Ravenclaw += 2
elif q2 == 4:
    Gryffindor += 2
else:
    print('Wrong input')

print('Q3) Which kind of instrument most pleases your ear?')
print('1) The violin')
print('2) The trumpet')
print('3) The piano')
print('4) The drum')
q3 = int(input())

if q3 == 1:
    Slytherin += 4
elif q3 == 2:
    Hufflepuff += 4
elif q3 == 3:
    Ravenclaw += 4
elif q3 == 4:
    Gryffindor += 4
else:
    print('Wrong input')

if Gryffindor > Slytherin and Gryffindor > Hufflepuff and Gryffindor > Ravenclaw:
    print('Welcome to house Gryffindor!')
elif Slytherin > Gryffindor and Slytherin > Hufflepuff and Slytherin > Ravenclaw:
    print('Welcome to house Slytherin!')
elif Hufflepuff > Slytherin and Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw:
    print('Welcome to Hufflepuff')
else:
    print('Welcome to Ravenclaw!')

