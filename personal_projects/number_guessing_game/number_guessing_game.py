import random

users_name = input("Tell me your name: ")

def greeting(name:str) -> None:
    """
    Takes the user´s name and gives a greeting
    :param name: Takes the user´s name
    """
    print(f"Hello, {name}, good luck!")

greeting(users_name)

guessing_range = input("Give me a range of two numbers to guess on, separated by a space or a comma: ")

if " " in guessing_range:
    lower_range, higher_range = guessing_range.split()
elif "," in guessing_range:
    lower_range, higher_range = guessing_range.split(",")
else:
    print("Enter a valid separator")
    exit()

lower_range, higher_range = int(lower_range), int(higher_range)

def generate_machines_number() -> int:
    """
    Generates a random number between the ones that the user specified
    :return: 34 (User´s numbers: 1,100)
    """
    random_machines_number = random.randint(lower_range, higher_range)
    return random_machines_number

machines_number = generate_machines_number()
attempts = 7
wrong_guesses = 0

while wrong_guesses < attempts:
    while True:
        try:
            users_guess = int(input("Type a number to try to find the right number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number")

    if users_guess == machines_number:
        print(f"Congrats! You guessed the right number, it was {machines_number}")
        break
    elif users_guess > machines_number:
        print(f"You´re going high, try with a smaller number")
    elif users_guess < machines_number:
        print(f"You´re going too low, try with a bigger number")
    else:
        print(f"Try with a real number between {lower_range} and {higher_range}")

    print(f"You have {attempts - wrong_guesses - 1} attempts left")
    wrong_guesses += 1

    if wrong_guesses == attempts:
        print(f"You lost! The right number was {machines_number}")