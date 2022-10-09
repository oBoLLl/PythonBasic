"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3, cчитаем 3 + 33 + 333 = 369.
"""

user_input = input("Введите число >>>")

if not user_input.isdigit():
    print("Введено не верное число")
    exit()

n = (user_input)
nn = (user_input + user_input)
nnn = (user_input + user_input + user_input)

first = int(n)
second = int (nn)
third = int (nnn)

sum = int(first + second + third)
print("Программа считает по формуле n + nn + nnn, где n - введенное число")
print(sum)
