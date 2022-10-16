"""
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def main(first_name: str = None,
         last_name: str = None,
         year: int = None,
         city: str = None,
         email: str = None,
         phone: str = None):
    return f"{first_name} {last_name} ({year}), {city}, {email}, {phone}"


user_first_name = input(" Введите Имя >>> ")
user_last_name = input(" Введите Фамилию >>> ")
user_year = int(input(" Введите год рождения >>> "))
user_city = input(" Введите город >>> ")
user_email = input(" Введите Email >>> ")
user_phone = input(" Введите номер телефона >>> ")

print(
    main(first_name=user_first_name, last_name=user_last_name,
         year=user_year, city=user_city, email=user_email,
         phone=user_phone)
)
