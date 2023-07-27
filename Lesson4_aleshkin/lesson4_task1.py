"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""

from sys import argv

script_name, workhours, pph, profit = argv
#Options: 8 200 100

def sallary():
    #workhours = int(input('Выработка в часах: '))
    #pph = int(input('Ставка в час: '))
    #profit = int(input('Премия: '))
    result = int(workhours) * int(pph) + int(profit)
    print(result)

sallary()