# The Python import random module in Python defines a series of functions for generating or manipulating random integers.
import random

# Displays the string "Welcome to Guess the Number!" in the terminal.
print("Welcome to Guess the Number!")
# Displays the string "The rules are simple. I will think of a number, and you will try to guess it." in the terminal.
print("The rules are simple. I will think of a number, and you will try to guess it.")

# Selects a random integer between 1 & 10, and then places it into a variable called 'number'.
number = random.randint(1, 10)
# Places the Boolean 'False' into a variable named 'isGuessRight'
isGuessRight = False
# Whilst the variable 'isGuessRight' is not equal to 'True' keep asking user to guess 'number'.
while isGuessRight != True:
    # The string "Guess a number between 1 and 10: " is placed into an 'input()' function which is then placed into a variable called 'guess'.
    guess = input("Guess a number between 1 and 10: ")
    # The 'guess' variable is placed inside an 'int()' function which takes the integer input by the user
    # and uses an 'if statement' to find out if that integer is equal to the variable 'number'.
    if int(guess) == number:
        # The string "You guessed {}. That is correct! You win!" will be displayed in the terminal if the variable 'isGuessRight' is equal to 'True'.
        # '{}' will be be replaced with the correct number because the 'guess' variable is inside the format() function
        # which takes the value of the 'guess' variable and puts it in '{}'.
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    # The string "You guessed {}. Sorry, that isn’t it. Try again." will be displayed in the terminal if the variable 'isGuessRight' is equal to 'False'.
    # '{}' will be be replaced with the incorrect number because the 'guess' variable is inside the format() function
    # which takes the value of the 'guess' variable and puts it in '{}'.
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
