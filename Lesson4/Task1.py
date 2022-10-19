"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

file_name, hours, salary, bonus = argv
try:
    hours = int(hours)
    salary = int(salary)
    bonus = int(bonus)
    payment = hours * salary + bonus
    print(f'заработная плата сотрудника  {payment}')
except ValueError:
    print('Not a number')


# Тут пришло осознание, что необходимо выдать полный путь до файла. В моём случае это
# E:\Python\pythonProject\HW4\Task1.py и после уже остальные три аргумента hours, salary, bonus

"""
def pay():
    try:
        hours = float(input('Выработка в часах >>> '))
        salary = int(input('Ставка в убитых енотах >>> '))
        bonus = int(input('Премия в убитых енотах >>> '))
        payment = hours * salary + bonus
        print(f'заработная плата сотрудника составляет {payment} убитых енотов.')
    except ValueError:
        return print('Введено не корректное значение')
pay()
"""