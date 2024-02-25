Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> n = int(input("Введите число: "))
Введите число: 8
>>> if n % 2 == 0 and n > 0:
... print("Число является четным и положительным")
  File "<stdin>", line 2
    print("Число является четным и положительным")
    ^
IndentationError: expected an indented block after 'if' statement on line 1
>>> else:
  File "<stdin>", line 1
    else:
    ^^^^
SyntaxError: invalid syntax
>>> print("Число не является четным и положительным")
Число не является четным и положительным
>>>
