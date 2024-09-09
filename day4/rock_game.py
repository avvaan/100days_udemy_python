import random

# Картинки для камня, ножниц и бумаги с правильным переносом строк
rock_pict = (
    "    _______\n"
    "---'   ____) \n"
    "      (_____) \n"
    "      (_____) \n"
    "      (____) \n"
    "---.__(___) \n"
)

scissors_pict = (
    "    _______\n"
    "---'   ____)____ \n"
    "          ______) \n"
    "       __________) \n"
    "      (____) \n"
    "---.__(___) \n"
)

paper_pict = (
    "    _______\n"
    "---'   ____)____ \n"
    "          ______) \n"
    "          _______) \n"
    "         _______) \n"
    "---.__________) \n"
)

# Словари для выбора картинки и названия выбора
choices = {"R": (rock_pict, "Rock"), "P": (paper_pict, "Paper"), "S": (scissors_pict, "Scissors")}

# Получение и проверка ввода пользователя
user_choice = input ("Enter your choice (R for Rock, P for Paper, S for Scissors): ").upper ()

if user_choice not in choices:
    print ("Invalid choice. Please choose R, P, or S.")
    exit ()

# Компьютер случайным образом выбирает
computer_choice = random.choice (list (choices.keys ()))


# Функция для отображения результата
def who_won(man_choice, computer_choice):
    if man_choice == computer_choice:
        return "It's a Draw!"

    # Логика победителя
    win_conditions = {("R", "S"), ("P", "R"), ("S", "P")}
    if (man_choice, computer_choice) in win_conditions:
        return "You won!"
    else:
        return "You lost!"


# Вывод выборов игрока и компьютера
print (f"You chose: {choices[user_choice][1]}")
print (choices[user_choice][0])  # Печать изображения игрока
print (f"Computer chose: {choices[computer_choice][1]}")
print (choices[computer_choice][0])  # Печать изображения компьютера

# Определение и вывод результата игры
result = who_won (user_choice, computer_choice)
print (result)
