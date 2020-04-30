n=int(input('Введите число n: '))
print('Введите список из',n,'чисел')
spisok = list(map(int,input().split()))
# при выводе списка была ошибка invalid literal for int() with base 10.  Погуглив узнал,что
 # нужен split , который работает как разделитель и map, который превращает в int, чтобы все заработало
spisok=sorted(spisok)
print(spisok) # можно и сразу вывести 2 числа, но решил сделать выводы поэтапно
print(spisok[-2],spisok[-1], 'наибольшие элементы списка')
