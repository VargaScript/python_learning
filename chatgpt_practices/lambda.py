#1. Lambda function to multiply a number by 5
from functools import reduce

addition = lambda x: x * 5
print(addition(3))

#2. Lambda function to determine if a number is even or odd
is_even = lambda x: True if x % 2 == 0 else False
print(is_even(1))

#3. Square each number on a list of integers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

#4. Select strings longer than 5
words = ["Adair", "Dhayana", "Monserrat", "Chris"]
char_length = list(filter(lambda word: len(word) > 5, words))
print(char_length)

#5. Check if a word starts with the letter "a"
checking_a = ["Apple", "banana", "Avocado", "cherry", "apricot", "Berry", "almond", "fig", "Anise", "grape"]
word_starts_with_a = list(filter(lambda word: word[0].lower() == "a", checking_a))
print(word_starts_with_a)

#6. Sort the list of tuples by the second element in a tuple
data = [("apple", 5), ("banana", 2), ("cherry", 8), ("date", 4), ("elderberry", 1)]
sorted_tuples = sorted(data, key=lambda tup: tup[1], reverse=True)
print(sorted_tuples)

#7. Multiply all the list by using reduce()
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
multiply_all = reduce(lambda first_number, second_number: first_number * second_number, numbers)
print(multiply_all)

#8. Use map to return the length of each word
length_of_word = ["Apple", "banana", "Avocado", "cherry", "apricot", "Berry", "almond", "fig", "Anise", "grape"]
word_length = list(map(lambda word: len(word), length_of_word))
print(word_length)

#9. Two arguments, sum them up and return it divided by 2
real_number = lambda num_1, num_2: num_1 + num_2 / 2
print(real_number(100, 50))

#10. Filter numbers greater than 50 using filter()
numbers = [10, 25, 47, 55, 63, 21, 88, 12, 59]
greater_than = list(sorted(filter(lambda number: number > 50, numbers), reverse=True))
print(greater_than)