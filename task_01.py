# Stwórz funkcję pitagoras, która oblicza długość przeciwprostokątnej dowolnego trójkąta prostopadłego 
#z użyciem twierdzenia pitagorasa
import math
def pitagoras(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

# Przykładowe wywołanie funkcji def pitagoras
try:
    a = int(input('Podaj długość pierwszego boku: '))
    b = int(input('Podaj długosc drugiego boku: '))
    c = pitagoras(a, b)
    print('Długość trzeciego boku: ', c)

except ValueError:
    print('nieprawidłowa wartosc')
