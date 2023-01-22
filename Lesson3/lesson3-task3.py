# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.


def my_func(a, b, c):
    args_list = [a, b, c]
    args_sum = max(args_list)
# Находим и удаляем самый больщой аргумент
    args_list.remove(args_sum)
# Оставляем второй наибольший аргумент
    args_sum += max(args_list)
    return args_sum


one = int(input('Введите первый аргумент: '))
two = int(input('Введите второй аргумент: '))
three = int(input('Введите третий аргумент: '))
print(my_func(one, two, three))