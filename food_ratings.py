print('Hey there! \n')
print('Welcome to your must trustable trust ratings program!')
print('Please give your level of satisfaction (1-5 stars)')
print('How was you food?')

for i in range(5,0,-1):
    print(f'{i} Stars ')

stars = float(input())

if stars > 4.5:
    print('Extraordinary')
elif stars > 4:
    print('Excellent')
elif stars > 3:
    print('Good')
elif stars > 2:
    print('Fair')
else:
    print('Poor')

