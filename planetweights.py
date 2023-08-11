print('Welcome to planet weights!')
weightE = float(input('Please tell me your weight in earth: '))

print('This are the planets and its numbers: ')
print('1. Mercury')
print('2. Venus')
print('3. Marte')
print('4. Jupiter')
print('5. Saturn')
print('6. Uranus')
print('7. Neptune')
planet = float(input('Pleaste tell me the number of the planet: '))




if planet == 1:
    print(f'Your weight in the planet Mercury is: {weightE * 0.38}')
elif planet == 2:
    print(f'Your weight in the planet Venus is: {weightE * 0.91}')
elif planet == 3:
    print(f'Your weight in the planet Mars is: {weightE * 0.38}')
elif planet == 4:
    print(f'Your weight in the planet Jupiter is: {weightE * 2.53}')
elif planet == 5:
    print(f'Your weight in the planet Saturn is: {weightE * 1.07}')
elif planet == 6:
    print(f'Your weight in the planet Uranus is: {weightE * 0.89}')
elif planet == 7:
    print(f'Your weight in the planet Neptune is: {weightE * 1.14}')
else:
    print('Please check yous answers.')
    
    
