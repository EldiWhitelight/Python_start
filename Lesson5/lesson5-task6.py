# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие
# лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий. Необязательно,
# чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
import json
with open('lesson5-task6.txt', 'r', encoding='utf-8') as txt:
    dict = {line.strip().split(':')[0]: line.strip().split(':')[1].split() for line in txt}


def num_from_string(string):
# Ищем числа в строках
    result = ''
    for i in string:
        if i.isdigit():
            result += i
        else:
            break
    if result != '':
        return int(result)
    else:
        return 0


for subject, content in dict.items():
    cur_subject = 0  # дефолтное кличество занятий для выбранного предмета
    for i in content:
        cur_subject += num_from_string(i)
    dict[subject] = cur_subject

print(json.dumps(dict, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': ')))
