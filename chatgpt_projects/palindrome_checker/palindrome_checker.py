"""def is_palindrome(word):
    cleaned_word = word.strip().lower().replace(" ", "").replace(",", "").replace(".", "").replace("?", "")
    reversed_word = word[::-1].strip().lower().replace(" ", "").replace(",", "").replace(".", "").replace("?", "")

    if reversed_word == cleaned_word:
        print(f"The word {word} is palindrome")
    else:
        print(f"The word {word} is not a palindrome")

users_word = input("Enter a word to check if it´s palindrome or not: ")
is_palindrome(users_word)"""

def is_palindrome(word):
    """Takes a word or phrase and verifies if it´s a palindrome(Is read equals frontwards and backwards)
    Example: ana = ana
             adair != riada
    """
    
    text = word.strip().lower().replace(" ", "").replace(",", "").replace(".", "").replace("?", "")
    return text == text[::-1]

users_word = input("Enter a word to check if it´s palindrome or not: ")
is_palindrome(users_word)

if is_palindrome(users_word):
    print(f"The word {users_word} is palindrome")
else:
    print(f"The word {users_word} is not a palindrome")