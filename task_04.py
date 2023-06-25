# def generator(start, end):
#     current = start
#     while current <= end:
#         yield current
#         current +=1
# start = int(input('podaj poczatek przedziału: '))
# koniec = int(input('podaj koniec przedzialu: '))

# moj_generator = generator(start, koniec)
# for liczba in moj_generator:
#     print(liczba)

#Za pomocą generatora, stwórz instrukcję, która będzie zwracać kolejne liczby z przedziału podanego przez użytkownika.
custom_range = [2,3,4,5,1,66,7]

def get_range(input_range):
    ind = 0
    print(ind)
    while ind < len(input_range):
        yield input_range[ind]
        ind = ind+1
count = get_range(custom_range)
print(next(count))
print(next(count))

list(range(0,10,2)) # co druga liczba z przedzialu
list(range(0,10)) # kazda liczba z przedzialu