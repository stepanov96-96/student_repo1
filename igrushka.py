import random


def check_guess(answer, guess):
    for digit in guess:
        if digit in answer:
            return True
    return False

def main():
    best_score = 0

    nickname = input("Привет! Как тебя зовут? ")
    print(f"Привет, {nickname}! Давай начнем игру.")

    while True:
        score = 0
        lives = 3

        while lives > 0:
            pc_answer = ''.join(random.sample('0123456789', 4))
            user_guess = input("Введите число от 0 до 9: ")

            if user_guess.upper() == 'E':
                break

            if check_guess(pc_answer, user_guess):
                print("Правильно! +10 очков")
                score += 10
            else:
                lives -= 1
                print(f"Неправильно! Осталось жизней: {lives}")

        if score > best_score:
            best_score = score
            print(f"Твой рекорд: {best_score}")

        decision = input("Твой результат: {} очков. Хочешь сыграть еще раз? (Y/N) ".format(score))
        if decision.upper() != 'Y':
            print(f"Спасибо за игру, {nickname}! Твой лучший результат: {best_score} очков.")
            break

if __name__ == "__main__":
    main()