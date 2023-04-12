import random
from word_list import words
from hag_art import man
from hangman_art import logo
from game_rules import rules

end_game = False


def start_the_game():
    print(rules)
    print(logo)
    word = random.choice(words)

    word_letters = list(word)

    guessed_letters = []
    tries = 6

    while tries > 0:
        print(man[6 - tries])

        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
                print("Буква угаданна!")
            else:
                display_word += "_"
        print("Угадайте слово: ", display_word)
        print("Попытки: ", tries)

        guess = input("Ваша буква: ")
        guessed_letters.append(guess)

        if guess not in word_letters:
            print("Не угадал!")
            tries -= 1

        if all(letter in guessed_letters for letter in word_letters):
            print("Поздравляю! Вы угадали слово:", word)
            break

    if tries == 0:
        print(man[6])
        print("Вы использовали все попытки! Загаданное слово было:", word)


while not end_game:
    greeting = input('Поиграем? (да / нет): ')
    if greeting.lower() == 'да':
        print('Отлично! Давай начнем игру!')
        start_the_game()
        end_game = True
    elif greeting.lower() == 'нет':
        print('Жаль, может в другой раз!')
        break
    else:
        print('Неправильный ввод. Пожалуйста, введите "да" или "нет".')
