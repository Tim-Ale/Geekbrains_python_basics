"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.

"""

# Удалить данные из файла "out_file.txt", если он уже создан
with open("out_file.txt", 'w') as myfile:
    myfile.write('')

with open("out_file.txt", 'a') as myfile:
# Режим 'a' добавляет строки в файл "out_file.txt".
    while True:
        new_line = input("Введите строку (пустая строка для окончания ввода): ")
        if new_line == '':
            break
        myfile.write(new_line + '\n')

# Вывести данные файла "out_file.txt"
print(f'Запись данных в файл завершена. файл: ')
with open("out_file.txt", 'r', encoding='utf-8') as f_obj:
    for el_line in f_obj:
        print(el_line)
