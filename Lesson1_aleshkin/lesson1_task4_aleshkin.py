"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""


n = int(input("Введите целое положительоне число: "))
if n <= 0:
    print("Не верное значение")
else:
    b = -1
    while n > 10:
        m = n % 10
        n //= 10
        if m > b:
            b = m
    print(f'Самая большая цифра в числе: {b}')
