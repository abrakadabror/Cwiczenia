# Wykorzystaj dane z poprzedniego zadania, do stworzenia funkcji zwracającej treść:
# „Hello”+ name +”! Your body temperature is ” +temperature+’. My scanners suggest you are ’<”Sick” if Is_sick==True; else “healthy”>

Jan = {'name': 'Jan', 'age': 33, 'gender': 'M', 'temp': 36.6, 'is_sick': False, 'blood': '0', 'height': 175}
Tom = {'name': 'Tom', 'age': 35, 'gender': 'M', 'temp': 39, 'is_sick': True, 'blood': 'A', 'height': 179}
Ana = {'name': 'Ana','age': 21, 'gender': 'K', 'temp': 36.7, 'is_sick': True, 'blood': 'A', 'height': 165}
Ina = {'name': 'Ina','age': 29, 'gender': 'K', 'temp': 36.6, 'is_sick': False, 'blood': 'B', 'height': 172}
Kris = {'name': 'Kris','age': 24, 'gender': 'M', 'temp': 37.1, 'is_sick': True, 'blood': 'AB', 'height': 182}

dict_out = {'Jan': Jan, 'Tom': Tom, 'Ana': Ana, 'Ina': Ina, 'Kris': Kris}
dict_out.keys()
print(dict_out)

def get_greeting(my_dict):
    name = my_dict['name']
    temp = my_dict['temp']
    if my_dict['is_sick']:
        return 'Hello' +str(name)+'! your body temperature is' + str(temp)+'my scanners suggests you are sick'
    else:
        return ' Hello' + str(name)+'!your body temperature is' + str(temp)+ 'my scanners suggest you are healthy'
for key in dict_out.keys():
    print(get_greeting(dict_out[key]))