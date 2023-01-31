# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти чётные
# числа от 100 до 1000 (включая границы). Нужно получить результат вычисления произведения всех элементов списка.

from functools import reduce
from operator import mul
from random import randrange

num = int(input('Укажите количество элементов списка: '))

my_list = [randrange(100, 1001, 2) for i in range(num)]


product_of_num = reduce(mul, my_list)


print(my_list)
print(product_of_num)