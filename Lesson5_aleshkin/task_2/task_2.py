"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('input_file.txt', 'r', encoding='utf-8') as f_obj:
    count_lines = 0
    for el_line in f_obj:
        count_lines += 1
        words = el_line.split()
        print(f' Слов в строке {count_lines}: {len(words)}')
print(f' Всего строк: {count_lines}')