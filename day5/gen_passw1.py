import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Генерация случайных символов для пароля
generated_password_letters = random.sample(letters, nr_letters)
generated_password_symbols = random.sample(symbols, nr_symbols)
generated_password_numbers = random.sample(numbers, nr_numbers)

# Объединение всех частей пароля
generated_password = generated_password_letters + generated_password_symbols + generated_password_numbers

# Перемешивание всех символов
random.shuffle(generated_password)

# Преобразование списка в строку
password = "".join(generated_password)

print(f"This is your password: {password}")