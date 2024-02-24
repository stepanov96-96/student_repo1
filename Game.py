import random

def play_game():
    name = input("Введите свой никнейм: ")
    print("Привет, {}. Правила игры очень просты. ПК задает 4-х значное число, а вы пытаетесь его угадать.".format(name))
    print("Загаданное число содержит цифры от 0 до 9.")
    print("Вы можете выйти из игры в любой момент, нажав клавишу E.")

    score = 0
    lives = 3
    record = 0

    while lives > 0:
        pc_number = str(random.randint(1000, 9999))
        user_input = input("Введите число: ")

        if user_input.lower() == "e":
            break
        elif len(user_input) != 4 or not user_input.isdigit():
            print("Пожалуйста, введите 4-х значное число.")
            continue

        for digit in user_input:
            if digit in pc_number:
                score += 10
                print("Вы угадали цифру! +10 очков")
                break
        else:
            lives -= 1
            print("К сожалению, вы не угадали. У вас осталось {} жизней.".format(lives))

        if score > record:
            record = score

    print("Игра окончена. Ваш счет: {}. Ваш рекорд: {}".format(score, record))
    play_again = input("Хотите ли вы повторить игру? (да/нет): ")
    if play_again.lower() == "да":
        play_game()
    else:
        print("Спасибо за игру, до свидания!")

play_game()