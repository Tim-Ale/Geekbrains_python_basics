"""
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
p = int(input('Введите значение выручки: '))
t = int(input('Введите значение издержек: '))
if t >= p:
    print('Убыток.')
else:
    print('Прибыль.')
    print(f'Соотношение прибыли к выручке: {(p-t)*100/p}%')
    h = int(input('Введите численность сотрудников: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника: {(p-t)/h}')