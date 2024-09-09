for number in range(1,101):
    number_3=number%3
    number_5=number%5
    if number_3==0 and number_5==0:
        number = ("FizzBuzz")

    elif number_3==0:
         number = ("Fizz")
    elif number_5==0:
        number=('Buzz')
    print(number)
