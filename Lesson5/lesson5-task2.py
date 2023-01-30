# 2. Создать текстовый файл (не программно),
# сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

with open('my_new_text.txt', 'r', encoding='utf-8') as txt:
    cur_line = 0
    for line in txt:
        cur_line += 1
        num_of_words = len(line.split())
        print(f'В строке {cur_line} - {num_of_words} слов')
    print(f'Всего в файле {cur_line} строк')