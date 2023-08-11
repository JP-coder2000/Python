#first_side = int(input('Enter the first short side of the triangle: '))
#second_side = int(input('Enter the second short side of the triangle: '))
#hypotenuse = (first_side ** 2 + second_side ** 2) ** 0.5
#print('El valor de la hipotenusa es:', hypotenuse)

#first_side = int(input('Enter the first short side of the triangle: '))
#second_side = int(input('Enter the second short side of the triangle: '))
#hypotenuse = (first_side ** 2 + second_side ** 2) ** 0.5
#print(f'El valor de la hipotenusa es: {hypotenuse}')

a = int(input('Escribe el coeficiente de a: '))
b = int(input('Escribe el coeficiente de b: '))
c = int(input('Escribe el coeficiente de c: '))

xuno = (-b + ((b **2 -(4 * a * c)) ** 0.5 ))/ (2*a)
xdos = (-b - ((b **2 -(4 * a * c)) ** 0.5 ))/ (2*a)
print(xuno)
print(xdos)
