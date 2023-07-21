"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.

Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.

Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.

Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

Набор натуральных чисел можно задать непосредственно в коде,
например, my_list = [7, 5, 3, 3, 2].
"""
"""
my_list = []

for _ in range(5):
    number = int(input("Введите число: "))
    c = my_list.count(number)
    if len(my_list) == 0:
        my_list.append(number)
    else:
        for element in my_list:
            if c > 0:
                i = my_list.index(number)
                my_list.insert(i+c, number)
                break
            else:
                if number > element:
                    j = my_list.index(element)
                    my_list.insert(j, number)
                    break
                elif number < my_list[len(my_list) - 1]:
                    my_list.append(number)

print(my_list)
"""

rating = [7, 5, 3, 3, 2]
print(f'Рейтинг: {rating}')
while True:
    new_element = int(input("Введите новый элемент рейтинга (Сtrl+F2 для выхода): "))
    position = len(rating)
    for i in range(len(rating)):
        if new_element >= rating[i]:
            position = i
            break
    rating.insert(position, new_element)
    print("Результат: ", rating)
