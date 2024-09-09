import random
from wods_hangman import word_list
from hangman_steps import hangman_steps
word_to_guess = random.choice (word_list)
word_to_guess_squares = ["_"] * len (word_to_guess)
wrong_guesses = 0
max_wrong_guesses = 4  # Максимальное количество попыток


# Цикл игры
while wrong_guesses < max_wrong_guesses and "_" in word_to_guess_squares:
    print (hangman_steps[wrong_guesses])  # Показать текущее состояние виселицы
    print (" ".join (word_to_guess_squares))  # Показать текущее состояние слова

    user_letter = input ("Guess a letter: ").lower ()

    if user_letter in word_to_guess:
        for index, letter in enumerate (word_to_guess):
            if letter == user_letter:
                word_to_guess_squares[index] = user_letter  # Открываем угаданную букву
    else:
        wrong_guesses += 1  # Увеличиваем количество ошибок
    if user_letter in word_to_guess_squares:
        print("You already guessed this letter")
    if user_letter not in word_to_guess:
        print(f"No {user_letter} in the word")
    print(f"You have {max_wrong_guesses - wrong_guesses} attempts left")
# Итог игры
if "_" not in word_to_guess_squares:
    print ("Congratulations! You guessed the word:", word_to_guess)
else:
    print (hangman_steps[wrong_guesses])  # Показать полную виселицу
    print ("You lost! The word was:", word_to_guess)
