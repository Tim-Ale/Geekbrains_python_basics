"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
lst = input("Заполните список элементов через пробел: ").split()
lst_new = lst
for el in range(0, len(lst)-1, 2):
    lst_new[el], lst_new[el+1] = lst[el+1], lst[el]
print(lst_new)