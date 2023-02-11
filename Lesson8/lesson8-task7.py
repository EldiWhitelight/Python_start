# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        if self.im < 0:
            return f"({self.re}{self.im}i)"
        else:
            return f"({self.re}+{self.im}i)"

    def __add__(self, other):
        return ComplexNumber(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return ComplexNumber(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)


# проверяем в сравнении со встроенным типом complex
a = complex(4, 6)
a_1 = ComplexNumber(4, 6)
b = complex(7, -9)
b_1 = ComplexNumber(7, -9)

c = a + b
c_1 = a_1 + b_1

d = a * b
d_1 = a_1 * b_1

print(f"{a} + {b} = {c}")
print(f"{a_1} + {b_1} = {c_1}")
print(f"{a} * {b} = {d}")
print(f"{a_1} * {b_1} = {d_1}")