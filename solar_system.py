from math import pi
from random import choice as ch
from math import pow

planets = [
  'Mercury',
  'Venus',
]

random_planet = ch(planets)

if random_planet ==  'Mercury':
    area = 4 * pi * pow(2440,2)
    print(f"Mercury's area is: {area}")
elif random_planet == 'Venus':
    area2 = 4* pi * pow(6052,2)
    print(f"Venus's area is: {area2}")

