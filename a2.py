num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

print(f"Результат сложения: {num1 + num2}")
print(f"Результат вычитания: {num1 - num2}")
print(f"Результат умножения: {num1 * num2}")

if num2 != 0:
    print(f"Результат деления: {num1 / num2}")
    print(f"Остаток от деления: {num1 % num2}")
else:
    print("Деление на ноль невозможно")