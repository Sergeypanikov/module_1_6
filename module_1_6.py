my_dict = {'Anton': 1985, 'Nikita': 1943, 'Vova': 1870}
print(my_dict)
print(my_dict['Nikita'])
my_dict['Olga'] = 1990
print(my_dict)
my_dict.update({'Nina': 2020, 'Gleb': 2022})
print(my_dict)
my_dict.pop('Nina')
print(my_dict)
# Увы, не могу понять как вывести значение ключа Нина
# 3 пункт домашнего задания
my_set = {1, '3 яблока', 4.12, 5, 6, 4, 2, 1, 8, 4, (1, 3, 2.12)}
print(my_set)
list_ = [1, 2, 3, 4, 4, 3, 2, 1]
list_ = set(list_)
print(list_)
print(list_.add(5))
print(list_.add(7))
print(list_)
print(list_.remove(1))
print(list_)