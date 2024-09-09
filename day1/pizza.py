print("Welcome to Python pizza deliveries!")
size = input('What size pizza do you want S, M or L?')

small=15
medium=20
large=25
pep = 2
cheese = 1
if size == "L":
    price = large
if size == "M":
    price = medium
if size=="S":
    price = small

pepperoni = input ("do you want pepperoni on your pizza? y/n")
if pepperoni == "y" and size != "S":
    price = price + pep
else:
    price = price+2
extra_cheese: str = input ("do you want extra cheese on your pizza? y/n")
if extra_cheese == "y":
    price = price + cheese
else:
    price = price
print(f"your final bill is ${price}")
