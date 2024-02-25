import random

def play_game():
    record = 0
    print("Добро пожаловать в игру!")
    nickname = input("Пожалуйста, введите ваш никнейм: ")
    print("Правила игры:")
    print("ПК задает 4-значное число. Вам нужно угадать хотя бы одну цифру.")
    print("За каждое угаданное число вы получаете 10 очков, за ошибку жизнь отнимается.")
    
    play_again = "да"
    while play_again.lower() == "да":
        score = 0
        lives = 3
        pc_number = str(random.randint(1000, 9999))
        
        print("Новый раунд! Угадайте число:")
        print(pc_number)
        
        user_guess = input("Введите ваш вариант числа (0-9) или нажмите E для выхода: ")
        
        if user_guess == 'E':
            print(f"Игра окончена. Ваш рекорд: {record} очков.")
            break
        
        for digit in user_guess:
            if digit in pc_number:
                score += 10
                print("Правильно! +10 очков.")
                break
            else:
                lives -= 1
                
        if lives == 0:
            print(f"Вы проиграли. Ваш счет: {score} очков.")
            if score > record:
                record = score
            
            play_again = input("Хотите сыграть еще раз? (да/нет): ")

    print(f"Спасибо за игру, {nickname}! Ваш рекорд: {record} очков.")

if __name__ == "__main__":
    play_game()
