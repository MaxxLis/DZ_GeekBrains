# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def salary(labor_times, price_hour, prize):
    return labor_times * price_hour + prize


script_name, labor_times, price_hour, prize = argv

print('Зарплата сотрудника: ', salary(int(labor_times), int(price_hour), int(prize)))


# для вызова из терминала:  python dz_4_1.py 192 600 12000