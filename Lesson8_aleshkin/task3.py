"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.
Класс-исключение должен контролировать типы данных элементов списка.
"""
"""
Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
"""


class OnlyNumbers(Exception):
    pass

numbers = []
while True:
    try:
        num = input("Введите число (или 'exit' для завершения): ")
        if num == 'exit':
            break
        if not num.isdigit():
            raise OnlyNumbers("Введите только числа")
        numbers.append(int(num))
    except OnlyNumbers as err:
        print(err)

print("Список чисел:", numbers)