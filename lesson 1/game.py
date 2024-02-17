import random
def game():
    a = input("Введите свой ник: ")
    print("Привет, " + a + "!")
    print("Правила игры:")
    print("Компьютер загадывает 4-х значное число.")
    print("Тебе нужно угадать одну из цифр от 1 до 9.")
    print("У тебя 3 жизни. После каждой ошибки ты теряешь одну из них.")
    print("Если ты угадаешь число, то ты получешь 10 очков!")
    print("Также ты можешь выйти их игры с помощью клавиши E.")

    rec = 0

    while True:
        num = str(random.randint(1000, 9999))
        live = 3
        point = 0
        print("Угадай одну из цифр")

        while live > 0:
            b = input("Введите цифру от 0 до 9: ")

            if b == "E":
                print("Выход из игры...")
                break

            if b in num:
                print("Верно: + 10 очков!")
                point += 10
            else:
                print("Не верно: -1 жизнь")
                live -= 1
                print("У тебя осталось", live, "жизней.")

            if point > rec:
                rec = point

        if live == 0:
            print("Игра окончена! Ты набрал", point, "очков!")

        play_again = input("Хотите сыграть ещё раз? (YES or NO): ")
        if play_again.lower() != "YES":
            print("Твой рекорд", rec, "очков!")
        else: break

game()
