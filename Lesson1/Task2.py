"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды, выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

user_time = input("Введите положительное целое число >>>")

if not user_time.isdigit():
    print("Введено не верное число")
    exit()

user_input = int(user_time)

hours = user_input // 3600
minutes = (user_input % 3600) // 60
seconds = (user_input % 3600) % 60

print("Вы ввели", user_time, "секунд, это:")

print(f"{hours:>02}:{minutes:>02}:{seconds:>02}")
