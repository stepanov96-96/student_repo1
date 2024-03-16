import random
import string

def generate_password(length, use_digits=False, use_symbols=False, use_uppercase=False):
    chars = string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    if use_uppercase:
        chars += string.ascii_uppercase
    return ''.join(random.choice(chars) for _ in range(length))

length = int(input("Введите длину пароля: "))
use_digits = input("Использовать цифры? (Y/N): ").lower() == 'Y'
use_symbols = input("Использовать символы? (Y/N): ").lower() == 'Y'
use_uppercase = input("Использовать заглавные буквы? (Y/N): ").lower() == 'Y'

password = generate_password( length, use_digits, use_symbols, use_uppercase)
print(f"Сгенерированный пароль: {password}")