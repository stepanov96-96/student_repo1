# Запрашиваем у пользователя два числа
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Выполняем арифметические операции
sum_result = num1 + num2
subtraction_result = num1 - num2
multiplication_result = num1 * num2
division_result = num1 / num2
remainder_result = num1 % num2

# Выводим результат каждой операции
print("Сумма:", sum_result)
print("Разность:", subtraction_result)
print("Произведение:", multiplication_result)
print("Деление:", division_result)
print("Остаток от деления:", remainder_result)