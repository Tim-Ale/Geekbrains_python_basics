"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

with open('sallary.txt', 'r', encoding='utf-8') as my_obj:
    #totalsal = 0
    #count = 0
    totalsal = []
    lowsal = []
    my_list = my_obj.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
           lowsal.append(i[0])
        #totalsal += float(i[1])
        #count += 1
        totalsal.append(i[1])
print(f'Оклад менее 20 тыс.: {lowsal}'
      f', средняя величина дохода сотрудников: {sum(map(float, totalsal)) / len(totalsal)}')