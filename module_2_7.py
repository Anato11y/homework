def print_params(a=1, b='строка', c=True):
    print( a, b,  c)
# 1.Вызов функции с разным количеством аргументов:
print('Вызов функции с разным количеством аргументов:')
print_params()
print_params(5, 'другая строка', False)
print_params(b=25)
print_params(c=[1, 2, 3])

# 2.Распаковка параметров:
print('Распаковка параметров:')
values_list = [10, 'example', False]
values_dict = {'a': 100, 'b': 'строка', 'c': [4, 5, 6]}
print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:'
print('Распаковка + отдельные параметры:')
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)