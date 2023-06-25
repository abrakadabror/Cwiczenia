#Stwórz obiekt klasy Square, o atrybucie side, area,circumference i metodach, get_area(), get_circ(), 
#odpowiednio obliczające pole i obwód kwadratu
class Square:
    def __init__(self, side_length):
        self.side_length = side_length
    def get_area(self):
        return self.side_length ** 2 #oblicza pole prosstokąta
    def get_circ(self):
        return self.side_length *4 
square1 = Square(int(input('Podaj liczbę: ')))
print('Pole wynosi: ',square1.get_area())

square2 = Square(4)  #oblicza pole kwadratu
print('Pole wynosi: ',square2.get_area())

circumference = Square(int(input('Podaj liczbę: '))) #obliczamy obdów kwadratu
print('Obwód wynosi: ', circumference.get_circ())