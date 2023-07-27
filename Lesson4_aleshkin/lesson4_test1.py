#ВКЛЮЧЕНИЯ!
#традиицционный итератор с ф-цией append/ заполняем массив
lst = []
for el in range(10):
    lst.append(el)
print(lst)

#только четные
lst = []
for el in range(10):
    if el % 2 == 0:
        lst.append(el)
print(lst)

#списковое включение (LC - list comprehension)
lst = [el for el in range(10)]
print(lst)

#LC включая только четные
lst = [el for el in range(10) if el % 2 == 0]
print(lst)

#множество
set_obj = set()
for el in range(10):
    set_obj.add(el)
print(set_obj)

#множество LC
set_obj = {el for el in range(10)}
print(set_obj)

#словари
dct = {}
for el in range(10):
    dct[el] = el**2
print(dct)

#словари LC
dct = {el: el**2 for el in range(10)}

#не кортеж/генератор
obj = (el for el in range(10))
print(obj)


#pizza
lst = [1, 2, 3]
for el in lst:
    print(el)

#pizza в холодильнике
lst = [el for el in range(3)]
for el in lst:
    print(el)

#pizza инструкция по созданию
#/вычисление по запросу (ленивое) - не занимает память
obj = (el for el in range(3))
for el in lst:
    print(el)
#^^генератор для экономии памяти^^

#
def func():
    lst = [el for el in range(10)]
    return lst

res = func()
for el in res:
    print(el)

#генератор
def func():
    for el in range(10):
        yield el

res = func()
for el in res:
    print(el)


#модуль math - встроенный. математика

#модуль itertools
#count - больше/ значения от ...
from itertools import count
for el in count(7):
    if el > 15:
        break
    else:
        print(el)

#functools
#reduce - применяет ко всем элементам массива, сводит к одному значению

from functools import reduce

def my_func(prev_el, el):
    # >>!<<
    print(f'{prev_el}, {el}')
    return prev_el + el

print(reduce(my_func, (10, 20, 30, 40)))
