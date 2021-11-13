# Assignment 2B
# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is ____.

apples_quantity = int(input("How many apples you want to buy: "))
orange_quantity = int(input("How many oranges you want to buy: "))

apple_Price = 20
orange_Price = 25

apple_Amount = 0
orange_Amount = 0

if apples_quantity < 0 or orange_quantity < 0:
    print("Quantity cannot be less than zero")
else :
    apple_Amount = apples_quantity * apple_Price
    orange_Amount = orange_quantity * orange_Price
    print("The total amount is: " + str(apple_Amount + orange_Amount))