# Запрашиваем у пользователя два числа в виде строк
num1_str = input("Введите первое число: ")
num2_str = input("Введите второе число: ")

# Преобразуем введенные строки в числа
num1 = float(num1_str)
num2 = float(num2_str)

# Вычисляем сумму введенных чисел
sum_result = num1 + num2

# Выводим результат
print("Сумма чисел", num1, "и", num2, "равна", sum_result)