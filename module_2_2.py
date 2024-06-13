first=input('Введите число first: ')
second=input('Введите число second: ')
third=input('Введите число third: ')
if first==second and first==third:
    print('Количество одинаковых чисел:',3)
elif first==second or first==third or first==third:
    print('Количество одинаковых чисел:',2)
else:
    print('Количество одинаковых чисел:',0)