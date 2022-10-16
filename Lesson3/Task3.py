"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(first, second, last):
    items = [first, second, last]
    items.remove(min(items))

    return sum(items)


a, b, c = int(input("Введите число a >>> ")),\
          int(input("Введите число b >>> ")),\
          int(input("Введите число c >>> "))

print(f'Результат суммы двух наибольших введенных значений {my_func(a, b, c)}')
