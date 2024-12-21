my_dict = {'Anastasia': 1984, 'Philipp': 1974, 'Erik': 2021}
print(my_dict)
print(my_dict['Anastasia'])
print(my_dict.get('Ivan'))
print(my_dict.get('Ivan', 'В словаре нет'))
my_dict.update({'Alex': 1980, 'Peter': 1981})
print(my_dict)
my_dict.pop('Philipp')
print(my_dict)
p = my_dict.pop
print(p)
print(my_dict)

my_set = {18, 24, 1903, 'Peace', True, 'Flag', 18}
print(my_set)
my_set.add(False)
print(my_set)
my_set.remove(18)
print(my_set)
