"""
Поработайте с переменными, создайте несколько,
выведите на экран,
запросите у пользователя несколько чисел и строк, и сохраните в переменные,
выведите на экран.
"""

Text_variable = 'This is text varible in string'
Int_var1 = 10
Int_var2 = 100
Float_var = 15.3

user_name = input("Введите Ваше имя тут >>>")
user_2_name = input("Введите Ваше отчество тут >>>")

print(user_name, user_2_name, ", Добро пожаловать. "
                              "Ниже список некоторых переменных.")
print("Text_variable is set >>> " + Text_variable)
print(Int_var1, " <<< First Integer variable")
print(Int_var2, " <<< Second Integer variable")
print(Float_var, " <<< This is float variable")
