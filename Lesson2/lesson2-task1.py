# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
# каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

a = []
a.append(10)
a.append(10.13)
a.append('string')
a.append([10, 10.13, 'string'])
a.append((10, 10.13, 'string'))
a.append({2, 3, 3, 4, 4, 5, 6})
a.append({'integral': 10, 'float': 10.13, 'string': 'string'})
a.append(frozenset([2, 3, 3, 4, 4, 5, 6]))
a.append(complex(3, -3))
a.append(None)
a.append(False)
a.append(bytearray(b'some text'))

for i in a:
     print(i, type(i))


