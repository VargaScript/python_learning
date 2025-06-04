# Sort alphabetically, ignoring case
names = ["alice", "Bob", "CHARLIE", "dave"]
names.sort(key=str.lower)
print(names)

#Sort by word length
words = ["apple", "banana", "kiwi", "watermelon"]
words.sort(key=len)
print(words)

#Sort by its absolute value
nums = [10, -5, 3, -20, 15]
nums.sort(key=abs)
print(nums)

#Sort by number of vowels
"""words = ["pear", "banana", "kiwi", "grape"]

def count_vowels(words):
    for word in words:
        vowels = ["a", "e", "i", "o", "u"]
        quantity = 0
        if vowels in word:
            quantity += 1
            return quantity

words.sort(key=count_vowels)
print(words)"""
"""
words = ["pear", "banana", "kiwi", "grape"]

def count_vowels(word):
    vowels = "aeiou"
    return sum(1 for letter in word.lower() if letter in vowels)

words.sort(key=count_vowels)


def count_vowels(word):
    vowels = "aeiou"
    return sum(1 for letter in word.lower() if letter in vowels)

print(words)

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 30}
]

people.sort(key=people["age"])

"""



#Part 2
words = ["banana", "Apple", "cherry", "avocado"]
words.sort(key=str.lower)
print(words)

numbers = [-10, 5, -2, -8, 3]
numbers.sort(key=abs)
print(numbers)

names = ["Tom", "Elizabeth", "Anna", "Joe"]
names.sort(key=len)
print(names)

pairs = [(1, 5), (2, 1), (4, 3), (3, 2)]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

pairs.sort(key=lambda pair: pair[0] + pair[1])
print(pairs)

words = ["banana", "apple", "cherry", "date", "kiwi"]

def counting_vowels(words_to_validate):
    vowels = "aeiou"
    return sum(1 for letter in words_to_validate.lower() if letter in vowels)

words.sort(key=counting_vowels, reverse=True)
print(words)

"""people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

def extract_age(people):
    for person in people:
        dict_person = person[0]
        for dict_person in

people.sort(key=extract_age)
print(people)"""


sentences = [
    'Learn Python programming',
    'Sorting is fun',
    'Practice every day'
]

def get_last_word(sentence):
    return sentence.split()[-1].lower()

sentences.sort(key=get_last_word)
print(sentences)

files = ['report.pdf', 'data.csv', 'image.png', 'script.py']

def order_by_extension(files):
    return files.split(".")[-1].lower()

files.sort(key=order_by_extension)
print(files)

string_numbers = ['10', '1', '20', '2']

def order_numbers(numbers):
    return int(numbers)

string_numbers.sort(key=order_numbers)
print(string_numbers)