"""def square_list(numbers):
    squared_list = []
    for number in numbers:
        squared_number = number ** 2
        squared_list.append(squared_number)
    return squared_list

numbers_list: list[int] = [1, 2, 3, 4, 5]
print(square_list(numbers_list))

def count_vowels(words):
    vowel_amount = 0
    lower_sentence = words.lower()
    for letter in lower_sentence:
        if letter in ["a", "e", "i", "o", "u"]:
            vowel_amount += 1
    return vowel_amount

sentence: str = "Adair Isai Vargas Pastrana"
print(count_vowels(sentence))

def merge_dictionaries(*dictionaries):
    merged_dict = {}
    for dictionary in dictionaries:
        for key, value in dictionary.items():
            if key in merged_dict:
                merged_dict[key] += value
            else:
                merged_dict[key] = value
    return merged_dict

dict_1 = {"first": 1, "second": 2, "third": 3}
dict_2 = {"first": 1, "second": 2, "Third": 3}
print(merge_dictionaries(dict_1, dict_2))

def is_palindrome(sentence):
    clean_sentence = sentence.lower().replace(" ", "")
    clean_sentence_backwards = clean_sentence[::-1]
    if " " in sentence:
        if clean_sentence == clean_sentence_backwards:
            return f"The phrase '{sentence}' is a palindrome!"
        else:
            return f"The phrase '{sentence}' is not a palindrome"
    else:
        if clean_sentence == clean_sentence_backwards:
            return f"The word '{sentence}' is a palindrome!"
        else:
            return f"The word '{sentence}' is not a palindrome"

word = str(input("Write a word or phrase to know if it´s a palindrome: "))
print(is_palindrome(word))"""

def recursive_factorial(n):
    if n == 3:
        return 3
    else:
        return n * recursive_factorial(n - 1)

print(recursive_factorial(5))

def recursive_fibonacci(limit):
    if limit <= 1:
        return 1
    else:
        return recursive_fibonacci(limit - 2) + recursive_fibonacci(limit - 1)

print(recursive_fibonacci(11))

