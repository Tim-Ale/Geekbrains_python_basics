"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('num_file.txt', 'w+') as file_obj:
    my_line = input('Введите цифры через пробел: ')
    file_obj.writelines(my_line)
    my_num = my_line.split()

print(sum(map(int, my_num)))