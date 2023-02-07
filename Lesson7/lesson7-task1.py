# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, list_of_lists):
        self.matrix = list_of_lists

    def __str__(self):
        max_len = 1
        copy_of_matrix = self.matrix.copy()  # Создаем копию матрицы
        for i in range(len(copy_of_matrix)):
            copy_of_matrix[i] = list(map(str, copy_of_matrix[i]))  # Приводим числа в матрице к строке
            # Если текущее число длиннее предыдущих в значение наибольшей длины, то присваеваем ему новое
            max_len = len(max(copy_of_matrix[i], key=len)) if max_len < len(max(copy_of_matrix[i], key=len)) \
                else max_len

        # Строка для вывода
        string = ''
        for i in range(len(copy_of_matrix)):
            for j in range(len(copy_of_matrix[i])):
                copy_of_matrix[i][j] = copy_of_matrix[i][j].ljust(max_len)
            string += ' '.join(copy_of_matrix[i])
            # Если строка не последняя, переносим строку
            string += '\n' if i != len(copy_of_matrix) - 1 else ''
        return string

    def __add__(self, other):
        result = []  # Список для результата
        for i in range(len(self.matrix)):
            result_row = []  # Список для строки строки матрицы
            for j in range(len(self.matrix[i])):
                result_el = self.matrix[i][j] + other.matrix[i][j]
                result_row.append(result_el)  # Добавляем в строку
            result.append(result_row)  # Добавляем в список
        return Matrix(result)


# Проверка
a = Matrix([[6, 17, 27], [3765, 4, 345], [76, 66, 7890]])
b = Matrix([[78, 55, 77], [8976, 3, 778], [66, 55, 8765]])

print(a)
print()
print(a)
print()
print(a + b)