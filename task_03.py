#Stwórz klasy Square, Rectangle, Circle, Triangle, Figure I ustal schemat dziedziczenia między nimi.

import math

class figure:
    pass
class square(figure): #kwadrat
    def __init__(self, bok):
        self.bok = bok
    def area(self):
        return self.bok ** 2
kwadrat = square(2)
print('wynik: ', kwadrat.area()) 
print('\n')

class rectangle(figure): #prostokąt
    def __init__(self, bok1, bok2):
        self.bok1 = bok1 
        self.bok2 = bok2
    def area(self):
        return self.bok1 * self.bok2
prostokat = rectangle(bok1 = 1 , bok2 = 2 )
print('wynik_01: ', prostokat.area())
print('\n')
class circle(figure):#koło
    def __init__(self, promien):
        self.promien = promien
    def obwod(self):
        return math.pi * self.promien ** 2
kolo =  circle(2)
print('wynik_02: ', kolo.obwod())
print('\n')

class triangle(figure): #trójkąt
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self): #obwód
        return self.a + self.b + self.c
trojkat = triangle(a = 1, b = 2, c = 3)
print('wynik_03 ', trojkat.perimeter())

