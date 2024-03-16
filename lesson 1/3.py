import math

r = int(input('Ведите радиус круга, что бы узнать его площадь: '))
s = math.pi * math.pow(r, 2)
print('Площадь круга с радиусом ' + str(r) + ' равна', round(s))
