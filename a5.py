num = int(input("Введите число: "))

peremennayasssss = (num % 2 == 0) and (num > 0)

result = bool(peremennayasssss)

if result:
    print("Результат: {result}, {num} - четное и положительное число")
else:
    print("Результат: {result}, {num} не является четным и положительным числом")