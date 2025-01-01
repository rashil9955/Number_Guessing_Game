import random

min = 0
max = 100
value_range = 10
random_number = random.randint(min, max)

lower_range = random_number - 10
upper_range = random_number + 10

Flag = True


print()
print("Welcome to number guessing game\n")


print("I just thought of a number. Can you guess it?\n")


if lower_range < min:
    lower_range = 0

if upper_range > max:
    upper_range = 100


while Flag:

    # test weather the input is in the range or not
    user_input = int(input("Enter your guess: "))

    if user_input < min or user_input > max:
        print("Please enter a number between 1 and 100\n")
        Flag = False



    #if guessed the correct number,
    if user_input == random_number:
        print("You guessed it!\n")

        #end the while loop
        Flag = False

    elif user_input > upper_range:
        print("your guess is too high!\n")


    elif user_input < lower_range:
        print("your guess is too low!\n")


    elif (user_input < upper_range) and (user_input > random_number):
        print("your guess is slightly high\n")


    elif (user_input > lower_range) and (user_input < random_number):
        print("your guess is slightly low\n")

    else:
        print("Invalid Input\n")
        Flag = False

