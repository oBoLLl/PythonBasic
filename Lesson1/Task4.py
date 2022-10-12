"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while, арифметические операции.
"""

print("В введенном далее числе будет найдена максимальная цифра")
user_input = input("Введите положительное число >>> ")

if not user_input.isdigit():
    print("Введено не верное число")
    exit()

num = int(user_input)
max_num = 0

while num and max_num != 9:
    temp = num % 10
    num = num // 10
    max_num = temp if temp > max_num else max_num

print("Наибольшая цифра в введенном числе:", max_num)

