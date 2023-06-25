# tabela_pacjetow = [[
# 'name', 'age',' gender', 'temperature','is_sick', 'blood', 'height'],
# ['jan', 33, 'M', '33,6', 'false', '0', 175],
# ['tom', 35, 'M', '39', 'true', 'a', 179],
# ['ana', 21, 'k', '36,7', 'true', 'a', 165],
# ['ina', 29, 'k', '36,6', 'false', 'b', 172],
# ['kris', 24, 'M', '37,1', 'true', 'ab', 182]
# ]

# pacjeci = []

# naglowek = tabela_pacjetow[0] #pobieranie nazw kolumn z pierwszego wiersza

# for wiersz in tabela_pacjetow[1:]: #przetwarzanie pozostalych wierszy tabeli od pierwszej do "entej"
#     slownik_pacjenta = dict(zip(naglowek, wiersz)) #funckja zip tworzy zestawienie dwóch list w tym przypadku nagłowej i wiersz
#     pacjeci.append(slownik_pacjenta) # dodanie slownika do listy pacjetow

# for pacjent in pacjeci:
#     print(pacjent)

#***********
# Dana jest tabela pacjentów. Zapisz informację o każdym z pacjentów w formie słownika. Dane wprowadź w kolejności, w jakiej pojawiają się w tabeli.
Jan = {'name': 'Jan', 'age': 33, 'gender': 'M', 'temp': 36.6, 'is_sick': False, 'blood': '0', 'height': 175}
Tom = {'name': 'Tom', 'age': 35, 'gender': 'M', 'temp': 39, 'is_sick': True, 'blood': 'A', 'height': 179}
Ana = {'name': 'Ana','age': 21, 'gender': 'K', 'temp': 36.7, 'is_sick': True, 'blood': 'A', 'height': 165}
Ina = {'name': 'Ina','age': 29, 'gender': 'K', 'temp': 36.6, 'is_sick': False, 'blood': 'B', 'height': 172}
Kris = {'name': 'Kris','age': 24, 'gender': 'M', 'temp': 37.1, 'is_sick': True, 'blood': 'AB', 'height': 182}

dict_out = {'Jan': Jan, 'Tom': Tom, 'Ana': Ana, 'Ina': Ina, 'Kris': Kris}
dict_out.keys()
print(dict_out)

