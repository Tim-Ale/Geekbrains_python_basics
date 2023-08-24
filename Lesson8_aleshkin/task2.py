"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivideZero(Exception):
    pass


try:
    delimoe = int(input("Введите делимое: "))
    delitel = int(input("Введите делитель: "))

    if delitel == 0:
        raise DivideZero("Деление на ноль недопустимо")

    my_result = delimoe / delitel
    print(f'Результат: {my_result}')

except ValueError:
    print("Не верные данные. Не число.")

except DivideZero as err:
    print("Ошибка:", err)
