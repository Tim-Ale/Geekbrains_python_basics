"""
Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
n = int(input("Введите число N (от 1 до 9): "))
if n <= 0 or n >= 10:
    print("Не верное значение N")
else:
    a = n
    b = str(n) + str(n)
    b = int(b)
    c = str(n) + str(n) + str(n)
    c = int(c)
    print(f'Сумма N+NN+NNN: {a+b+c}')
    """Или так:"""
    #print(f'Сумма N+NN+NNN: {n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))}')
