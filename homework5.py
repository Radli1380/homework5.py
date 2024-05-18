my_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви']
print(my_list)
print("Первый элемент списка:", my_list[0])
print("Последний элемент списка:", my_list[-1])
print("Подсписок с третьего до пятого элементов:", my_list[2:5])
my_list[2] = 'грейпфрут'
print("Измененный список my_list:", my_list)
my_dict = {'apple': 'яблоко', 'banana': 'банан', 'orange': 'апельсин'}
print("Словарь my_dict:", my_dict)
key = 'apple'
print("Значение для ключа", key, ":", my_dict[key])
my_dict['apple'] = 'яблочко'
my_dict['grape'] = 'виноград'
print("Измененный словарь my_dict:", my_dict)
