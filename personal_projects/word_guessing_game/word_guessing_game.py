#Input characters to try to find the final word

"""
Necessary steps
    1. Greet the user
    2. Generate a random word
    3. Define failed attempts, total attempts and the word
    4. Check if the character is in the word and print the character
    5. Check if the user has remaining attempts
"""

import random

#This could be done with an external library to generate real random words, not just predefined ones
list_of_words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

users_name = input("Whats your name?")
print(f"Hello, {users_name}, good luck!")

random_word = random.choice(list_of_words)

failing_attempts = 12
word_guessed = ''

while failing_attempts > 0:
    failed_attempts = 0
    for char in random_word:
        if char in word_guessed:
            print(char)
        else:
            print("_")
            failed_attempts += 1
                
        
        
        if word_guessed not in random_word:
            failing_attempts -= 1
            
            print("Wrong")
            print(f"You have {failing_attempts} more attempts")
            
            if failed_attempts == 0:
                print("You lose")