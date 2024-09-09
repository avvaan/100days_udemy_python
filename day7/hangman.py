import random
hangman_steps = [
    """
    -----
    |   |
        |
        |
        |
        |
    --------
    """,
    """
    -----
    |   |
    O   |
        |
        |
        |
    --------
    """,
    """
    -----
    |   |
    O   |
    |   |
        |
        |
    --------
    """,
    """
    -----
    |   |
    O   |
   /|\\  |
        |
        |
    --------
    """,
    """
    -----
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    --------
    """
]
lives=6
word_list=["apple","orange","banana"]
word_to_guess=random.choice(word_list)
word_to_guess_squares=["_"]*len(word_to_guess)
# Основной цикл, который продолжается, пока слово не угадано
while "_" in word_to_guess_squares:
    print (" ".join (word_to_guess_squares))  # Показать текущее состояние слова
    user_letter = input ("Give me a letter: ").lower ()

    # Проверка каждой буквы в слове
    for index, letter in enumerate (word_to_guess):
        if letter == user_letter:
            word_to_guess_squares[index] = user_letter  # Открываем угаданную букву
        else:
            lives=lives-1
        if lives==0:
            print("You lost!")

# Когда цикл завершится, выводим полное слово
print ("Congratulations, you guessed the word:", word_to_guess)


