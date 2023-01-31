# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

with open('salary_text.txt', 'r', encoding='utf-8') as txt:

    salary_of_employee = {line.split()[0].strip(): float(line.split()[1]) for line in txt.readlines()}

start_salary = 0
for surname, salary in salary_of_employee.items():
    start_salary += salary
    if salary < 20000:
        print(surname)
average_salary = start_salary / len(salary_of_employee)
print(f'Средняя величина дохода равна {average_salary}')