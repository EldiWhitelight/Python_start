# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто
# и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Production(ABC):
  @abstractmethod
  def consumption(self):
    pass


class Coat(Production):
     def __init__(self, size):
         self.size = size

     @property
     def consumption(self):
         return (self.size / 6.5 + 0.5)


class Suite(Production):
     def __init__(self, height):
         self.height = height

     @property
     def consumption(self):
         return (2 * self.height + 0.3)

# Проверяем
V = Coat(44)
H = Suite(1.60)
total_consumption = V.consumption + H.consumption
print(f'Расход ткани для пальто {V.size} размера и костюма на рост {H.height} составляет {total_consumption} м')