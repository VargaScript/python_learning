#Input a number and try to find the match

"""
Necessary steps
    1. The user gives a range to generate a random number to guess on
    2. Store the user´s number
    3. Compare the number and print if the user´s above or below the number
"""

import random

ranges = input("Enter 2 numbers for the range of numbers to guess on, separated by a comma or space: ")

if " " in ranges: 
    lower_range, higher_range = ranges.split()
elif ",":
    lower_range, higher_range = ranges.split(",")
else: 
    print("Enter a valid separator")
    exit()
    
lower_range, higher_range = int(lower_range), int(higher_range)
machines_number = int(random.randint(lower_range, higher_range))

if higher_range >= 1000:
    chances = 10
else:
    chances = 7

counter = 0

while counter < chances:
    counter += 1
    users_number = int(input("Enter a valid number to play the game: "))
    if users_number == machines_number: 
        print(f"Your guess {users_number} is the correct number! Congratulations")
        break
    elif users_number > machines_number:
        print(f"Your guessed number {users_number} is too high, try with a lower number")
    elif users_number < machines_number:
        print(f"Your guessed number {users_number} is too low, try a higher number")
    else: 
        print("Try to guess a real integer number, maybe that works")

    if counter == chances:
        print(f"Game over, the number was {machines_number}")