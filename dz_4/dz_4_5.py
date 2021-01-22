# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

import random
from functools import reduce


arr = [i for i in range(100, 1001, 2)]
print(arr)

composition = reduce(lambda a, b: a * b, arr)
print(composition)
