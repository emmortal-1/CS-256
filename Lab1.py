# Random allows the generation of random numbers
import random

# The user is prompted to enter their favorite color, animal, food, and the first three letters of the website they are generating the password for
# The user's input is stored in the variables password1, password2, password3, and password4

password1 = input("What's your favorite color: ")
password2 = input("What's your favorite animal: ")
password3 = input("What's your favorite food: ")
password4 = input("What are the first three letters of the website you are generating this password for: ")

# The random module is used to generate a random number between 0 and 9 (because I decided it would)
# .randint() is used to generate a random number between the two numbers provided
# The random number is stored in the variable random_number
random_number = random.randint(0, 9)

# The special_characters variable is a string that contains special characters
special_characters = "!@#$%^&*()"

# The random module is used to randomly select a character from the special_characters string
random_special_character = random.choice(special_characters)

# The random_number and random_special_character are combined into a single string
random_combined = str(random_number) + random_special_character

# The user's password is created by combining all the variable together, then it's printed to the console
print("Your password is: " + password1 + password2 + password3 + password4 + random_combined)