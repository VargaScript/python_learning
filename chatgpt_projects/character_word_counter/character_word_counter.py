def word_counter(phrase):
    words = len(phrase.split())
    characters = len(phrase)
    print(f"Your phrase has {words} words and {characters} characters", end="\n")

users_phrase = input("Type a phrase, I will count all of the characters an words in it: ")
word_counter(users_phrase)